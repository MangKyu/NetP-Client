class LoginFrameHandler:
    client = None

    # Constructor for Login Frame Handler instance
    def __init__(self, client):
        self.client = client

    # Send Login Request to Server
    def login(self, id, pw):
        if id != '' and pw != '':
            loginDict = {'MSG': '/LGIN', 'ID': id, 'PW': pw}
            self.client.sendMsg(loginDict)
            self.client.sem.acquire()
            if self.client.rcvThread.msg == 'ACK':
                self.client.rcvThread.msg == ''
                msg = 'Success'
                return True, msg
            else:
                msg = 'Login Failed'

        elif id == '':
            msg = 'Please Enter your ID'

        elif pw == '':
            msg = 'Please Enter your PW'
        return False, msg
