from socket import socket, AF_INET, SOCK_STREAM

serverName = "ec2-34-221-214-226.us-west-2.compute.amazonaws.com"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = raw_input("Input lowercase sentence: ")

clientSocket.send(sentence)

modifiedSentence = clientSocket.recv(1024)
print("I have received modified info from server: " + modifiedSentence)

clientSocket.close()
