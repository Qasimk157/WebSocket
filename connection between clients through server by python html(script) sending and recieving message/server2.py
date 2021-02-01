import socket
import time
import pickle



HEADERSIZE = 10


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1236))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"connection from {address} has been established!")

    d = {1: "Hey", 2: "there"}
    msg = pickle.dumps(d)

    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg

    clientsocket.send(msg)
#     while True:
#         time.sleep(1)
#         msg = f"The time is! {time.time()}"
#         msg = f'{len(msg):<{HEADERSIZE}}' + msg
#         clientsocket.send(bytes(msg, "utf-8"))
