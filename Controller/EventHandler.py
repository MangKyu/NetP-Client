from Controller.FrameHandler import LoginFrameHandler, SignUpFrameHandler, \
    MainFrameHandler, SettingFrameHandler, SellingFrameHandler, RoomFrameHandler

# the class which has each frame handler
class EventHandler:
    frameList = None
    client = None
    loginHandler = None
    signUpHandler = None
    mainHandler = None
    settingHandler = None
    sellingHandler = None
    roomHandler = None

    # Constructor for EventHandler instance
    def __init__(self, client, frameList):
        self.client = client
        self.frameList = frameList
        self.loginHandler = LoginFrameHandler.LoginFrameHandler(client)
        self.signUpHandler = SignUpFrameHandler.SignUpFrameHandler(client)
        self.mainHandler = MainFrameHandler.MainFrameHandler(client, frameList['main'])
        self.settingHandler = SettingFrameHandler.SettingFrameHandler(client)
        self.sellingHandler = SellingFrameHandler.SellingFrameHandler(client)
        self.roomHandler = RoomFrameHandler.RoomFrameHandler(client, frameList['room'])

    # Change frame and update user's data
    def changeFrame(self, frame):
        if self.frameList['login'].loginFrame != frame or self.frameList['sign'] != frame:
            self.frameList['main'].refreshData()
            self.frameList['room'].refreshData()
            self.frameList['setting'].refreshData()
            self.frameList['selling'].refreshData()
        frame.tkraise()

