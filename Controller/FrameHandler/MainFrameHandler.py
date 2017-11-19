try:
    import Tkinter as tk
    import tkFont
    import ttk
except ImportError:  # Python 3
    import tkinter as tk
    import tkinter.font as tkFont
    import tkinter.ttk as ttk

class MainFrameHandler:
    client = None
    mainFrame = None

    # Constructor for Main Frame Handler instance
    def __init__(self, client, mainFrame):
        self.client = client
        self.mainFrame = mainFrame

    # add room list to roomFrame
    def addRoom(self, roomList):
        self.mainFrame.mainFrame.roomFrame.addRoom(roomList)

    # Send room data Request to Server
    def goRoom(self, roomIdx):
        roomDict = {'MSG': '/RINF', 'RIDX': roomIdx}
        self.client.sendMsg(roomDict)
        self.client.sem.acquire()
        if self.client.rcvThread.msg == 'ACK':
            self.client.rcvThread.msg == ''
            msg = 'go to room Success'
            return True, msg
        else:
            msg = 'Go to room Failed'
            return False, msg

    # Send Room List Request to Server
    def reqList(self):
        rDict = {'MSG': '/RRRR'}
        self.client.sendMsg(rDict)