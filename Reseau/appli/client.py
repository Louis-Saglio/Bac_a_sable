from listener import *


client = socket.socket()
client.connect(("", 8888))

listener = Listener(client)
speaker = Speaker(client)

listener.start()
speaker.start()

listener.join()
speaker.join()

client.close()
