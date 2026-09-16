import socket;
host = "localhost"
port = 5000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))

s.listen(1)
    
c,addre = s.accept()

print("Connection from :",str(addre))

c.send(b"Hello from server, how are U")

msg = "bye"

c.send(msg.encode())

s.close()