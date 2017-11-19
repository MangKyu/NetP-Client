import threading
from tkinter.messagebox import showinfo

# Thread to receive signal from server
class RCVThread(threading.Thread):
    connFlag = True
    msg = None
    user = None
    sock = None
    client = None

    # Constructor for RCVThread instance
    def __init__(self, client, sock, user):
        threading.Thread.__init__(self)
        self.client = client
        self.connFlag = True
        self.sock = sock
        self.user = user

    def run(self):
        #try:
            while self.connFlag:
                msg = self.sock.recv(4096)
                msgDict = self.client.aesCipher.decrypt(msg)
                msgProtocol = msgDict['MSG']
                print('RECIEVED'+str(msgDict))

                if msgProtocol == "/EXIT":
                    print("/EXIT- RCVThread")
                    break

                if msgProtocol == '/LGIN' or msgProtocol == '/SGUP':
                    if msgDict['RPLY'] == 'ACK':
                        self.msg = 'ACK'
                        self.user.setUser(msgDict['NAME'], msgDict['ID'], msgDict['MONEY'])
                    else:
                        self.msg = 'REJ'
                    self.client.sem.release()

                elif msgProtocol == '/CKID' or msgProtocol == '/MAIL' or msgProtocol == '/SLIT' or msgProtocol == '/CHPW':
                    if msgDict['RPLY'] == 'ACK':
                        self.msg = 'ACK'
                    else:
                        self.msg = 'REJ'
                    self.client.sem.release()

                elif msgProtocol == '/CHMN':
                    if msgDict['RPLY'] == 'ACK':
                        self.user.money = msgDict['MONEY']
                        self.msg = 'ACK'
                    else:
                        self.msg = 'REJ'
                    self.client.sem.release()

                elif msgProtocol == '/RLST':
                    self.client.adminRoom.setRoomLst(msgDict['ROOMS'])
                    self.client.eventHandler.mainHandler.addRoom(msgDict['ROOMS'])

                elif msgProtocol == '/RINF':
                    ext = msgDict['ITPATH'].split('.')[1]
                    imgPath = self.client.recvImg('test', ext)
                    if msgDict['RPLY'] == 'ACK':
                        self.msg = 'ACK'
                        self.client.adminRoom.setRoom(msgDict, imgPath)
                    else:
                        self.msg = 'REJ'
                    self.client.sem.release()

                elif msgProtocol == '/ACRQ':
                    if msgDict['RPLY'] == 'ACK':
                        self.msg = 'ACK'
                    else:
                        self.msg = 'REJ'
                    self.client.sem.release()

                elif msgProtocol == '/RERQ':
                    self.client.eventHandler.roomHandler.updateData(msgDict['RIDX'], msgDict['PRICE'])

                elif msgProtocol == '/ALRM':
                    if msgDict['RPLY'] == 'ACK':
                        self.user.money = msgDict['MONEY']
                        showinfo('Auction', msgDict['CNT'])

                elif msgProtocol == '/ACLT':
                    if len(msgDict['ROOMS']) == 0:
                        self.msg = 'REJ'
                    else:
                        self.msg = 'ACK'
                    self.client.sem.release()
                    self.client.adminRoom.setRoomLst(msgDict['ROOMS'])
                    self.client.eventHandler.mainHandler.addRoom(msgDict['ROOMS'])


        #except:
#            self.exit()

    # exit the thread
    def exit(self):
        self.sock.close()
        self.connFlag = False