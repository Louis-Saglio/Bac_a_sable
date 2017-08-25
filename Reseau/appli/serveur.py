import select
from listener import *


# Création du serveur
serveur = socket.socket()
serveur.bind(('', 8888))
serveur.listen(5)

# Connexion du client
socket_to_client, addresse_client = serveur.accept()
print(addresse_client)

listener = Listener(socket_to_client)
speaker = Speaker(socket_to_client)

listener.start()
speaker.start()

listener.join()
speaker.join()

socket_to_client.close()
serveur.close()
