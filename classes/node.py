from Crypto.Hash import SHA512
import secrets
import numpy

class Node:
    def __init__(self, incomingAddress, incomingPort, outgoingAddress, outgoingPort):

        self.incomingAddress = hostAddress
        self.incomingPort = incomingPort
        self.outgoingAddress = outgoingAddress
        self.outgoingPort = outgoingPort

        self.incomingNodes = []
        self.outgoingNodes = []

        self.maxIncomingQueuedNodes = 5
        self.maxIncomingNodes = 100
        self.maxOutgoingNodes = 100

        self.id = SHA512.new(bytes(str(incomingAddress + incomingPort + outgoingAddress + outgoingPort + secrets.token_bytes(256))))

        self.trainingImages
        self.trainingLabels
        self.testImages
        self.testLabels

        self.messageSendCount = 0
        self.messageRecvCount = 0
        self.messageShardByteSize = 128

        self.shutdown = False

        self.main()

    def createServerSocket(self):

        socketContext = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socketContext.bind((self.incomingAddress, self.incomingPort))
        socketContext.settimeout(10)
        socketContext.listen(self.maxIncomingQueuedNodes)

        return socketContext

    def handleIncomingPeer(self, clientSocket):

        while not self.shutdown:
            try:
                instructionBytes = clientSocket.recv(self.messageShardByteSize)
                if instructionBytes:
                    instructionString = "".join(map(chr, instructionBytes))
                    print(instructionString)
                else:
                    print("breaking")
                    break

            except keyboardInterrupt:
                raise

            except:
                FATAL("An unhandled exception occured")

        clientSocket.close()

    def main(self):

        serverSocket = self.createServerSocket()

        while not self.shutdown:
            try:
                print("Waiting to accept new peer")
                clientSocket, clientAddress = serverSocket.accept()
                clientSocket.settimeout(10)
                print("Accepting new peer connection")
                thread = threading.Thread(target = self.handleIncomingPeer, args = [clientSocket])
                thread.start()
                print("Allocated thread to peer")

            except keyboardInterrupt:
                self.stop()
                continue

            except:
                FATAL("An unhandled exception occured")
                self.stop()
                continue

        serverSocket.close()

    def stop(self):
        self.shutdown = True
