try:
    from Tkinter import *
except ImportError:
    from tkinter import *
import datetime
from Controller import Clock
class RoomFrameHandler:
    client = None
    roomFrame = None
    clock = None

    # Constructor for Room Frame Handler instance
    def __init__(self, client, roomFrame):
        self.client = client
        self.roomFrame = roomFrame
        self.clock = Clock.Clock(roomFrame)
        self.clock.start()

    # Set image
    def setImg(self, path, watch):
        self.roomFrame.roomFrame.imgPath = path
        self.roomFrame.setImage(watch)

    # Send Buy Request to Server
    def buy(self, myPrice, price, endTime, roomIdx):
        if myPrice <= price:
            msg = 'Too Lower Price'
        elif myPrice > 100000:
            msg = 'Too high Price'
        else:
            now = datetime.datetime.now()
            endTime = datetime.datetime.strptime(endTime, '%Y-%m-%d %H:%M:%S')
            if now < endTime:
                sendDict = {'MSG': '/ACRQ', 'PRICE': myPrice, 'RIDX': roomIdx}
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
            self.roomFrame.roomFrame.price.configure(text=price)

    def sendWatch(self, roomIdx, watch):
        sendDict = {'MSG': '/CHWC', 'WATCH': watch, 'RIDX': roomIdx}
        self.client.sendMsg(sendDict)
        self.client.sem.acquire()
        if self.client.rcvThread.msg == 'ACK':
            msg = '''Auction Request Complete'''
            return True, msg
        else:
            msg = '''Auction Request Failed'''
            return False, msg
