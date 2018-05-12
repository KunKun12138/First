from wsgiref.simple_server import make_server
from TheSecondChapter.serverTest2_1 import application

httpd = make_server('',8080,application)

print('开启8080端口服务....')

httpd.serve_forever()
