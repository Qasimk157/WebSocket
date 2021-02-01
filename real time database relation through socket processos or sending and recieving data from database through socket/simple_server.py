import socket
import mysql.connector
ip='127.0.0.1'
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, 1028))
# print(socket.gethostname())
s.listen(1)
mydatabase = mysql.connector.connect(
    host = '127.0.0.1', user = 'root',
    passwd = 'Qasim@304', database = 'testdb')


mycursor = mydatabase.cursor()
mycursor.execute("Select * From testdb.book")
myresult = mycursor.fetchall()
myres=str(myresult)
# while True:
#     clt, adr=s.accept()
#     print(f"conection to {adr} established")
#     clt.send(bytes(myres, 'utf-8'))
con,addr=s.accept()
print("connected with", addr)
while True:
    # messg = input("send message to client: ")
    con.send(myres.encode())
    print("waiting for responce")
    c_messg=con.recv(1024)
    data1=c_messg.decode()
    s = "INSERT INTO book(bookid,title,price) VALUES(%s,%s,%s)"
    b1 = (9, data1, 562)
    mycursor.execute(s, b1)
    mydatabase.commit()
    mycursor.execute("Select * From testdb.book")
    myresult1 = mycursor.fetchall()
    print(myresult1)

    #save
    #datafetch
    # con.send(messg.encode())
    print("message from client: ", c_messg.decode())