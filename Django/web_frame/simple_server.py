import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 8080))
sock.listen(5)

while True:
    conn, addr = sock.accept()  # 阻塞
    # 有用户连接，获取用户发送数据
    data = conn.recv(8096)
    print(data)
    conn.send(b'123123')
    conn.close()
