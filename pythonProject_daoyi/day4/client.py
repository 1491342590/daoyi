import socket

ip = socket.gethostbyname(socket.gethostname())

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg = input('请输入要发送的内容：')
info = msg.encode()
s.connect(('127.0.0.1',8005))
s.send(info)
s.close()