#part1
import socket
serverPort=12000
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ("The server is ready to receive")
while 1:
    connectionSocket, addr = serverSocket.accept()
    byte_sentence1 = connectionSocket.recv(1024)
    utf_sentence1 = byte_sentence1.decode("utf-8")
    f = open(utf_sentence1, "x")
    ##

    byte_sentence2 = connectionSocket.recv(1024)
    utf_sentence2 = byte_sentence2.decode("utf-8")
    f=open(utf_sentence1,"a")
    f.write(utf_sentence2+"\n")
    ##
    byte_sentence3 = connectionSocket.recv(1024)
    utf_sentence3 = byte_sentence3.decode("utf-8")
    f = open(utf_sentence1, "a")
    f.write(utf_sentence3+"\n")
    ##

    byte_sentence4 = connectionSocket.recv(1024)
    utf_sentence4 = byte_sentence4.decode("utf-8")
    f = open(utf_sentence1, "a")
    f.write(utf_sentence4+"\n")

    connectionSocket.close()
    break#test ederken sıkıntı cıkardıgı icin break dedim.