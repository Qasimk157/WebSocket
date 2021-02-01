import socket

ip='127.0.0.1'
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, 1028))
# s.bind((socket.gethostname(),1028))
# print(socket.gethostname())
s.listen(1)

con,addr=s.accept()
print("connected with", addr)
while True:
    messg = input("send message to client: ")
    con.send(messg.encode())
    print("waiting for responce")
    c_messg=con.recv(1024)
    data1=c_messg.decode()
    print("message from client: ", c_messg.decode())
