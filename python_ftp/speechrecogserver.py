# coding=utf-8
from ftp_python import Ftp_server
from testing_py import CMU_Sphinx_recognizer
from TCP_server_python27 import MultithreadingTCPServer

class Speech_server():
    def __init__(self):
        self.tcp_server_ip = '140.115.54.22'
        self.tcp_server_port = 12000

        self.ftp_server = Ftp_server()
        self.cmu_Sphinx_recognizer = CMU_Sphinx_recognizer()
        self.tcp_server = MultithreadingTCPServer(self.tcp_server_ip, self.tcp_server_port)
        pass

    def ftp_server_on(self):
        # 這會被bind住
        self.ftp_server.server_online()
        
    pass

if __name__ == "__main__":
    speech_server = Speech_server()
    speech_server.ftp_server_on()
    print('ftpftp')