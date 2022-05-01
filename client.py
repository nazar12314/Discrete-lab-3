import socket
import threading
import rsa
from hashlib import sha384

class Client:
    def __init__(self, server_ip: str, port: int, username: str) -> None:
        self.server_ip = server_ip
        self.port = port
        self.username = username
        self.public = None
        self.private = None
        self.server_keys = None

    def init_connection(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.connect((self.server_ip, self.port))
        except Exception as e:
            print("[client]: could not connect to server: ", e)
            return

        self.s.send(self.username.encode())

        self.public, self.private = rsa.generate_public_and_private_keys()

        # exchange public keys
        keys = self.s.recv(1024).decode()  # get public server keys
        self.server_keys = (int(key) for key in keys.split(","))

        # send encoded clients' keys. Looks like: (e, n, d)
        secret = rsa.encode(self.server_keys, ",".join(str(key) for key in self.public+self.private[:1]))
        self.s.send(secret.encode())

        message_handler = threading.Thread(target=self.read_handler,args=())
        message_handler.start()
        input_handler = threading.Thread(target=self.write_handler,args=())
        input_handler.start()

    def read_handler(self):
        while True:
            msg_hash, message = self.s.recv(1024).decode().split("|")
            decoded = rsa.decode(self.private, message)
            if msg_hash == sha384(decoded.encode()).hexdigest():
                print(decoded)
            else:
                print("Message integrity error!")

    def write_handler(self):
        while True:
            message = input()
            encoded = sha384(message.encode()).hexdigest()+"|"+rsa.encode(self.public, message)
            self.s.send(encoded.encode())

if __name__ == "__main__":
    cl = Client("127.0.0.1", 9001, "b_g")
    cl.init_connection()
