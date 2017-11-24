class SellingFrameHandler:
    client = None

    # Constructor for Selling Frame Handler instance
    def __init__(self, client):
        self.client = client

    # Send sell Request to Server
    def sell(self, item):

        if len(item.itemName) > 15:
            msg = 'itemName is too long'
        elif item.itemName == '':
            msg = 'No ItemName'
        elif len(item.itemDesc) > 150:
            msg = 'desc is too long'
        elif item.price < 0:
            msg = 'Price cannot be under 0'
        elif item.price >= 100000:
            msg = 'Price cannot be higher than 100000'
        elif item.itemDesc.__contains__('씨발') or item.itemDesc.__contains__('새끼') or item.itemDesc.__contains__('꺼져'):
            msg = 'Do not contain cuss word'
        elif len(item.itemDesc) > 150:
            msg = 'desc is too long'
        else:
            str = item.imgPath.split('.')
            sellDict = {'MSG': '/SLIT', 'ITNAME': item.itemName, 'SELLER': item.seller,
                        'PRICE': item.price, 'ITDESC': item.itemDesc, 'ITPATH': str[1]}
            self.client.sendMsg(sellDict)
            self.client.sendImg(item.imgPath)
            self.client.sem.acquire()
            if self.client.rcvThread.msg == 'ACK':
                msg = '''Sell Item Complete'''
                return True, msg
            else:
                msg = '''Sell Item Failed'''
        return False, msg
