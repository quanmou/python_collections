"""
pip install thrift
"""

from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol

from helloworld import HelloWorld
from helloworld.constants import *
from helloworld.ttypes import *


try:
    # Make socket
    transport = TSocket.TSocket('127.0.0.1', 30303)
    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)
    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    # Create a client to use the protocol encoder
    client = HelloWorld.Client(protocol)
    # Connect!
    transport.open()
    client.ping()
    print("client: ping()")
    msg = client.sayHello()
    print(msg)
    msg = client.sayMsg(HELLO_YK)
    print(msg)
    transport.close()
except Thrift.TException as tx:
    print("%s" % tx.message)
