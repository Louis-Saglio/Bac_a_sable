import threading
import socket
import sys
import time


class Listener(threading.Thread):
    def __init__(self, listener_socket: socket.socket):
        super().__init__()
        self.listener_socket = listener_socket

    def run(self):
        while True:
            message = self.listener_socket.recv(1024).decode()
            if message.lower() == "fin":
                break
            else:
                sys.stdout.write(message + "\n")


class Speaker(threading.Thread):
    def __init__(self, speaker_socket: socket.socket):
        super().__init__()
        self.speaker_socket = speaker_socket

    def run(self):
        while True:
            message = input().encode()
            self.speaker_socket.send(message)
            time.sleep(3)
            if message.decode().lower == "fin":
                break
