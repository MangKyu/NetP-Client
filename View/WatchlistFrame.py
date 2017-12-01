try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from PIL import ImageTk, Image
import re

class WatchlistFrame:
    root = None
    watchlistFrame = None
    mainView = None
    labelList = []
    imgList = []

    # Create Frame for Room with Item
    def __init__(self, mainView, root):
        self.root = root
        self.mainView = mainView

        watchlistFrame = Frame(root)
        watchlistFrame.place(relx=0.00, rely=0.00, relheight=1.00, relwidth=1.00)
        watchlistFrame.configure(relief=GROOVE)
        watchlistFrame.configure(width=265)

        watchlistFrame.bgLabel = Label(watchlistFrame)
        watchlistFrame.bgLabel.place(x=0, y=0, relwidth=1, relheight=1)
        watchlistFrame.bgImage = PhotoImage(file="../View/Pictures/watchlistFrame/background.png")
        watchlistFrame.bgLabel.configure(image=watchlistFrame.bgImage)

        watchlistFrame.imageLabel = Label(watchlistFrame)
        watchlistFrame.imageLabel.place(relx=0.08, rely=0.15)
        watchlistFrame._img0 = PhotoImage(file="../View/Pictures/logo.png")
        watchlistFrame.imageLabel.configure(image=watchlistFrame._img0, bg='#4f779e')
        watchlistFrame.imageLabel.bind('<Button-1>', self.clickLogo)

        watchlistFrame.name = Label(watchlistFrame)
        watchlistFrame.name.place(relx=0.5, rely=0.146, relheight=0.04, relwidth=0.3)
        watchlistFrame.name.configure(text=self.mainView.mc.user.name, bg='#4f779e', fg='white', font=('08서울남산체 M', 12))
        watchlistFrame.name.lift()

        watchlistFrame.money = Label(watchlistFrame)
        watchlistFrame.money.place(relx=0.5, rely=0.212, relheight=0.04, relwidth=0.3)
        watchlistFrame.money.configure(text=self.mainView.mc.user.money, bg='#4f779e', fg='white', font=('08서울남산체 B', 12))
        watchlistFrame.money.lift()

        watchlistFrame.imgPath = None

        watchlistFrame.itemFrame = Frame(watchlistFrame, highlightbackground="green", highlightcolor="green",
                                         highlightthickness=1)
        watchlistFrame.itemFrame.place(relx=0.06, rely=0.3, relheight=0.6, relwidth=0.88)

        # --- create canvas with scrollbar ---

        watchlistFrame.canvas = Canvas(watchlistFrame.itemFrame)
        watchlistFrame.canvas.pack(side=LEFT)

        watchlistFrame.verScrollbar = Scrollbar(watchlistFrame.itemFrame, command=watchlistFrame.canvas.yview,
                                                orient=VERTICAL)
        watchlistFrame.verScrollbar.pack(side=RIGHT, fill='y', expand =TRUE)
        watchlistFrame.canvas.configure(yscrollcommand=watchlistFrame.verScrollbar.set)
        watchlistFrame.verScrollbar.lift()

        # when all widgets are in canvas
        watchlistFrame.canvas.bind('<Configure>', self.on_configure)

        # --- put frame in canvas ---

        watchlistFrame.listFrame = Frame(watchlistFrame.itemFrame)
        watchlistFrame.canvas.create_window((0, 0), window=watchlistFrame.listFrame, anchor='nw')
        watchlistFrame.canvas.place(relx=0, rely=0, relheight=1, relwidth=1)
        watchlistFrame.canvas.pack(side=LEFT, expand=TRUE, padx=25)

        self.watchlistFrame = watchlistFrame

        # --- add widgets in frame ---\
        self.mainView.watchlistFrame = watchlistFrame
        self.watchlistFrame = watchlistFrame

    def createCanvas(self):
        self.watchlistFrame.canvas.destroy()
        self.watchlistFrame.listFrame.destroy()
        self.watchlistFrame.itemFrame.destroy()

        self.watchlistFrame.itemFrame = Frame(self.watchlistFrame, highlightbackground="green", highlightcolor="green",
                                         highlightthickness=1)
        self.watchlistFrame.itemFrame.place(relx=0.06, rely=0.3, relheight=0.6, relwidth=0.88)

        self.watchlistFrame.canvas = Canvas(self.watchlistFrame.itemFrame)
        self.watchlistFrame.canvas.pack(side=LEFT)

        self.watchlistFrame.verScrollbar = Scrollbar(self.watchlistFrame.itemFrame, command=self.watchlistFrame.canvas.yview,
                                                orient=VERTICAL)
        self.watchlistFrame.verScrollbar.pack(side=RIGHT, fill='y', expand=TRUE)
        self.watchlistFrame.canvas.configure(yscrollcommand=self.watchlistFrame.verScrollbar.set)
        self.watchlistFrame.verScrollbar.lift()

        # when all widgets are in canvas
        self.watchlistFrame.canvas.bind('<Configure>', self.on_configure)
        self.watchlistFrame.listFrame = Frame(self.watchlistFrame.itemFrame)
        self.watchlistFrame.canvas.create_window((0, 0), window=self.watchlistFrame.listFrame, anchor='nw')
        self.watchlistFrame.canvas.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.watchlistFrame.canvas.pack(side=LEFT, expand=TRUE)

    def on_configure(self, event):
        # update scroll region after starting 'mainloop'
        # when all widgets are in canvas
        self.watchlistFrame.canvas.configure(scrollregion=self.watchlistFrame.canvas.bbox('all'))

    # Go to the MainFrame
    def clickLogo(self, event):
        self.mainView.mc.eventHandler.changeFrame(self.mainView.frameList['main'].mainFrame)

    def refreshData(self):
        name, money = self.mainView.mc.user.getUser()
        self.watchlistFrame.name.configure(text=name)
        self.watchlistFrame.money.configure(text=money)

    def openPhotoImage(self, path):
        img = Image.open(path)
        img = img.resize((240, 120), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        return img

    def createItem(self, itName, path, price):
        img = self.openPhotoImage(path)
        panel = Label(self.watchlistFrame.listFrame, image=img)
        panel.image = img
        panel.place(relwidth=1)
        panel.pack(side=TOP)
        label = Label(self.watchlistFrame.listFrame, font=('08서울남산체 M', 15))
        label.configure(text=itName + ': ' + str(price) +'won')
        label.pack(side=TOP, pady=(0, 10))
        label.bind('<Button-1>', lambda text=label['text']: self.goRoom(label))
        self.labelList.append(label)
        self.imgList.append(panel)
        
    def goRoom(self, label):
        m = re.search(r"\[([A-Za-z0-9_]+)\]", label['text'])
        roomIdx = int(m.group(1))
        try:
            rFlag, msg = self.mainView.mc.eventHandler.mainHandler.goRoom(roomIdx)
            # Get the Message from Controller whether go Room was succeeded
            if rFlag:
                path = self.mainView.mc.adminRoom.roomList[roomIdx].item.imgPath
                self.mainView.mc.eventHandler.roomHandler.setImg(path, self.mainView.mc.adminRoom.roomList[roomIdx].watch)
                self.mainView.mc.eventHandler.changeFrame(self.mainView.frameList['room'].roomFrame)
            else:
                self.mainView.mc.showMessage('msg', 'Failed  to get room info')
        except:
            pass