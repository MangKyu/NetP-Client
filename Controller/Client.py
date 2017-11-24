import socket
import smtplib
from Controller import RCVThread
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import random
import threading
from Controller import AEScipher

class Client:
    port = 8099
    host = "127.0.0.1"
    sock = None
    rcvThread = None
    sem = None
    eventHandler = None
    adminRoom = None
    aesCipher = None
    user = None

    # Constructor for client instance
    def __init__(self, user, eventHandler, adminRoom):
        self.user = user
        self.aesCipher = AEScipher.AEScipher()
        self.adminRoom = adminRoom
        self.eventHandler = eventHandler
        self.sem = threading.Semaphore(0)
        self.connect()

    # connect with server and create Receiver Thread
    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        msg = self.sock.recv(1024)
        msg = msg.decode("utf-8", "ignore")
        self.port = int(msg)
        self.sock.close()

        # reconnect with another port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        self.rcvThread = RCVThread.RCVThread(self, self.sock, self.user)
        self.rcvThread.start()

    # send message
    def sendMsg(self, msg):
        print('Client Send: '+str(msg))
        aesMsg = self.aesCipher.encrypt(msg)
        if msg == "exit":
            self.sock.close()
        self.sock.send(aesMsg)

    # send Mail for Sign Up
    def generateCode(self):
        code = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(
            random.randint(0, 9))
        return code

    # send mail for Authorization
    def sendMail(self, rcvAddr, code):
        sender = 'whalsrb1226@gmail.com'
        receiver = rcvAddr
        msgRoot = MIMEMultipart('related')
        msgRoot['From'] = sender
        msgRoot['To'] = receiver
        msgRoot['Subject'] = 'Authorization email from Python Program'

        msgAlt = MIMEMultipart('alternative')
        msgRoot.attach(msgAlt)

        mail_msg = """
        <p>[   Make Account for Python Program   ]</p>
        <p><a href="https://www.facebook.com/profile.php?id=100007184050577">Sender's Facebook Link </a></p>
        <p> Please enter the code to the Program!!</p>
        <p><img src="cid:logoImage"></p>
        """
        mail_msg += "\n Authorization Code = "
        mail_msg += code
        msgAlt.attach(MIMEText(mail_msg, 'html', 'utf-8'))

        fp = open("../View/logo.png", 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()

        msgImage.add_header('Content-ID', '<logoImage>')
        msgRoot.attach(msgImage)

        try:
            smtp = smtplib.SMTP('smtp.gmail.com', 587)
            smtp.ehlo()  # say hello for protocol
            smtp.starttls()  # need to start TLS Encryption, not for SSL

            smtp.login(sender, 'enendekekd12')
            smtp.sendmail(sender, receiver, msgRoot.as_string())
            smtp.quit()
        except smtplib.SMTPException:
            print("Error : Send mail")

    # Send Image to server
    def sendImg(self, imgPath):
        with open(imgPath, 'rb') as f:
            img = f.read()
            self.sock.send(img)
            self.sock.send(bytes('`', 'utf-8'))
            f.close()

    # Receive Image from server
    def recvImg(self, imgPath, ext):
        if ext != None:
            imgPath = imgPath + '.'+ext
        with open(imgPath, 'wb') as f:
            while True:
                buf = self.sock.recv(4096)
                if str(buf[len(buf)-1]) == '96':
                    buf = bytearray(buf)
                    buf.pop(len(buf)-1)
                    buf = bytes(buf)
                    f.write(buf)
                    f.close()
                    return imgPath
                f.write(buf)

    # Exit
    def exit(self):
        self.rcvThread.exit()