import socket;

host = "localhost"
port = 1024

s = socket.socket()

s.bind((host,port))

s.listen(1)
    
c,addre = s.accept()

print("A client Accepted connection")

fname = c.recv(1024)

fname = str(fname.decode())

print("File name recived from client " + fname)


try:
    f = open(fname,'rb')
    content = f.read()
    c.send(content)
    print("File content send to client")
    f.close()

except FileNotFoundError:
    c.send(b"File does not exist")
c.close()