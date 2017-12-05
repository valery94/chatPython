import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('127.0.0.1', 80))
serverSocket.setblocking(0)

print("Server start work!")

clients = []

while True:
    try:
        message, ip = serverSocket.recvfrom(1024)

        if ip not in clients:
            print(str('Add in chat new user: ip ->'.encode()) + str(ip))
            clients.append(ip)
            
        print(str(ip) + str(message))
        for client in clients:
            serverSocket.sendto(message, client)       
    except:
        pass

serverSocket.close()
