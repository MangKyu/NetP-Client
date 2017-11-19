import threading
import re

class SignUpFrameHandler:
    client = None

    # Constructor for Sign Up Frame Handler instance
    def __init__(self, client):
        self.client = client

    # Send check ID Request to Server
    def chkID(self, id):
        if len(id) > 20:
            msg = 'Please Make your ID shorter than 20 characters'
        elif id == '':
            msg = 'Please Enter Your ID'
        else:
            chkDict = {'MSG': '/CKID', 'ID': id}
            self.client.sendMsg(chkDict)
            self.client.sem.acquire()
            if self.client.rcvThread.msg == 'ACK':
                self.client.rcvThread.msg == ''
                msg = '''ID Check Pass'''
                return True, msg
            else:
                msg = 'ID Already Exist'
        return False, msg

    # Send mail Request to Server
    def sendMail(self, mail):
        p = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

        if p.match(mail):
            mailDict = {'MSG': '/MAIL', 'MAIL': mail}
            self.client.sendMsg(mailDict)
            self.client.sem.acquire()
            if self.client.rcvThread.msg == 'ACK':
                code = self.client.generateCode()
                mailThread = threading.Thread(target=self.client.sendMail, args=(mail, code))
                mailThread.start()
                self.client.rcvThread.msg == ''
                print(code)
                return True, code
            else:
                msg = 'mail Already Exist'
        else:
            msg = 'Please Check your mail Format'
        return False, msg

    # Send Sign up Request to Server
    def signUp(self, name, id, pw, pw2, mail, code, IDBool, mailBool, frameName, frameMail, frameCode):
        if name != '':
            if IDBool and frameName == id:
                if pw == pw2 and pw != '':
                    if mailBool and frameMail == mail:
                        if code == frameCode:
                            signUpDict = {'MSG': '/SGUP', 'NAME': name, 'ID': id, 'PW': pw, 'MAIL': mail}
                            self.client.sendMsg(signUpDict)
                            self.client.sem.acquire()
                            if self.client.rcvThread.msg == 'ACK':
                                self.client.rcvThread.msg == ''
                                msg = 'Sign Up Success'
                                return True, msg
                            else:
                                msg = 'Sign Up Failed'
                        else:
                            msg = 'Wrong code'
                    else:
                        msg = 'Please send mail and right code'
                else:
                    msg = 'Check PW and PW2 '
            else:
                msg = 'Please Check your ID'
        else:
            msg = 'Please Enter your Name'
        return False, msg

    # return cancle Request
    def cancel(self):
        return True
