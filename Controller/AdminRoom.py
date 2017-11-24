from Model import Room, Watch

class AdminRoom:
    roomList = None
    room = None
    user = None
    watchList = None

    def __init__(self, user):
        self.user = user
        self.roomList = {}
        self.room = Room.Room(-1, 'None', 'None')
        self.watchList = []
    # Set Room List
    def setRoomLst(self, roomList):
        self.roomList = {-1: self.room}

        for i in range(len(roomList)):
            # roomList[i][0] = roomIdx, roomList[i][1] = seller, roomList[i][2] = itemName
            room = Room.Room(roomList[i][0], roomList[i][1], roomList[i][2])
            self.roomList[room.roomIdx] = room

    # Set Room variable
    def setRoom(self, roomDict, imgPath):
        self.room = self.roomList[roomDict['RIDX']]
        self.room.endTime = roomDict['ENDT']
        self.room.item.setItem(roomDict['PRICE'], roomDict['ITDESC'], imgPath)
        self.room.watch = roomDict['WATCH']

    # Update Room data in Room List
    def updateRoom(self, roomIdx, price):
        self.roomList[roomIdx].item.price = price

    def setWatchlist(self, watchList):
        # watchList[i][0] = itemName, watchList[i][1] = imgPath, watchList[i][2] = price, watchList[i][3]= roomIdx
        self.watchList = []
        for i in range(len(watchList)):
            self.watchList.append(Watch.Watch(watchList[i][0], watchList[i][1], watchList[i][2], watchList[i][3]))
