try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import datetime
class RoomFrameHandler:
    client = None
    roomFrame = None

    # Constructor for Room Frame Handler instance
    def __init__(self, client, roomFrame):
        self.client = client
        self.roomFrame = roomFrame

    # Set image
    def setImg(self, path):
        self.roomFrame.roomFrame.itemFrame.imgPath = path
        self.roomFrame.setImage()

    # Send Buy Request to Server
    def buy(self, myPrice, price, endTime, roomIdx):
        if myPrice <= price:
            msg = 'Too Lower Price'
        else:
            now = datetime.datetime.now()
            endTime = datetime.datetime.strptime(endTime, '%Y-%m-%d %H:%M:%S')
            if now < endTime:
                sendDict = {'MSG': '/ACRQ', 'PRICE': myPrice, 'BUYER': self.client.adminRoom.user.id, 'RIDX': roomIdx}
                self.client.sendMsg(sendDict)
                self.client.sem.acquire()
                if self.client.rcvThread.msg == 'ACK':
                    msg = '''Auction Request Complete'''
                    return True, msg
                else:
                    msg = '''Auction Request Failed'''
            else:
                msg = 'Auction was Already Finished'
                return False, msg
        return False, msg

    # update room in the room list
    def updateData(self, roomIdx, price):
        self.client.adminRoom.updateRoom(roomIdx, price)
        if self.client.adminRoom.room.roomIdx == roomIdx:
            self.roomFrame.roomFrame.itemFrame.price.configure(text=price)