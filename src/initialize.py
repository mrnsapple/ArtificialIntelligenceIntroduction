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
    """
    The base class structure of the project is composed of the initialize class,
    It is the class used to start the communication with the server. 
    All project clases are intialized and destroyed in this class
    """

    """
    @param algorithm_type:AlgorithmType The type chosen to solve the algorithm 
    @param problem:Problem  Logics that are specific for each problem we solve
    @param algorithm: All logic for the specific algorithm used to move in the tree search
    @return None
    """
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

    """
    Initialize log files
    
    @return None
    """
    def set_logs(self):
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

    """
    Connect to the server

    @return None
    """
    def connect(self):
        logging.debug('This message should go to the log file')
        self.socket.connect((self.host, self.port))

    """
    Close connection with server

    @return None
    """
    def reset(self):
        
        self.socket.close()

    """
    Get data from the server

    @return dict the data retrieved from the server 
    """
    def get_data(self):
        data = protocol.receive_json(self.socket)
        if not data:
            return None
        data = json.loads(data)
        return data

    """
    Send data to the server

    @param data:dict data to send to the server
    @return None
    """
    def send_data(self, data):
        #if not data:
        #    raise InitializeException("No data to be sent")
        bytes_data = json.dumps(data).encode("utf-8")
        protocol.send_json(self.socket, bytes_data)

    """
    Loop of the game, it will finish when one of the player wins and server stops sending data to client

    @return None
    """
    def run(self):
        end = False
        while not end:
            print("IN LOOP")
            received_message = self.get_data()
            if not received_message:
                print("no message, finished learning")
                end = True
                continue
            self.fantom_logger.debug("|\n|")
            self.fantom_logger.debug("fantom answers")
            self.fantom_logger.debug(f"question type ----- {received_message['question type']}")
            self.fantom_logger.debug(f"data -------------- {received_message['data']}")

            response =self.launch_tree(received_message)
            self.fantom_logger.debug(f"response index ---- {response}")
            self.fantom_logger.debug(f"response ---------- {received_message['data'][response]}")
        
            self.send_data(response)
          

    """
    Run the tree search that will return an answer to the server given a specific problem and algorithm

    @param data:Dict The information received from the server
    @return Node answer to give to the server
    """
    def launch_tree(self, data):
        
        self.problem.initial_state = Node(data)
        node:Node = self.tree.tree_search(self.problem, self.algorithm)
        return 0
