import socket

HOST = '127.0.0.1'  # Server's hostname
PORT = 9292 # Server's port being listened on

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

with sock as s:
    # Connect client to server
    s.connect((HOST, PORT))

    # Send byte string message to server
    s.sendall(b'Hello, world!')

    data = s.recv(1024)  # Listen for response from server

print('Received', repr(data))

