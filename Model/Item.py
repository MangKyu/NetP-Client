class Item:
    seller = None
    itemName = None
    price = None
    itemDesc = None
    imgPath = None

    # Constructor for Item instance
    def __init__(self, seller, itemName, price=0, itemDesc=None, imgPath=None):
        self.seller = seller
        self.itemName = itemName
        self.price = price
        self.itemDesc = itemDesc
        self.imgPath = imgPath

    # Set Item data
    def setItem(self, price, itemDesc, imgPath):
        self.price = price
        self.itemDesc = itemDesc
        self.imgPath = imgPath
