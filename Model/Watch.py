class Watch:
    itemName = None
    imgPath = None
    price = 0
    roomIdx = 0

    def __init__(self, itemName, imgPath, price, roomIdx):
        self.itemName = itemName
        self.imgPath = '../View/Pictures/item/'+imgPath
        self.price = price
        self.roomIdx = roomIdx
