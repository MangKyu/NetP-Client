try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from PIL import ImageTk, Image
from View import ImageFrame
class RoomFrame:
    root = None
    roomFrame = None
    mainView = None

    # Create Frame for Room with Item
    def __init__(self, mainView, root):
        self.root = root
        self.mainView = mainView

        roomFrame = Frame(root)
        roomFrame.place(relx=0.00, rely=0.00, relheight=1.00, relwidth=1.00)
        roomFrame.configure(relief=GROOVE)
        roomFrame.configure(width=265)

        roomFrame.bgLabel = Label(roomFrame)
        roomFrame.bgLabel.place(x=0, y=0, relwidth=1, relheight=1)
        roomFrame.bgImage = PhotoImage(file="../View/Pictures/RoomFrame/background.png")
        roomFrame.bgLabel.configure(image=roomFrame.bgImage)

        roomFrame.imageLabel = Label(roomFrame)
        roomFrame.imageLabel.place(relx=0.08, rely=0.15)
        roomFrame._img0 = PhotoImage(file="../View/Pictures/RoomFrame/logo.png")
        roomFrame.imageLabel.configure(image=roomFrame._img0, bg='#4f779e')
        roomFrame.imageLabel.bind('<Button-1>', self.clickLogo)

        roomFrame.name = Label(roomFrame)
        roomFrame.name.place(relx=0.5, rely=0.146, relheight=0.04, relwidth=0.3)
        roomFrame.name.configure(text=self.mainView.mc.user.name, bg='#4f779e', fg='white', font=('08서울남산체 M', 12))
        roomFrame.name.lift()

        roomFrame.money = Label(roomFrame)
        roomFrame.money.place(relx=0.5, rely=0.212, relheight=0.04, relwidth=0.3)
        roomFrame.money.configure(text=self.mainView.mc.user.money, bg='#4f779e', fg='white', font=('08서울남산체 B', 12))
        roomFrame.money.lift()

        roomFrame.item = Label(roomFrame)
        roomFrame.item.place(relx=0.32, rely=0.605, relheight=0.04, relwidth=0.58)
        roomFrame.item.configure(text='itemName', bg="#56769e", fg='white', font=('08서울남산체 B', 12))

        roomFrame.seller = Label(roomFrame)
        roomFrame.seller.place(relx=0.32, rely=0.554, relheight=0.04, relwidth=0.58)
        roomFrame.seller.configure(text='Seller ID', bg="#56769e",fg='white', font=('08서울남산체 B', 12))

        roomFrame.price = Label(roomFrame)
        roomFrame.price.place(relx=0.32, rely=0.655, relheight=0.04, relwidth=0.58)
        roomFrame.price.configure(text="Price  ", bg="#56769e", fg='white', font=('08서울남산체 B', 12))

        roomFrame.curT = Label(roomFrame)
        roomFrame.curT.place(relx=0.32, rely=0.702, relheight=0.04, relwidth=0.58)
        roomFrame.curT.configure(text="curT ", bg="#56769e", fg='white', font=('08서울남산체 B', 12))

        roomFrame.endT = Label(roomFrame)
        roomFrame.endT.place(relx=0.32, rely=0.752, relheight=0.04, relwidth=0.58)
        roomFrame.endT.configure(text="endT ", bg = "#56769e", fg='white', font=('08서울남산체 B', 12))

        roomFrame.descText = Text(roomFrame, bg='#56769e')
        roomFrame.descText.place(relx=0.32, rely=0.802, relheight=0.07, relwidth=0.58)
        roomFrame.descText.configure(state=DISABLED, fg='white', font=('08서울남산체 B', 12))
        roomFrame.imgPath = None

        roomFrame.imgLabel = Label(roomFrame)
        roomFrame._img1 = PhotoImage(file="../Controller/test.png")
        roomFrame.imgLabel.place(relx=0.26, rely=0.3, height=120, width=150)
        roomFrame.imgLabel.configure(image=roomFrame._img1)
        roomFrame.imgLabel.bind('<Button-1>', self.newImage)

        roomFrame.watchLabel = Label(roomFrame)
        roomFrame.watch_img1 = PhotoImage(file="../View/Pictures/RoomFrame/YesWatch.png")
        roomFrame.watchLabel.place(relx=0.85, rely=0.3, height=25, width=25)
        roomFrame.watchLabel.configure(image=roomFrame.watch_img1, bg='#4f779e')
        roomFrame.watchLabel.bind('<Button-1>', self.sendWatch)

        roomFrame.priceEntry = Entry(roomFrame)
        roomFrame.priceEntry.place(relx=0.059, rely=0.9, height=30, relwidth=0.58)

        roomFrame.roomButton = Button(roomFrame)
        roomFrame.roomButton.place(relx=0.66, rely=0.9, height=30, relwidth=0.28)
        roomFrame.roomButton.configure(bg='#4f536e', fg='white', text='''BUY''', font=('08서울남산체 M', 16))
        roomFrame.roomButton.bind('<Button-1>', self.buy)
        self.mainView.roomFrame = roomFrame
        self.roomFrame = roomFrame

    # Go to the MainFrame
    def clickLogo(self, event):
        self.mainView.mc.eventHandler.changeFrame(self.mainView.frameList['main'].mainFrame)
        self.roomFrame.priceEntry.delete(0, END)

    # Set the Image in the RoomFrame
    def setImage(self, watch):
        img = Image.open(self.roomFrame.imgPath)
        img = img.resize((150, 120), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.roomFrame._img1 = img
        self.roomFrame.imgLabel.configure(image=self.roomFrame._img1)
        if watch:
            self.roomFrame.watch_img1 = PhotoImage(file="../View/Pictures/RoomFrame/YesWatch.png")
        else:
            self.roomFrame.watch_img1 = PhotoImage(file="../View/Pictures/RoomFrame/NoWatch.png")
        self.roomFrame.watchLabel.configure(image=self.roomFrame.watch_img1, bg='#4f779e')
        self.setData()

    # Set data for the item in the RoomFrame
    def setData(self):
        self.roomFrame.item.configure(text=self.mainView.mc.adminRoom.room.item.itemName)
        self.roomFrame.seller.configure(text=self.mainView.mc.adminRoom.room.seller)
        self.roomFrame.price.configure(text=self.mainView.mc.adminRoom.room.item.price)
        self.roomFrame.endT.configure(text=self.mainView.mc.adminRoom.room.endTime)
        self.roomFrame.descText.configure(state=NORMAL)
        self.roomFrame.descText.delete('1.0', END)
        self.roomFrame.descText.insert(END, self.mainView.mc.adminRoom.room.item.itemDesc)
        self.roomFrame.descText.configure(state=DISABLED)

    # Buy Action for Button
    def buy(self, event):
        # Get item price, my price, end time of Auction from Entry
        price = self.roomFrame.price['text']
        myPrice = self.roomFrame.priceEntry.get()
        endTime = self.roomFrame.endT['text']

        # Check my price whether it is integer value
        try:
            int_price = int(myPrice)
        except ValueError:
            msg = 'price is not an integer'
            self.mainView.mc.showMessage('Selling Frame Error', msg)
            return

        # Send the Request to the Controller
        bFlag, msg = self.mainView.mc.eventHandler.roomHandler.buy(int_price, price, endTime,
                                                              self.mainView.mc.adminRoom.room.roomIdx)
        # Get the Message from Controller whether buy request was succeeded
        if bFlag:
            self.mainView.mc.eventHandler.changeFrame(self.mainView.frameList['main'].mainFrame)
            self.roomFrame.priceEntry.delete(0, END)
        else:
            self.mainView.mc.showMessage('Selling Frame Error', msg)

    # Refresh User's Data
    def refreshData(self):
        name, id, money = self.mainView.mc.user.getUser()
        self.roomFrame.name.configure(text=name)
        self.roomFrame.money.configure(text=money)

    def newImage(self, *event):
        ImageFrame.ImageFrame(self.mainView, self.roomFrame.imgPath)

    def sendWatch(self, *event):
        # Send the Request to the Controller
        wFlag, msg = self.mainView.mc.eventHandler.roomHandler.sendWatch(self.mainView.mc.adminRoom.room.roomIdx,
                                                                         self.mainView.mc.adminRoom.room.watch)
        # Get the Message from Controller whether buy request was succeeded
        if wFlag:
            self.roomFrame.priceEntry.delete(0, END)
            path = self.mainView.mc.adminRoom.room.item.imgPath
            watch = self.mainView.mc.adminRoom.room.watch
            self.mainView.mc.eventHandler.roomHandler.setImg(path, watch)
            self.mainView.mc.eventHandler.changeFrame(self.mainView.frameList['room'].roomFrame)

        else:
            self.mainView.mc.showMessage('Selling Frame Error', msg)
