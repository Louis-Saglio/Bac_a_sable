import socket

hote = ""
port = 12800

serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur_socket.bind((hote, port))
serveur_socket.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))

socket_client, infos_connexion = serveur_socket.accept()

msg_recu = b""
while msg_recu != b"fin":
    msg_recu = socket_client.recv(1024)
    # L'instruction ci-dessous peut lever une exception si le message
    # Réceptionné comporte des accents
    print(msg_recu.decode())
    socket_client.send(b"5 / 5")

print("Fermeture de la connexion")
socket_client.close()
serveur_socket.close()
