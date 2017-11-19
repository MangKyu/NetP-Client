try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from Model import Item

class SellingFrame:
    root = None
    sellingFrame = None
    mainView = None

    # Create Frame for Selling
    def __init__(self, mainView, root):
        self.root = root
        self.mainView = mainView

        sellingFrame = Frame(root)
        sellingFrame.place(relx=0.00, rely=0.00, relheight=1.00, relwidth=1.00)
        sellingFrame.configure(relief=GROOVE)
        sellingFrame.configure(width=265)

        sellingFrame.logoImage = Label(sellingFrame)
        sellingFrame.logoImage.place(relx=0.02, rely=0.009)
        sellingFrame._img0 = PhotoImage(file="../View/Pictures/Icon.png")
        sellingFrame.logoImage.configure(image=sellingFrame._img0)
        sellingFrame.logoImage.bind('<Button-1>', self.clickLogo)

        sellingFrame.IDLabel = Label(sellingFrame)
        sellingFrame.IDLabel.place(relx=0.288, rely=0.001, height=34, width=55)
        sellingFrame.IDLabel.configure(text='''ID       :''')
        sellingFrame.IDLabel.lift()

        sellingFrame.nameLabel = Label(sellingFrame)
        sellingFrame.nameLabel.place(relx=0.285, rely=0.05, height=34, width=60)
        sellingFrame.nameLabel.configure(text='''Name  :''')
        sellingFrame.nameLabel.lift()

        sellingFrame.moneyLabel = Label(sellingFrame)
        sellingFrame.moneyLabel.place(relx=0.282, rely=0.1, height=34, width=60)
        sellingFrame.moneyLabel.configure(text='''Money :''')
        sellingFrame.moneyLabel.lift()

        sellingFrame.ID = Label(sellingFrame)
        sellingFrame.ID.place(relx=0.5, rely=0.001, height=34, width=75)
        sellingFrame.ID.configure(text=self.mainView.mc.user.id)
        sellingFrame.ID.lift()

        sellingFrame.name = Label(sellingFrame)
        sellingFrame.name.place(relx=0.5, rely=0.05, height=34, width=75)
        sellingFrame.name.configure(text=self.mainView.mc.user.name)
        sellingFrame.name.lift()

        sellingFrame.money = Label(sellingFrame)
        sellingFrame.money.place(relx=0.493, rely=0.1, height=34, width=70)
        sellingFrame.money.configure(text=self.mainView.mc.user.money)
        sellingFrame.money.lift()

        sellingFrame.sellFrame = Frame(sellingFrame, highlightbackground="green",
                                       highlightcolor="green", highlightthickness=1)
        sellingFrame.sellFrame.place(relx=0.05, rely=0.18, relheight=0.65, relwidth=0.9)

        sellingFrame.sellFrame.itemLabel = Label(sellingFrame.sellFrame)
        sellingFrame.sellFrame.itemLabel.place(relx=0.015, rely=0.04, relheight=0.1, relwidth=0.2)
        sellingFrame.sellFrame.itemLabel.configure(text=" Item  :")

        sellingFrame.sellFrame.itemEntry = Entry(sellingFrame.sellFrame)
        sellingFrame.sellFrame.itemEntry.place(relx=0.26, rely=0.04, relheight=0.1, relwidth=0.68)

        sellingFrame.sellFrame.priceLabel = Label(sellingFrame.sellFrame)
        sellingFrame.sellFrame.priceLabel.place(relx=0.015, rely=0.19, relheight=0.1, relwidth=0.2)
        sellingFrame.sellFrame.priceLabel.configure(text="Price  :")

        sellingFrame.sellFrame.priceEntry = Entry(sellingFrame.sellFrame)
        sellingFrame.sellFrame.priceEntry.place(relx=0.26, rely=0.19, relheight=0.1, relwidth=0.68)

        sellingFrame.sellFrame.descLabel = Label(sellingFrame.sellFrame)
        sellingFrame.sellFrame.descLabel.place(relx=0.015, rely=0.34, relheight=0.1, relwidth=0.2)
        sellingFrame.sellFrame.descLabel.configure(text="Desc  :")

        sellingFrame.sellFrame.descText = Text(sellingFrame.sellFrame)
        sellingFrame.sellFrame.descText.place(relx=0.26, rely=0.34, relheight=0.15, relwidth=0.68)

        sellingFrame.sellFrame.imagePath = None

        sellingFrame.sellFrame.imgLabel = Label(sellingFrame.sellFrame)
        sellingFrame._img1 = PhotoImage(file="../View/Pictures/SellingFrame/ImgIcon.png")
        sellingFrame.sellFrame.imgLabel.place(relx=0.2, rely=0.55, height=120, width=150)
        sellingFrame.sellFrame.imgLabel.configure(image=sellingFrame._img1)
        sellingFrame.sellFrame.imgLabel.bind('<Button-1>', self.openItemImg)

        sellingFrame.sellingButton = Button(sellingFrame)
        sellingFrame.sellingButton.place(relx=0.23, rely=0.83, height=40, width=150)
        sellingFrame.sellingButton.configure(text=" Sell")
        sellingFrame.sellingButton.bind('<Button-1>', self.sell)

        sellingFrame.copyrightLabel = Label(sellingFrame)
        sellingFrame.copyrightLabel.place(relx=0.07, rely=0.92, height=24, width=242)
        sellingFrame.copyrightLabel.configure(text='''Made by 201411317 Cho MinKyu''')

        self.mainView.sellingFrame = sellingFrame
        self.sellingFrame = sellingFrame

    # Get the Image for item
    def openItemImg(self, event):
        self.sellingFrame.sellFrame.imagePath = filedialog.askopenfilename(
            title="choose your file", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        if self.sellingFrame.sellFrame.imagePath != '':
            img = Image.open(self.sellingFrame.sellFrame.imagePath)
            img = img.resize((150, 120), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            self.sellingFrame._img1 = img
            self.sellingFrame.sellFrame.imgLabel.configure(image=self.sellingFrame._img1)

    # Go to the MainFrame
    def clickLogo(self, event):
        self.mainView.mc.eventHandler.changeFrame(self.mainView.frameList['main'].mainFrame)

    # Sell Action for Button
    def sell(self, event):
        # Get item name, price, item Description from Entry
        itemName = self.sellingFrame.sellFrame.itemEntry.get()
        price = self.sellingFrame.sellFrame.priceEntry.get()
        itemDesc = self.sellingFrame.sellFrame.descText.get("1.0", END)

        # Check price whether it is integer value
        if self.sellingFrame.sellFrame.imagePath != '':
            try:
                integer_price = int(price)
            except ValueError:
                msg = 'price is not an integer'
                self.mainView.mc.showMessage('Selling Frame Error', msg)
                return
            else:
                # Create item instance
                item = Item.Item(self.mainView.mc.user.id, itemName, integer_price, itemDesc, self.sellingFrame.sellFrame.imagePath)

                # Get the Message from Controller whether sell request was succeeded
                sellFlag, msg = self.mainView.mc.eventHandler.sellingHandler.sell(item)
                if sellFlag:
                    self.mainView.mc.eventHandler.changeFrame(self.mainView.frameList['main'].mainFrame)
                    self.clearFrame()
                    return
        else:
            msg = 'No Image!'
            self.mainView.mc.showMessage('Selling Frame Error', msg)

    # Clear the Entry
    def clearFrame(self):
        self.sellingFrame.sellFrame.descText.delete('1.0', END)
        self.sellingFrame.sellFrame.priceEntry.delete(0, END)
        self.sellingFrame.sellFrame.itemEntry.delete(0, END)
        self.sellingFrame._img1 = PhotoImage(file="../View/Pictures/SellingFrame/ImgIcon.png")
        self.sellingFrame.sellFrame.imgLabel.configure(image=self.sellingFrame._img1)

    # Refresh User's Data
    def refreshData(self):
        name, id, money = self.mainView.mc.user.getUser()
        self.sellingFrame.ID.configure(text=id)
        self.sellingFrame.name.configure(text=name)
        self.sellingFrame.money.configure(text=money)
