from socket import *
import base64
import ssl

# Mail content
subject = "I love computer networks!"
contenttype = "text/plain"
msg = "I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver =  'smtp.qq.com'

# Sender and reciever
fromaddress = '2878079058@qq.com'
toaddress =  '2021040906013@std.uestc.edu.cn'

send_msg = 'FROM:' + fromaddress + '\r\n'
send_msg += 'TO:' + toaddress + '\r\n'
send_msg += 'Subject:' + subject + '\r\n'
send_msg +=  '\r\n '+ msg
send_msg = send_msg.encode()

# Auth information (Encode with base64)
username = base64.b64encode('2878079058'.encode())
password =base64.b64encode('behtgbnnjqvodheb'.encode())

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET,SOCK_STREAM)
serverport = 25
clientSocket.connect((mailserver, serverport))

recv = clientSocket.recv(1024).decode()
print(recv)

# Send HELO command and print server response.
heloCommand = 'HELO mailserver\r\n'
while True:
    clientSocket.send(heloCommand.encode())
    recv = clientSocket.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '250':
        break


# Send AUTH LOGIN command and print server response.
clientSocket.sendall('AUTH LOGIN\r\n'.encode())
recv = clientSocket.recv(1024).decode()
print(recv)

clientSocket.sendall((username +b'\r\n'))
recv = clientSocket.recv(1024).decode()
print(recv)

clientSocket.sendall((password + b'\r\n'))
recv = clientSocket.recv(1024).decode()
print(recv)

# Send MAIL FROM command and print server response.
mail_from = 'MAIL FROM:<2878079058@qq.com>\r\n'
while True:
    clientSocket.send(mail_from.encode())
    recv = clientSocket.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '250':
        break

# Send RCPT TO command and print server response.
rcpt_to = 'RCPT TO:<2021040906013@std.uestc.edu.cn>\r\n'
while True:
    clientSocket.send(rcpt_to.encode())
    recv = clientSocket.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '250':
        break

# Send DATA command and print server response.
data = 'DATA\r\n'
while True:
    clientSocket.send(data.encode())
    recv = clientSocket.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '354':
        break
# Send message data.
clientSocket.send(send_msg)

# Message ends with a single period and print server response.
while True:
    clientSocket.send(endmsg.encode())
    recv = clientSocket.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '250':
        break

# Send QUIT command and print server response.
QUITCommand = 'QUIT\r\n'
while True:
    clientSocket.send(QUITCommand.encode())
    recv = clientSocket.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '221':
        break

# Close connection
clientSocket.close()
