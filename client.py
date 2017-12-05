import socket
import threading

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.connect(('127.0.0.1', 0))
clientSocket.setblocking(0)

def receving(name, sock):
    while True:
        try:
            tLock.acquire()
            while True:
                data, addr = sock.recvfrom(1024)
                print(str(data))
        except:
            pass
        finally:
            tLock.release()

tLock = threading.Lock()
rT = threading.Thread(target=receving, args=("RecvThread", clientSocket))
rT.start()

name = input("Name: ")
message = input(name + "-> ")
       
while True:
    if(message!=''):
        clientSocket.sendto(name.encode() + ": ".encode() + message.encode(), ('127.0.0.1',80))
    tLock.acquire()
    message = input(name + "-> ")
    tLock.release()

rT.join()
s.close()
