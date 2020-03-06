import socket
import sys
import threading

from .node import Node

class Client(Node):

    def __init__(self):

        print("init")

        self.serverAddress = "localhost"
        self.serverPort = 25565
        self.clientReqAddress = "192.168.0.2"
        self.clientReqPort = 25566
        self.serverQueueMax = 10
        self.messageByteSize = 128

    def start(self):

        self.threads = {
            "client" : threading.Thread(target=self.startClient, daemon=True),
            "server" : threading.Thread(target=self.startServer, daemon=True)
        }

        self.threads.client.start()
        self.threads.server.start()

    def startClient(self):

        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientSocket.connect((self.clientReqAddress, self.clientReqPort))



        print("init")

    def startServer(self):

        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.bind((self.serverAddress, self.serverPort))
        self.serverSocket.listen(self.serverQueueMax)

        while True:

            clientConnection, clientAddress = self.serverSocket.accept()

            try:

                while True:

                    data = clientConnection.recv(messageByteSize)

                    if data:
                        print(data)
                    else:
                        print("breaking")
                        break

            finally:

                print("Server closing connection")
                clientConnection.close()
