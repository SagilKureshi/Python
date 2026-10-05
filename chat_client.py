import socket

host = 'localhost'
port = 65535

s = socket.socket()
s.connect((host, port))

# Changed variable name from 'str' to 'msg' to avoid overwriting Python built-ins
msg = input("Enter data : ")

while msg != 'exit':
    s.send(msg.encode())
    
    data = s.recv(1024)
    data = data.decode()
    
    # INDENTED: These must be inside the loop to run on every turn
    print("from server :" + data)
    msg = input("Enter data : ")

s.close()
