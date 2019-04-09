from socket import socket, AF_INET, SOCK_DGRAM

serverName = "ec2-34-221-214-226.us-west-2.compute.amazonaws.com"
serverPort = 12001

clientSocket = socket(AF_INET, SOCK_DGRAM)
message = raw_input("Input lowercase sentence: ")

clientSocket.sendto(message, (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print("I have received modified info from server: " + modifiedMessage)
clientSocket.close()
