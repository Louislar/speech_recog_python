# coding=utf-8
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


# #例項化虛擬使用者，這是FTP驗證首要條件
# authorizer = DummyAuthorizer()

# #新增使用者許可權和路徑，括號內的引數是(使用者名稱， 密碼， 使用者目錄， 許可權)
# authorizer.add_user('user', '12345', '/home/wmlab/speech_recog_python/python_ftp/', perm='elradfmw')

# #新增匿名使用者 只需要路徑
# authorizer.add_anonymous('/home/wmlab/speech_recog_python/python_ftp/')

# #初始化ftp控制代碼
# handler = FTPHandler
# handler.authorizer = authorizer

# #新增被動埠範圍
# handler.passive_ports = range(2000, 2333)

# #監聽ip 和 埠
# server = FTPServer(('140.115.54.22', 2121), handler)

# #開始服務
# server.serve_forever()

class Ftp_server():
    def __init__(self):
        self.usr_nm = 'user'
        self.usr_pw = '12345'
        self.server_root_path = '/home/wmlab/speech_recog_python/python_ftp/'
        self.server_ip = '140.115.54.22'
        self.server_port = 2121
    
    def server_online(self):
        #例項化虛擬使用者，這是FTP驗證首要條件
        authorizer = DummyAuthorizer()

        #新增使用者許可權和路徑，括號內的引數是(使用者名稱， 密碼， 使用者目錄， 許可權)
        authorizer.add_user(self.usr_nm, self.usr_pw, self.server_root_path, perm='elradfmw')

        #新增匿名使用者 只需要路徑
        authorizer.add_anonymous('/home/wmlab/speech_recog_python/python_ftp/')

        #初始化ftp控制代碼
        handler = FTPHandler
        handler.authorizer = authorizer

        #新增被動埠範圍
        handler.passive_ports = range(2000, 2333)

        #監聽ip 和 埠
        server = FTPServer((self.server_ip, self.server_port), handler)

        #開始服務
        server.serve_forever()
        pass
    pass

if __name__ == "__main__":
    ftp_server = Ftp_server()
    ftp_server.server_online()
