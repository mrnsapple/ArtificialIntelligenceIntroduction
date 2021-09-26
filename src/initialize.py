from ArtificialIntelligenceIntroduction.src.node import Node
from ArtificialIntelligenceIntroduction.src.problem import Problem
from ArtificialIntelligenceIntroduction.src.tree_search import TreeSearch
from ArtificialIntelligenceIntroduction.src.algorithm import Algorithm, AlgorithmType
import ArtificialIntelligenceIntroduction.src.protocol as protocol

import socket
import logging
from logging.handlers import RotatingFileHandler
import os
import json

class InitializeException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        
class Initialize():
    def __init__(self, algorithm_type:AlgorithmType, problem:Problem, algorithm:Algorithm) -> None:
        self.algorithm_type =algorithm_type
        self.problem = problem
        self.algorithm = algorithm
        self.tree = TreeSearch()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.port = 12000
        self.host = "localhost"
        self.set_logs()  
        self.connect()

    def set_logs(self):
    
        """
        set up  logging
        """
        self.fantom_logger = logging.getLogger()
        self.fantom_logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter(
            "%(asctime)s :: %(levelname)s :: %(message)s", "%H:%M:%S")
        # file
        if os.path.exists("./logs/fantom.log"):
            os.remove("./logs/fantom.log")
        self.file_handler = RotatingFileHandler('./logs/fantom.log', 'a', 1000000, 1)
        self.file_handler.setLevel(logging.DEBUG)
        self.file_handler.setFormatter(self.formatter)
        self.fantom_logger.addHandler(self.file_handler)
        # stream
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.WARNING)
        self.fantom_logger.addHandler(stream_handler)

    def connect(self):
        logging.debug('This message should go to the log file')
        self.socket.connect((self.host, self.port))

    def reset(self):
        self.socket.close()

    def answer(self, question):
        # work
        print(question)
        print("\n\n")   

        data = question["data"]
        game_state = question["game state"]
        response_index = random.randint(0, len(data)-1)
        # log
        self.fantom_logger.debug("|\n|")
        self.fantom_logger.debug("fantom answers")
        self.fantom_logger.debug(f"question type ----- {question['question type']}")
        self.fantom_logger.debug(f"data -------------- {data}")
        self.fantom_logger.debug(f"response index ---- {response_index}")
        self.fantom_logger.debug(f"response ---------- {data[response_index]}")
        return response_index

    def get_data(self):
        data = protocol.receive_json(self.socket)
        if not data:
            return None
        data = json.loads(data)
        return data

    def send_data(self, data):
        #response = self.answer(data)
        # send back to server

        #if not data:
        #    raise InitializeException("No data to be sent")
        bytes_data = json.dumps(data).encode("utf-8")
        protocol.send_json(self.socket, bytes_data)

    def run(self):
        end = False
        while not end:
            print("IN LOOP")
            received_message = self.get_data()
            self.fantom_logger.debug("|\n|")
            self.fantom_logger.debug("fantom answers")
            self.fantom_logger.debug(f"question type ----- {received_message['question type']}")
            self.fantom_logger.debug(f"data -------------- {received_message['data']}")

            response =self.launch_tree(received_message)
            self.fantom_logger.debug(f"response index ---- {response}")
            self.fantom_logger.debug(f"response ---------- {received_message['data'][response]}")
        
            self.send_data(response)
            if not received_message:
                print("no message, finished learning")
                end = True


    def launch_tree(self, data):
        self.problem.initial_state = Node(data)
        node:Node = self.tree.tree_search(self.problem, self.algorithm)
        return node.data