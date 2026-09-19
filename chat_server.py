import socket

host = 'localhost'
port = 65535

s = socket.socket()
s.bind((host, port))
s.listen(1)
print("Waiting for a connection...")
c, addr = s.accept()
print("A client connected")

while True:
    data = c.recv(1024)
    if not data:
        break
    print("from client: " + data.decode())
    
    data1 = input("Enter Response: ")
    # CHANGED: Use .encode() to convert the string to bytes
    c.send(data1.encode())

print("Client disconnected.")
c.close()
s.close()
