"""Simple TCP client."""
# pylint: disable-msg=C0103
import socket

target_host = "127.0.0.1"
target_port = 9990

# Create a socket object.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client.
client.connect((target_host, target_port))

# Send message.
message = "Test"
client.send(message.encode('utf-8'))

# Receive message.
response = client.recv(4096)
print("Received: {}".format(response.decode('utf-8')))
