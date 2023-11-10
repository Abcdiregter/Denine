import socket
import os
import threads
import subprocess

sv = "127.0.0.1"
port = 28
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)

