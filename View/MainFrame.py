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

        mainFrame.bgLabel = Label(mainFrame)
        mainFrame.bgLabel.place(x=0, y=0, relwidth=1, relheight=1)
        mainFrame.bgImage = PhotoImage(file="../View/Pictures/MainFrame/background.png")
        mainFrame.bgLabel.configure(image=mainFrame.bgImage)

        mainFrame.imageLabel = Label(mainFrame)
        mainFrame.imageLabel.place(relx=0.08, rely=0.15)
        mainFrame._img0 = PhotoImage(file="../View/Pictures/MainFrame/logo.png")
        mainFrame.imageLabel.configure(image=mainFrame._img0, bg='#4f779e')
        mainFrame.imageLabel.bind('<Button-1>', self.clickLogo)

        mainFrame.name = Label(mainFrame)
        mainFrame.name.place(relx=0.5, rely=0.146, relheight=0.05, relwidth=0.3)
        mainFrame.name.configure(text=self.mainView.mc.user.name, bg='#4f779e', fg='white', font=('08서울남산체 M', 12))
        mainFrame.name.lift()

        mainFrame.money = Label(mainFrame)
        mainFrame.money.place(relx=0.5, rely=0.212,relheight=0.05, relwidth=0.3)
        mainFrame.money.configure(text=self.mainView.mc.user.money, bg='#4f779e', fg='white', font=('08서울남산체 M', 12))
        mainFrame.money.lift()

        mainFrame.setting = Label(mainFrame)
        mainFrame.setting.place(relx=0.8, rely=0.022, height=25, width=25)
        mainFrame.settingImg = PhotoImage(file='../View/Pictures/MainFrame/Setting.png')
        mainFrame.setting.configure(image=mainFrame.settingImg, bg = '#1b5394')
        mainFrame.setting.bind('<Button-1>', self.setting)

        container = Frame(mainFrame, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        mainFrame.roomFrame = MultiColumnListbox.MultiColumnListbox(container)
        mainFrame.roomFrame.tree.bind('<Double-Button-1>', self.goRoom)

        mainFrame.sellingButton = Label(mainFrame)
        mainFrame.sellingButton.place(relx=0.06, rely=0.88, height=30, relwidth=0.88)
        mainFrame.sellingButton.configure(bg='#4f536e', fg='white', text='''SELL''', font=('08서울남산체 M', 16))
        mainFrame.sellingButton.bind('<Button-1>', self.selling)

        self.mainView.mainFrame = mainFrame
        self.mainFrame = mainFrame

    # go Room Action for Button
    def goRoom(self, *event):

        # Get Current Item from listbox
        curItem = self.mainFrame.roomFrame.tree.item(self.mainFrame.roomFrame.tree.focus())
        # Send the Request to the Controller
        try:
            rFlag, msg = self.mainView.mc.eventHandler.mainHandler.goRoom(curItem['values'][0])
            # Get the Message from Controller whether go Room was succeeded
            if rFlag:
                path = self.mainView.mc.adminRoom.roomList[curItem['values'][0]].item.imgPath
                watch = self.mainView.mc.adminRoom.roomList[curItem['values'][0]].watch
                self.mainView.mc.eventHandler.roomHandler.setImg(path, watch)
                self.mainView.mc.eventHandler.changeFrame(self.mainView.frameList['room'].roomFrame)
            else:
                self.mainView.mc.showMessage('msg', 'Failed  to get room info')
        except:
            pass

        # go Room Action for Button
    def goThatRoom(self, roomIdx):
        # Send the Request to the Controller
        try:
            rFlag, msg = self.mainView.mc.eventHandler.mainHandler.goRoom(roomIdx)
            # Get the Message from Controller whether go Room was succeeded
            if rFlag:
                path = self.mainView.mc.adminRoom.roomList[roomIdx].item.imgPath
                watch = self.mainView.mc.adminRoom.roomList[roomIdx].watch
                self.mainView.mc.eventHandler.roomHandler.setImg(path, watch)
                self.mainView.mc.eventHandler.changeFrame(self.mainView.frameList['room'].roomFrame)
            else:
                self.mainView.mc.showMessage('msg', 'Failed  to get room info')
        except:
            pass

    # Refresh User's Data
    def refreshData(self):
        name, money = self.mainView.mc.user.getUser()
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
