import socket
import select

# Création du serveur
serveur = socket.socket()
serveur.bind(('', 8888))
serveur.listen(5)

# Connexion du client
socket_to_client, addresse_client = serveur.accept()
print(addresse_client)

# Communication avec le client
while True:
    # Lire le message
    message = socket_to_client.recv(1024)
    # Action
    if message == b"fin":
        break
    if message == b"toi":
        message = socket_to_client.send(input('>').encode())
        # if message == b"fin":
        #     break
    else:
        print(message.decode())

socket_to_client.close()
serveur.close()
