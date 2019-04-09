from socket import socket, AF_INET, SOCK_STREAM

serverName = ""
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input("Input lowercase sentence: ")

clientSocket.send(sentence)

modifiedSentence, serverAddress = clientSocket.recv(1024)
print("I have received modified info from server: " + modifiedSentence)

clientSocket.close()
