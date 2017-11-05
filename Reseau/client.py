import socket

client = socket.socket()
client.connect(('127.0.0.1', 8888))


while True:
    message = input(">").encode()
    client.send(message)
    if message == b"fin":
        break

client.close()
