"""Simple TCP server."""
# pylint: disable-msg=C0103
import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9990
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)
print("Listening on {} {}".format(bind_ip, bind_port))


def handle_client(client_socket):
    """Client handling thread."""

    # Print out a message from client.
    request = client_socket.recv(1024)
    print("Received: {}".format(request.decode('utf-8')))

    # Send back a message to client.
    client.send("Test back!".encode('utf-8'))
    client_socket.close()


while True:
    client, addr = server.accept()
    print("Accepted connection from: {}:{}".format(addr[0], addr[1]))

    # Create thread to handle incoming message.
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
