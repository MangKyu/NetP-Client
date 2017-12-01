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
        try:
            while self.connFlag:
                msg = self.sock.recv(4096)
                msgDict = self.client.aesCipher.decrypt(msg)
                msgProtocol = msgDict['MSG']
                print('RECIEVED'+str(msgDict))

                if msgProtocol == "/EXIT":
                    print("/EXIT- RCVThread")
                    break

                if msgProtocol == '/LGIN':
                    if msgDict['RPLY'] == 'ACK':
                        self.msg = 'ACK'
                        self.user.setUser(msgDict['NAME'], msgDict['ID'], msgDict['MONEY'])
                    else:
                        self.msg = 'REJ'
                    self.client.sem.release()

                elif msgProtocol == '/CKID' or msgProtocol == '/MAIL' or msgProtocol == '/SLIT' or \
                                msgProtocol == '/CHPW'or msgProtocol == '/SGUP':
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
                    imgPath = self.client.recvImg('../View/Pictures/item/test', ext)
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
                        self.user.money = self.user.money - msgDict['MONEY']
                        self.client.eventHandler.changeFrame(self.client.eventHandler.frameList['room'].roomFrame)
                        showinfo('Auction', msgDict['CNT'])
                    elif msgDict['RPLY'] == 'REJ':
                        showinfo('Auction', msgDict['CNT'])
                    elif msgDict['RPLY'] == 'NON':
                        self.user.money = self.user.money + msgDict['MONEY']
                        print('BABABABAB')
                        self.client.eventHandler.changeFrame(self.client.eventHandler.frameList['main'].mainFrame)
                        print('CAVABABAB')
                        self.client.eventHandler.frameList['main'].goThatRoom(msgDict['RIDX'])
                elif msgProtocol == '/ACLT':
                    if len(msgDict['ROOMS']) == 0:
                        self.msg = 'REJ'
                    else:
                        self.msg = 'ACK'
                    self.client.sem.release()
                    self.client.adminRoom.setRoomLst(msgDict['ROOMS'])
                    self.client.eventHandler.mainHandler.addRoom(msgDict['ROOMS'])

                elif msgProtocol == '/WCLT':
                    if msgDict['RPLY'] == 'ACK':
                        roomList = msgDict['ROOMS']
                        self.client.adminRoom.setWatchlist(roomList)
                        for i in range(len(roomList)):
                            self.client.recvImg(self.client.adminRoom.watchList[i].imgPath, None)
                        self.msg = 'ACK'
                    elif msgDict['RPLY'] == 'REJ':
                        self.msg = 'REJ'
                    self.client.sem.release()
        except:
            print('RCVThread Exit')
            self.exit()

    # exit the thread
    def exit(self):
        try:
            self.sock.close()
            if self.client.eventHandler.roomHandler.clock.sFlag:
                self.client.eventHandler.roomHandler.clock.sem.release()
            self.client.eventHandler.roomHandler.clock.tFlag = False
            self.connFlag = False
        except:
            pass