import socket
import pymysql


def f1():
    f = open('index.html', 'rb')
    data = f.read()
    f.close()
    return data


def f2():
    f = open('article.html', 'r', encoding='utf-8')
    data = f.read()
    f.close()
    import time
    ctime = time.time()
    data = data.replace('@@sw@@', str(ctime))
    return bytes(data, encoding='utf-8')


def f3():
    """
    动态页面, 从数据库中读取用户名和密码，替换掉html中的占位符，并返回html数据
    """
    conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='djangotest')
    # 游标设置为字典类型
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select id, username, password from userinfo")
    user_list = cursor.fetchall()
    cursor.close()
    conn.close()
    print(user_list)
    content_list = []
    for row in user_list:
        tp = "<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (row['id'], row['username'], row['password'])
        content_list.append(tp)
    content = "".join(content_list)

    f = open('user_list.html', 'r', encoding='utf-8')
    template = f.read()
    f.close()

    # 模板渲染(模板+数据）
    data = template.replace('@@content@@', content)
    return bytes(data, encoding='utf-8')


def f4():
    """
    使用python的模板引擎Jinja2来实现模板渲染
    """
    conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='djangotest')
    # 游标设置为字典类型
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select id, username, password from userinfo")
    user_list = cursor.fetchall()
    cursor.close()
    conn.close()

    f = open('host_list.html', 'r', encoding='utf-8')
    data = f.read()
    f.close()

    from jinja2 import Template
    template = Template(data)
    data = template.render(xxxxx=user_list)
    print(data)
    return bytes(data, encoding='utf-8')


routers = [
    ('/xxx', f1),
    ('/ooo', f2),
    ('/user_list.html', f3),
    ('/host_list.html', f4)
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
