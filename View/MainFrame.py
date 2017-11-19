try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from View import MultiColumnListbox

class MainFrame:
    root = None
    mainFrame = None
    mainView = None
    listBox = None

    # Create Frame for Main
    def __init__(self, mainView, root):
        self.root = root
        self.mainView = mainView

        mainFrame = Frame(root)
        mainFrame.place(relx=0.00, rely=0.00, relheight=1.00, relwidth=1.00)
        mainFrame.configure(relief=GROOVE)
        mainFrame.configure(width=265)

        mainFrame.imageLabel = Label(mainFrame)
        mainFrame.imageLabel.place(relx=0.02, rely=0.009)
        mainFrame._img0 = PhotoImage(file="../View/Pictures/icon.png")
        mainFrame.imageLabel.configure(image=mainFrame._img0)
        mainFrame.imageLabel.bind('<Button-1>', self.clickLogo)

        mainFrame.IDLabel = Label(mainFrame)
        mainFrame.IDLabel.place(relx=0.288, rely=0.001, height=34, width=55)
        mainFrame.IDLabel.configure(text='''ID       :''')
        mainFrame.IDLabel.lift()

        mainFrame.nameLabel = Label(mainFrame)
        mainFrame.nameLabel.place(relx=0.285, rely=0.05, height=34, width=60)
        mainFrame.nameLabel.configure(text='''Name  :''')
        mainFrame.nameLabel.lift()

        mainFrame.moneyLabel = Label(mainFrame)
        mainFrame.moneyLabel.place(relx=0.282, rely=0.1, height=34, width=60)
        mainFrame.moneyLabel.configure(text='''Money :''')
        mainFrame.moneyLabel.lift()

        mainFrame.ID = Label(mainFrame)
        mainFrame.ID.place(relx=0.5, rely=0.001, height=34, width=75)
        mainFrame.ID.configure(text=self.mainView.mc.user.id)
        mainFrame.ID.lift()

        mainFrame.name = Label(mainFrame)
        mainFrame.name.place(relx=0.5, rely=0.05, height=34, width=75)
        mainFrame.name.configure(text=self.mainView.mc.user.name)
        mainFrame.name.lift()

        mainFrame.money = Label(mainFrame)
        mainFrame.money.place(relx=0.493, rely=0.1, height=34, width=70)
        mainFrame.money.configure(text=self.mainView.mc.user.money)
        mainFrame.money.lift()

        mainFrame.setting = Label(mainFrame)
        mainFrame.setting.place(relx=0.76, rely=0.019, height=60, width=60)
        mainFrame.settingImg = PhotoImage(file='../View/Pictures/MainFrame/Setting.png')
        mainFrame.setting.configure(image=mainFrame.settingImg)
        mainFrame.setting.bind('<Button-1>', self.setting)

        container = Frame(mainFrame, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        mainFrame.roomFrame = MultiColumnListbox.MultiColumnListbox(container)
        mainFrame.roomFrame.tree.bind('<Double-Button-1>', self.goRoom)

        mainFrame.sellingButton = Button(mainFrame)
        mainFrame.sellingButton.place(relx=0.23, rely=0.8, height=59, width=150)
        mainFrame._img1 = PhotoImage(file='../View/Pictures/MainFrame/Selling.png')
        mainFrame.sellingButton.configure(image=mainFrame._img1)
        mainFrame.sellingButton.bind('<Button-1>', self.selling)

        mainFrame.copyrightLabel = Label(mainFrame)
        mainFrame.copyrightLabel.place(relx=0.07, rely=0.92, height=24, width=242)
        mainFrame.copyrightLabel.configure(text='''Made by 201411317 Cho MinKyu''')

        self.mainView.mainFrame = mainFrame
        self.mainFrame = mainFrame

    # go Room Action for Button
    def goRoom(self, event):

        # Get Current Item from listbox
        curItem = self.mainFrame.roomFrame.tree.item(self.mainFrame.roomFrame.tree.focus())

        # Send the Request to the Controller
        rFlag, msg = self.mainView.mc.eventHandler.mainHandler.goRoom(curItem['values'][0])

        # Get the Message from Controller whether go Room was succeeded
        if rFlag:
            path = self.mainView.mc.adminRoom.roomList[curItem['values'][0]].item.imgPath
            self.mainView.mc.eventHandler.roomHandler.setImg(path)
            self.mainView.mc.eventHandler.changeFrame(self.mainView.frameList['room'].roomFrame)
        else:
            self.mainView.mc.showMessage('msg', 'Failed  to get room info')

    # Refresh User's Data
    def refreshData(self):
        name, id, money = self.mainView.mc.user.getUser()
        self.mainFrame.ID.configure(text=id)
        self.mainFrame.name.configure(text=name)
        self.mainFrame.money.configure(text=money)

    # Change the frame to SettingFrame
    def setting(self, event):
        self.mainView.mc.eventHandler.changeFrame(self.mainView.frameList['setting'].settingFrame)

    # Change the frame to SellingFrame
    def selling(self, event):
        self.mainView.mc.eventHandler.changeFrame(self.mainView.frameList['selling'].sellingFrame)

    # Request the room List to the controller
    def clickLogo(self, event):
        self.mainView.mc.eventHandler.mainHandler.reqList()
