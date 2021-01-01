from socket import *
import base64
import ssl
subject = "Subject: Oh my god!\r\n"
contenttype = "text/plain"
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
version = "MIME-Version: 1.0\r\n"
msgtype = "Content-Type:multipart/mixed;boundary='BOUNDARY'\r\n\r\n"
msgboudary = b"--BOUNDARY\r\n"
# Choose a mail server (e.g. Google mail server)
# and call it mailserver
mailserver = ('smtp.qq.com', 465)
imgname = 'img.jpg'
msgfileType = b"Content-type:image/gif;\r\n"
msgfilename = b"Content-Disposition: inline; filename= '%s'\r\n"%imgname.encode()
msgfileId = b'Content-ID:<imgid1>\r\n'

# Sender and reciever
# Fill in start
receiver_email = 'wangyicbx@163.com'
sender_email = '836241487@qq.com'
# Fill in end

# Auth information (Encode with base64)
# Fill in start
userName = base64.b64encode('836241487@qq.com'.encode()).decode()
password = base64.b64encode('zawyptnbvqwrbeii'.encode()).decode()
# Fill in end

# Create socket called clientSocket
# and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket = ssl.wrap_socket(clientSocket, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_SSLv23)
clientSocket.connect(mailserver)
#Fill in end

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO QQ\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')


# Auth
# Send MAIL FROM command and print server response.
# Fill in start
auth_command = 'AUTH login\r\n'
clientSocket.send(auth_command.encode())
recv2 = clientSocket.recv(1024).decode()
print('2: '+recv2)

user_command = userName + '\r\n'
clientSocket.send(user_command.encode())
recv3 = clientSocket.recv(1024).decode()
print('3: '+recv3)

password_command = password + '\r\n'
clientSocket.send(password_command.encode())
recv4 = clientSocket.recv(1024).decode()
print('4: '+recv4)
# Fill in end


# Send RCPT TO command and print server response.
# Fill in start
from_command = 'MAIL FROM:<' + sender_email + '>\r\n'
clientSocket.send(from_command.encode())
recv5 = clientSocket.recv(1024).decode()
print('5: '+recv5)

to_command = 'RCPT TO:<' + receiver_email + '>\r\n'
clientSocket.send(to_command.encode())
recv6 = clientSocket.recv(1024).decode()
print('6: '+recv6)
# Fill in end


# Send DATA command and print server response.
# Fill in start
data_command = 'DATA\r\n'
clientSocket.send(data_command.encode())
recv7 = clientSocket.recv(1024).decode()
print('7: '+recv7)
# Fill in end


# Send message data.
# Fill in start
clientSocket.send(subject.encode())
clientSocket.send(version.encode())
clientSocket.send(msgtype.encode())

# 邮件内容
clientSocket.send(b'\r\n\r\n'+msgboudary)
clientSocket.send(b'Content-Type:text/html;\r\n')
clientSocket.send(b'Content-Transfer-Encoding:7bit\r\n\r\n')
clientSocket.send(bytes(msg.encode()))
clientSocket.send(b'<img src="cid:imgid1">')

clientSocket.send(b'\r\n\r\n'+msgboudary)
clientSocket.send(msgfileType)
clientSocket.send(msgfileId)
clientSocket.send(msgfilename)
clientSocket.send(b'Content-Transfer-Encoding:base64\r\n\r\n')
img = open("./brawler.jpg", 'rb')
while True:
    filedata = img.read(1024)
    if not filedata:
        break
    clientSocket.send(base64.b64encode(filedata))
img.close()

# Fill in end


# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode())
recv8 = clientSocket.recv(1024).decode()
print('8: '+recv8)
# Fill in end


# Send QUIT command and get server response.
# Fill in start
quit_command = 'QUIT\r\n'
clientSocket.send(quit_command.encode())
recv9 = clientSocket.recv(1024).decode()
print('9: '+recv9)
# Fill in end


# Close connection
# Fill in start
clientSocket.close()
# Fill in end
