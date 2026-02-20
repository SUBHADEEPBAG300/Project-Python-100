import socket
import threading

# Server setup
host = '127.0.0.1'   # localhost
port = 55555         # port number

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    """Send message to all connected clients."""
    for client in clients:
        client.send(message)

def handle_client(client):
    """Handle messages from a single client."""
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            # Remove client if disconnected
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('utf-8'))
            nicknames.remove(nickname)
            break

def receive():
    """Accept new client connections."""
    print("Server is running and listening...")
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of client is {nickname}")
        broadcast(f"{nickname} joined the chat!".encode('utf-8'))
        client.send("Connected to the server!".encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive()