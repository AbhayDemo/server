import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port
host = '127.0.0.1'  # This allows the server to be accessible from any IP address
port = 65530  # You can choose any port

# Bind the socket to the host and port
server_socket.bind((host, port))

# Start listening for incoming connections
server_socket.listen(5)
print(f"Server listening on port {port}...")

while True:
    # Accept a connection from a client
    
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    # Receive the message from the client
    message = client_socket.recv(1024).decode('utf-8')
    print(f"Received message: {message}")

    # If the client sends 'ping', respond with 'pong'
    if message == "ping":
        response = "pong"
        client_socket.send(response.encode('utf-8'))
        print(f"Sent response: {response}")

    # Close the client connection
    client_socket.close()
