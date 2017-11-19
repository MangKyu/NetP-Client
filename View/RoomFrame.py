try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from PIL import ImageTk, Image

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

        roomFrame.logoImage = Label(roomFrame)
        roomFrame.logoImage.place(relx=0.02, rely=0.009)
        roomFrame._img0 = PhotoImage(file="../View/Pictures/Icon.png")
        roomFrame.logoImage.configure(image=roomFrame._img0)
        roomFrame.logoImage.bind('<Button-1>', self.clickLogo)

        roomFrame.IDLabel = Label(roomFrame)
        roomFrame.IDLabel.place(relx=0.288, rely=0.001, height=34, width=55)
        roomFrame.IDLabel.configure(text='''ID       :''')
        roomFrame.IDLabel.lift()

        roomFrame.nameLabel = Label(roomFrame)
        roomFrame.nameLabel.place(relx=0.285, rely=0.05, height=34, width=60)
        roomFrame.nameLabel.configure(text='''Name  :''')
        roomFrame.nameLabel.lift()

        roomFrame.moneyLabel = Label(roomFrame)
        roomFrame.moneyLabel.place(relx=0.282, rely=0.1, height=34, width=60)
        roomFrame.moneyLabel.configure(text='''Money :''')
        roomFrame.moneyLabel.lift()

        roomFrame.ID = Label(roomFrame)
        roomFrame.ID.place(relx=0.5, rely=0.001, height=34, width=75)
        roomFrame.ID.configure(text=self.mainView.mc.user.id)
        roomFrame.ID.lift()

        roomFrame.name = Label(roomFrame)
        roomFrame.name.place(relx=0.5, rely=0.05, height=34, width=75)
        roomFrame.name.configure(text=self.mainView.mc.user.name)
        roomFrame.name.lift()

        roomFrame.money = Label(roomFrame)
        roomFrame.money.place(relx=0.493, rely=0.1, height=34, width=70)
        roomFrame.money.configure(text=self.mainView.mc.user.money)
        roomFrame.money.lift()

        roomFrame.itemFrame = Frame(roomFrame, highlightbackground="green",
                                       highlightcolor="green", highlightthickness=1)
        roomFrame.itemFrame.place(relx=0.05, rely=0.18, relheight=0.65, relwidth=0.9)

        roomFrame.itemFrame.itemLabel = Label(roomFrame.itemFrame)
        roomFrame.itemFrame.itemLabel.place(relx=0.013, rely=0.016, relheight=0.1, relwidth=0.2)
        roomFrame.itemFrame.itemLabel.configure(text=" Item   :")

        roomFrame.itemFrame.item = Label(roomFrame.itemFrame)
        roomFrame.itemFrame.item.place(relx=0.26, rely=0.03, relheight=0.07, relwidth=0.65)
        roomFrame.itemFrame.item.configure(text='itemName')

        roomFrame.itemFrame.sellerLabel = Label(roomFrame.itemFrame)
        roomFrame.itemFrame.sellerLabel.place(relx=0.013, rely=0.1, relheight=0.1, relwidth=0.2)
        roomFrame.itemFrame.sellerLabel.configure(text=" Seller  :")

        roomFrame.itemFrame.seller = Label(roomFrame.itemFrame)
        roomFrame.itemFrame.seller.place(relx=0.26, rely=0.114, relheight=0.07, relwidth=0.65)
        roomFrame.itemFrame.seller.configure(text='Seller ID')

        roomFrame.itemFrame.priceLabel = Label(roomFrame.itemFrame)
        roomFrame.itemFrame.priceLabel.place(relx=0.013, rely=0.184, relheight=0.1, relwidth=0.2)
        roomFrame.itemFrame.priceLabel.configure(text="Price   :")

        roomFrame.itemFrame.price = Label(roomFrame.itemFrame)
        roomFrame.itemFrame.price.place(relx=0.26, rely=0.206, relheight=0.07, relwidth=0.65)
        roomFrame.itemFrame.price.configure(text="Price  ")

        roomFrame.itemFrame.timeLabel = Label(roomFrame.itemFrame)
        roomFrame.itemFrame.timeLabel.place(relx=0.01, rely=0.268, relheight=0.1, relwidth=0.2)
        roomFrame.itemFrame.timeLabel.configure(text="End-T  :")

        roomFrame.itemFrame.time = Label(roomFrame.itemFrame)
        roomFrame.itemFrame.time.place(relx=0.26, rely=0.284, relheight=0.07, relwidth=0.65)
        roomFrame.itemFrame.time.configure(text="time ")

        roomFrame.itemFrame.descLabel = Label(roomFrame.itemFrame)
        roomFrame.itemFrame.descLabel.place(relx=0.013, rely=0.352, relheight=0.1, relwidth=0.2)
        roomFrame.itemFrame.descLabel.configure(text="Desc   :")

        roomFrame.itemFrame.descText = Text(roomFrame.itemFrame)
        roomFrame.itemFrame.descText.place(relx=0.26, rely=0.38, relheight=0.15, relwidth=0.68)
        roomFrame.itemFrame.descText.configure(state=DISABLED)
        roomFrame.itemFrame.imgPath = None

        roomFrame.itemFrame.imgLabel = Label(roomFrame.itemFrame)
        roomFrame._img1 = PhotoImage(file="../Controller/test.png")
        roomFrame.itemFrame.imgLabel.place(relx=0.2, rely=0.56, height=120, width=150)
        roomFrame.itemFrame.imgLabel.configure(image=roomFrame._img1)

        roomFrame.priceEntry = Entry(roomFrame)
        roomFrame.priceEntry.place(relx=0.15, rely=0.85, relheight=0.06, relwidth=0.4)

        roomFrame.roomButton = Button(roomFrame)
        roomFrame.roomButton.place(relx=0.63, rely=0.845, height=30, width=70)
        roomFrame.roomButton.configure(text=" Buy ")
        roomFrame.roomButton.bind('<Button-1>', self.buy)

        roomFrame.copyrightLabel = Label(roomFrame)
        roomFrame.copyrightLabel.place(relx=0.07, rely=0.92, height=24, width=242)
        roomFrame.copyrightLabel.configure(text='''Made by 201411317 Cho MinKyu''')

        self.mainView.roomFrame = roomFrame
        self.roomFrame = roomFrame

    # Go to the MainFrame
    def clickLogo(self, event):
        self.mainView.mc.eventHandler.changeFrame(self.mainView.frameList['main'].mainFrame)
        self.roomFrame.priceEntry.delete(0, END)

    # Set the Image in the RoomFrame
    def setImage(self):
        img = Image.open(self.roomFrame.itemFrame.imgPath)
        img = img.resize((150, 120), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.roomFrame._img1 = img
        self.roomFrame.itemFrame.imgLabel.configure(image=self.roomFrame._img1)
        self.setData()

    # Set data for the item in the RoomFrame
    def setData(self):
        self.roomFrame.itemFrame.item.configure(text=self.mainView.mc.adminRoom.room.item.itemName)
        self.roomFrame.itemFrame.seller.configure(text=self.mainView.mc.adminRoom.room.seller)
        self.roomFrame.itemFrame.price.configure(text=self.mainView.mc.adminRoom.room.item.price)
        self.roomFrame.itemFrame.time.configure(text=self.mainView.mc.adminRoom.room.endTime)
        self.roomFrame.itemFrame.descText.configure(state=NORMAL)
        self.roomFrame.itemFrame.descText.delete('1.0', END)
        self.roomFrame.itemFrame.descText.insert(END, self.mainView.mc.adminRoom.room.item.itemDesc)
        self.roomFrame.itemFrame.descText.configure(state=DISABLED)

    # Buy Action for Button
    def buy(self, event):
        # Get item price, my price, end time of Auction from Entry
        price = self.roomFrame.itemFrame.price['text']
        myPrice = self.roomFrame.priceEntry.get()
        endTime = self.roomFrame.itemFrame.time['text']

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
        self.roomFrame.ID.configure(text=id)
        self.roomFrame.name.configure(text=name)
        self.roomFrame.money.configure(text=money)
