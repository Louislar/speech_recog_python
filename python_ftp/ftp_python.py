from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

#例項化虛擬使用者，這是FTP驗證首要條件
authorizer = DummyAuthorizer()

#新增使用者許可權和路徑，括號內的引數是(使用者名稱， 密碼， 使用者目錄， 許可權)
authorizer.add_user('user', '12345', 'C://testing_folder/', perm='elradfmw')

#新增匿名使用者 只需要路徑
authorizer.add_anonymous('C://testing_folder/')

#初始化ftp控制代碼
handler = FTPHandler
handler.authorizer = authorizer

#新增被動埠範圍
handler.passive_ports = range(2000, 2333)

#監聽ip 和 埠
server = FTPServer(('127.0.0.1', 2121), handler)

#開始服務
server.serve_forever()