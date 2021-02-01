import socket
ip='127.0.0.1'
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, 1028))
while True:
    print("waiting for responce")
    s_messg=s.recv(1024)
    print("message from server: ",s_messg.decode())
    c_messg=input("send message to server: ")
    s.send(c_messg.encode())