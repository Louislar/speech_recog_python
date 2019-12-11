# coding=utf-8
from socket import *
import threading
import sys
from testing_py import CMU_Sphinx_recognizer

class MultithreadingTCPServer:
    def __init__(self, name, port):
        self.serverName = name
        self.serverPort = port
        self.cmu_Sphinx_recognizer = CMU_Sphinx_recognizer()

    def start(self):
        try:
            serverSocket = socket(AF_INET, SOCK_STREAM)
            print('Bind server socket to', self.serverName, ':', self.serverPort)
            serverSocket.bind((self.serverName, self.serverPort))
            serverSocket.listen(1)
            print('Multithreading server binding success')
            while True:
                clientSocket, address = serverSocket.accept()
                thread = threading.Thread(target = self.__handleClient, args = (clientSocket,))
                thread.start()
            serverSocket.close()
        except:
            pass
            print('start fail')
        finally:
            print('Server shutdown.')
            
    def __handleClient(self, clientSocket):
        clientName, clientPort = clientSocket.getpeername()
        print('Connecting to', clientName, clientPort)
        tmp_result = ''
        try:
            while True:
                message = clientSocket.recv(1024)
                if len(message) is 0:
                    break
                sentence = message.decode()
                print(sentence)
                tmp_result = self._recog_func()
                print(tmp_result)
                capitalizedSentence = sentence.upper()
                # print(type(capitalizedSentence))
                # print('-----------start sentence-----------')
                # print(capitalizedSentence)
                # print('----------end sentence-------------')
                clientSocket.send(tmp_result)
                # clientSocket.send('tmp_result')
                
        except:
            # clientSocket.send(tmp_result)
            clientSocket.close()
        finally:
            print('Disconnecting to', clientName, ':', clientPort)

    def _recog_func(self, wav_file_path='./test_wwaavv.wav'):
        self.cmu_Sphinx_recognizer.wav_file = wav_file_path
        recog_result = self.cmu_Sphinx_recognizer.recognize()
        out_str = recog_result + '\n' + recog_result +'\n' + recog_result +'\n'
        return out_str
        

if len(sys.argv) < 3:
    serverName = '140.115.54.22'
    serverPort = 12001
else:
    serverName = sys.argv[1]
    serverPort = int(sys.argv[2])

if __name__ == "__main__":
    server = MultithreadingTCPServer(serverName, serverPort)
    server.start()

# server = MultithreadingTCPServer(serverName, serverPort)
# server.start()

