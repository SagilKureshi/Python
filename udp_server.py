import socket
import time

host = 'localhost'
port = 65535

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

time.sleep(15)

s.sendto(b"Hello from UDP Server", (host,port))

msg = "Bye!"

s.sendto(msg.encode(),(host,port))
s.close()