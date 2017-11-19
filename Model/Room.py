from Model import Item

class Room:
    roomIdx = 0
    seller = None
    endTime = None
    item = None

    # Constructor for Room instance
    def __init__(self, roomIdx, seller, itemName):
        self.item = Item.Item(seller, itemName)
        self.roomIdx = roomIdx
        self.seller = seller
