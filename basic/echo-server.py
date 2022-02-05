import socket

HOST = '127.0.0.1'
PORT = 9292

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create TCP protocol socket, with IPv4 HOST address (AF_INET)

with sock as s:
    # Bind this socket to a particular host IP and port
    s.bind((HOST, PORT))

    # Listen for incoming connections
    print(f"Listening on {HOST}:{PORT}")
    s.listen()

    # Accept incoming connections
    conn, addr = sock.accept()

    while True:
        data = conn.recv(1024)
        print(data)
        if not data:
            break
        conn.sendall(data)