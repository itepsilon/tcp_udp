from socket import socket, AF_INET, SOCK_DGRAM

serverPort = 12001
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print("The server is ready to receive")

while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    print("Server received: " + message)
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage, clientAddress)
