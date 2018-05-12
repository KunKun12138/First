import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.sina.com.cn', 80))
# 发送数据:
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection:close\r\n\r\n')

buffer = []
while True:
    d = s.recv(1024)
    if d :
        buffer.append(d)
    else:
        break

data = b''.join(buffer)
print(data)

header,html = data.split(b"\r\n\r\n",1)
print("头部：\n",header.decode('utf-8'))
print("数据：",html.decode('utf-8'))


s.close()




