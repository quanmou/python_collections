import random
from locust import HttpUser, task, between, SequentialTaskSet, tag


class MyTaskCase(SequentialTaskSet):
    # 初始化方法，相当于 setup
    def on_start(self):
        pass

    # @task python中的装饰器，告诉下面的方法是一个任务，
    # 这个装饰器和下面的方法被复制多次，改动一下，就能写出多个接口
    # 装饰器后面带上(数字)代表在所有任务中，执行比例
    # 要用这个装饰器，需要头部引入 从locust中，引入 task
    @task
    @tag("leave_1")
    def register_(self):  # 一个方法，方法名称可以自己改
        url = '/erp/register'  # 接口请求的URL地址
        # 定义请求头为类变量，这样其他任务也可以调用该变量
        self.headers = {"Content-Type": "application/json"}
        self.username = "locust_" + str(random.randint(10000, 100000))
        self.pwd = '1234567890'
        # post请求的 请求体
        data = {"name": self.username, "pwd": self.pwd}
        # 使用self.client发起请求，请求的方法根据接口实际选,
        # catch_response 值为True 允许为失败 ，
        # name 设置任务标签名称   -----可选参数
        with self.client.post(url,
                              json=data,
                              headers=self.headers,
                              catch_response=True) as rsp:
            if rsp.status_code > 400:
                print(rsp.text)
                rsp.failure('register_ 接口失败！')

    @task  # 装饰器，说明下面是一个任务
    def login_(self):
        url = '/erp/loginIn'  # 接口请求的URL地址
        data = {"name": self.username, "pwd": self.pwd}
        with self.client.post(url,
                              json=data,
                              headers=self.headers,
                              catch_response=True) as rsp:
            # 提取响应json 中的信息，定义为 类变量
            self.token = rsp.json()['token']
            if rsp.status_code < 400 \
                    and rsp.json()['code'] == "200":
                rsp.success()
            else:
                rsp.failure('login_ 接口失败！')

    @task  # 装饰器，说明下面是一个任务
    def getuser_(self):
        url = '/erp/user'  # 接口请求的URL地址
        # 引用上一个任务的 类变量值   实现参数关联
        headers = {"Token": self.token}
        # 使用self.client发起请求，请求的方法 选择 get
        with self.client.get(url,
                             headers=headers,
                             catch_response=True) as rsp:
            if rsp.status_code < 400:
                rsp.success()
            else:
                rsp.failure('getuser_ 接口失败！')

    # 结束方法， 相当于teardown
    def on_stop(self):
        pass


# 定义一个运行类 继承HttpUser类，所以要从locust中引入HttpUser类
class UserRun(HttpUser):
    tasks = [MyTaskCase]
    # 设置运行过程中间隔时间，需要从locust中引入between
    wait_time = between(0.1, 3)
