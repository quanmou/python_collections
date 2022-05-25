const string HELLO_YK = "thrift-test"
service HelloWorld {
    void ping(),
    string sayHello(),
    string sayMsg(1:string msg)
}