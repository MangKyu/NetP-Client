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

        sellingFrame.bgLabel = Label(sellingFrame)
        sellingFrame.bgLabel.place(x=0, y=0, relwidth=1, relheight=1)
        sellingFrame.bgImage = PhotoImage(file="../View/Pictures/SellingFrame/background.png")
        sellingFrame.bgLabel.configure(image=sellingFrame.bgImage)

        sellingFrame.imageLabel = Label(sellingFrame)
        sellingFrame.imageLabel.place(relx=0.08, rely=0.15)
        sellingFrame._img0 = PhotoImage(file="../View/Pictures/SellingFrame/logo.png")
        sellingFrame.imageLabel.configure(image=sellingFrame._img0, bg='#4f779e')
        sellingFrame.imageLabel.bind('<Button-1>', self.clickLogo)

        sellingFrame.name = Label(sellingFrame)
        sellingFrame.name.place(relx=0.5, rely=0.146, relheight=0.05, relwidth=0.3)
        sellingFrame.name.configure(text=self.mainView.mc.user.name, bg='#4f779e', fg='white', font=('08서울남산체 M', 12))
        sellingFrame.name.lift()

        sellingFrame.money = Label(sellingFrame)
        sellingFrame.money.place(relx=0.5, rely=0.212,relheight=0.05, relwidth=0.3)
        sellingFrame.money.configure(text=self.mainView.mc.user.money, bg='#4f779e', fg='white', font=('08서울남산체 M', 12))
        sellingFrame.money.lift()

        sellingFrame.itemEntry = Entry(sellingFrame, bg = "#1c4478")
        sellingFrame.itemEntry.place(relx=0.3, rely=0.595, relheight=0.05, relwidth=0.58)
        sellingFrame.itemEntry.configure(fg='white', font=('08서울남산체 M', 12))

        sellingFrame.priceEntry = Entry(sellingFrame, bg = "#1c4478")
        sellingFrame.priceEntry.place(relx=0.3, rely=0.665, relheight=0.05, relwidth=0.58)
        sellingFrame.priceEntry.configure(fg='white', font=('08서울남산체 M', 12))

        sellingFrame.descText = Text(sellingFrame, bg = "#1c4478")
        sellingFrame.descText.place(relx=0.3, rely=0.735, relheight=0.08, relwidth=0.58)
        sellingFrame.descText.configure(fg='white', font=('08서울남산체 M', 12))

        sellingFrame.imagePath = ''

        sellingFrame.imgLabel = Label(sellingFrame)
        sellingFrame._img1 = PhotoImage(file="../View/Pictures/SellingFrame/ImgIcon.png")
        sellingFrame.imgLabel.place(relx=0.26, rely=0.33, height=120, width=150)
        sellingFrame.imgLabel.configure(image=sellingFrame._img1, bg="#5f7899")
        sellingFrame.imgLabel.bind('<Button-1>', self.openItemImg)

        sellingFrame.sellingButton = Button(sellingFrame)
        sellingFrame.sellingButton.place(relx=0.06, rely=0.88, height=30, relwidth=0.88)
        sellingFrame.sellingButton.configure(bg='#4f536e', fg='white', text='''SELL''', font=('08서울남산체 M', 16))
        sellingFrame.sellingButton.bind('<Button-1>', self.sell)

        self.mainView.sellingFrame = sellingFrame
        self.sellingFrame = sellingFrame

    # Get the Image for item
    def openItemImg(self, event):
        self.sellingFrame.imagePath = filedialog.askopenfilename(
            title="choose your file", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        if self.sellingFrame.imagePath != '':
            img = Image.open(self.sellingFrame.imagePath)
            img = img.resize((150, 120), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            self.sellingFrame._img1 = img
            self.sellingFrame.imgLabel.configure(image=self.sellingFrame._img1)

    # Go to the MainFrame
    def clickLogo(self, event):
        self.mainView.mc.eventHandler.changeFrame(self.mainView.frameList['main'].mainFrame)
        self.clearFrame()

    # Sell Action for Button
    def sell(self, event):
        # Get item name, price, item Description from Entry
        itemName = self.sellingFrame.itemEntry.get()
        price = self.sellingFrame.priceEntry.get()
        itemDesc = self.sellingFrame.descText.get("1.0", END)

        # Check price whether it is integer value
        if self.sellingFrame.imagePath is not '' or self.sellingFrame.imagePath is not None:
            try:
                integer_price = int(price)
            except ValueError:
                msg = 'price is not an integer'
                self.mainView.mc.showMessage('Selling Frame Error', msg)
                return
            else:
                # Create item instance
                item = Item.Item(self.mainView.mc.user.id, itemName, integer_price, itemDesc, self.sellingFrame.imagePath)

                # Get the Message from Controller whether sell request was succeeded
                sellFlag, msg = self.mainView.mc.eventHandler.sellingHandler.sell(item)
                if sellFlag:
                    self.mainView.mc.eventHandler.changeFrame(self.mainView.frameList['main'].mainFrame)
                    self.clearFrame()
                    return
                else:
                    self.mainView.mc.showMessage('Selling Frame Error', msg)
        else:
            msg = 'No Image!'
            self.mainView.mc.showMessage('Selling Frame Error', msg)

    # Clear the Entry
    def clearFrame(self):
        self.sellingFrame.descText.delete('1.0', END)
        self.sellingFrame.priceEntry.delete(0, END)
        self.sellingFrame.itemEntry.delete(0, END)
        self.sellingFrame._img1 = PhotoImage(file="../View/Pictures/SellingFrame/ImgIcon.png")
        self.sellingFrame.imgLabel.configure(image=self.sellingFrame._img1)

    # Refresh User's Data
    def refreshData(self):
        name, money = self.mainView.mc.user.getUser()
        self.sellingFrame.name.configure(text=name)
        self.sellingFrame.money.configure(text=money)
