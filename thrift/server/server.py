import socket

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from helloworld import HelloWorld
from helloworld.ttypes import *


class HelloWorldHandler:
    def __init__(self):
        self.log = {}

    def ping(self):
        print("server function: ping()")

    def sayHello(self):
        print("sayHello()")
        return "say hello from " + socket.gethostbyname(socket.gethostname())

    def sayMsg(self, msg):
        print("sayMsg(" + msg + ")")
        return "say " + msg + " from " + socket.gethostbyname(socket.gethostname())


handler = HelloWorldHandler()

processor = HelloWorld.Processor(handler)
transport = TSocket.TServerSocket('127.0.0.1', 30303)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
print("Starting python server...")
server.serve()
print("server side: done!")
