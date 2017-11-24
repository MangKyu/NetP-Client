try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from View.PreferenceFrame import ChargeFrame, ChangePWFrame


class SettingFrame:
    mainView = None
    settingFrame = None
    path = None

    # Create Frame for setting Frame
    def __init__(self, mainView, root):
        self.root = root
        self.mainView = mainView
        self.path = "../View/Pictures/SettingFrame/"

        settingFrame = Frame(root)
        settingFrame.place(relx=0.00, rely=0.00, relheight=1.00, relwidth=1.00)
        settingFrame.configure(relief=GROOVE)
        settingFrame.configure(width=265)

        settingFrame.bgLabel = Label(settingFrame)
        settingFrame.bgLabel.place(x=0, y=0, relwidth=1, relheight=1)
        settingFrame.bgImage = PhotoImage(file="../View/Pictures/SettingFrame/background.png")
        settingFrame.bgLabel.configure(image=settingFrame.bgImage)

        settingFrame.imageLabel = Label(settingFrame)
        settingFrame.imageLabel.place(relx=0.08, rely=0.15)
        settingFrame._img0 = PhotoImage(file="../View/Pictures/SettingFrame/logo.png")
        settingFrame.imageLabel.configure(image=settingFrame._img0, bg='#4f779e')
        settingFrame.imageLabel.bind('<Button-1>', self.clickLogo)

        settingFrame.name = Label(settingFrame)
        settingFrame.name.place(relx=0.5, rely=0.146, relheight=0.05, relwidth=0.3)
        settingFrame.name.configure(text=self.mainView.mc.user.name, bg='#4f779e', fg='white', font=('08서울남산체 M', 12))
        settingFrame.name.lift()

        settingFrame.money = Label(settingFrame)
        settingFrame.money.place(relx=0.5, rely=0.212,relheight=0.05, relwidth=0.3)
        settingFrame.money.configure(text=self.mainView.mc.user.money, bg='#4f779e', fg='white', font=('08서울남산체 M', 12))
        settingFrame.money.lift()

        # --- add widgets in frame ---\
        img = self.mainView.mc.openPhotoImage(self.path + "purple.png")
        panel = Label(settingFrame, image=img, bg='#6d2e9e')
        panel.image = img
        label = Label(settingFrame, font=('08서울남산체 M', 15))
        label.configure(text='''Change Password''', bg = "#1c4478", fg='white', font=('08서울남산체 M', 16))
        panel.place(relx=0.12, rely=0.33)
        label.place(relx=0.32, rely=0.33, relheight=0.07, relwidth=0.572)
        panel.bind('<Button-1>', self.changePW)

        img = self.mainView.mc.openPhotoImage(self.path + "yellow.png")
        panel = Label(settingFrame, image=img, bg='#fcbd00')
        panel.image = img
        label = Label(settingFrame, font=('08서울남산체 M', 15))
        label.configure(text='''Charge Money''', bg = "#1c4478", fg='white', font=('08서울남산체 M', 16))
        panel.place(relx=0.12, rely=0.43)
        label.place(relx=0.32, rely=0.43, relheigh=0.07, relwidth=0.572)
        panel.bind('<Button-1>', self.chargeMoney)

        img = self.mainView.mc.openPhotoImage(self.path + "purple.png")
        panel = Label(settingFrame, image=img, bg='#6d2e9e')
        panel.image = img
        label = Label(settingFrame, font=('08서울남산체 M', 15))
        label.configure(text='''Transaction List''', bg = "#1c4478", fg='white', font=('08서울남산체 M', 16))
        panel.place(relx=0.12, rely=0.53)
        label.place(relx=0.32, rely=0.53, relheigh=0.07, relwidth=0.572)
        panel.bind('<Button-1>', self.purchaseList)

        img = self.mainView.mc.openPhotoImage(self.path + "yellow.png")
        panel = Label(settingFrame, image=img, bg='#fcbd00')
        panel.image = img
        label = Label(settingFrame, font=('08서울남산체 M', 15))
        label.configure(text='''Auction List''', bg = "#1c4478", fg='white', font=('08서울남산체 M', 16))
        panel.place(relx=0.12, rely=0.63)
        label.place(relx=0.32, rely=0.63, relheigh=0.07, relwidth=0.572)
        panel.bind('<Button-1>', self.aucList)

        img = self.mainView.mc.openPhotoImage(self.path + "purple.png")
        panel = Label(settingFrame, image=img, bg='#fcbd00')
        panel.image = img
        label = Label(settingFrame, font=('08서울남산체 M', 15))
        label.configure(text='''Watch List''', bg = "#1c4478", fg='white', font=('08서울남산체 M', 16))
        panel.place(relx=0.12, rely=0.73)
        label.place(relx=0.32, rely=0.73, relheigh=0.07, relwidth=0.572)
        panel.bind('<Button-1>', self.watchList)

        self.mainView.settingFrame = settingFrame
        self.settingFrame = settingFrame

    # Refresh User's Data
    def refreshData(self):
        name, id, money = self.mainView.mc.user.getUser()
        self.settingFrame.name.configure(text=name)
        self.settingFrame.money.configure(text=money)

    # Go to the MainFrame
    def clickLogo(self, event):
        self.mainView.mc.eventHandler.changeFrame(self.mainView.frameList['main'].mainFrame)

    # Create the Change Password Frame
    def changePW(self, event):
        ChangePWFrame.ChangePWFrame(self.mainView)

    # Create the Charge Money Frame
    def chargeMoney(self, event):
        ChargeFrame.ChargeFrame(self.mainView)

    # request my current auction list
    def aucList(self, event):
        # Get the Message from Controller whether auction list request was succeeded
        aFlag, msg = self.mainView.mc.eventHandler.settingHandler.aucList(self.mainView.mc.user.id)
        if aFlag:
            self.mainView.mc.eventHandler.changeFrame(self.mainView.frameList['main'].mainFrame)
        else:
            self.mainView.mc.showMessage('No Auction list', msg)

    # request my purchased list
    def purchaseList(self, event):
        # Get the Message from Controller whether purchased list request was succeeded
        pFlag, msg = self.mainView.mc.eventHandler.settingHandler.purchaseList(self.mainView.mc.user.id)
        if pFlag:
            self.mainView.mc.eventHandler.changeFrame(self.mainView.frameList['main'].mainFrame)
        else:
            self.mainView.mc.showMessage('No purchase list', msg)

    def watchList(self, event):
        wFlag, msg = self.mainView.mc.eventHandler.settingHandler.watchList(self.mainView.mc.user.id)
        if wFlag:
            self.mainView.mc.eventHandler.changeFrame(self.mainView.frameList['watch'].watchlistFrame)
            self.mainView.mc.eventHandler.watchHandler.setWatchlist()
        else:
            self.mainView.mc.showMessage('No purchase list', msg)