class WatchlistFrameHandler:
    client = None
    watchlistFrame = None

    def __init__(self, client, watchlistFrame):
        self.client = client
        self.watchlistFrame = watchlistFrame

    def setWatchlist(self):
        self.destroyList()
        watchlist = self.client.adminRoom.watchList
        self.watchlistFrame.createCanvas()
        for i in range(len(watchlist)):
            self.watchlistFrame.createItem('['+str(watchlist[i].roomIdx)+']'+watchlist[i].itemName, watchlist[i].imgPath, watchlist[i].price)

    def destroyList(self):
        for i in range(len(self.watchlistFrame.imgList)):
            self.watchlistFrame.imgList[i].destroy()
            self.watchlistFrame.labelList[i].destroy()

        self.watchlistFrame.imgList = []
        self.watchlistFrame.labelList = []