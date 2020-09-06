import socket


def f1():
    f = open('index.html', 'rb')
    data = f.read()
    f.close()
    return data


def f2():
    f = open('article.html', 'rb')
    data = f.read()
    f.close()
    return data


routers = [
    ('/xxx', f1),
    ('/ooo', f2)
]


def run():
    sock = socket.socket()
    sock.bind(('127.0.0.1', 8080))
    sock.listen()

    while True:
        conn, addr = sock.accept()  # hang on
        # 用户连接，获取用户发送的数据
        data = conn.recv(8096)
        # print(data)
        data = str(data, encoding='utf-8')
        header, body = data.split('\r\n\r\n')
        temp_list = header.split('\r\n')
        method, url, protocal = temp_list[0].split()
        conn.send(b"HTTP/1.1 200 OK\r\n\r\n")

        func_name = None
        for item in routers:
            if item[0] == url:
                func_name = item[1]
                break

        if func_name:
            response = func_name()
        else:
            response = b'404'

        conn.send(response)
        conn.close()


if __name__ == "__main__":
    run()
