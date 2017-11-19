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

        settingFrame.logoImage = Label(settingFrame)
        settingFrame.logoImage.place(relx=0.02, rely=0.009)
        settingFrame._img0 = PhotoImage(file="../View/Pictures/Icon.png")
        settingFrame.logoImage.configure(image=settingFrame._img0)
        settingFrame.logoImage.bind('<Button-1>', self.clickLogo)

        settingFrame.IDLabel = Label(settingFrame)
        settingFrame.IDLabel.place(relx=0.288, rely=0.001, height=34, width=55)
        settingFrame.IDLabel.configure(text='''ID       :''')
        settingFrame.IDLabel.lift()

        settingFrame.ID = Label(settingFrame)
        settingFrame.ID.place(relx=0.5, rely=0.001, height=34, width=75)
        settingFrame.ID.configure(text=self.mainView.mc.user.id)
        settingFrame.ID.lift()

        settingFrame.nameLabel = Label(settingFrame)
        settingFrame.nameLabel.place(relx=0.285, rely=0.05, height=34, width=60)
        settingFrame.nameLabel.configure(text='''Name  :''')
        settingFrame.nameLabel.lift()

        settingFrame.name = Label(settingFrame)
        settingFrame.name.place(relx=0.5, rely=0.05, height=34, width=75)
        settingFrame.name.configure(text=self.mainView.mc.user.name)
        settingFrame.name.lift()

        settingFrame.moneyLabel = Label(settingFrame)
        settingFrame.moneyLabel.place(relx=0.282, rely=0.1, height=34, width=60)
        settingFrame.moneyLabel.configure(text='''Money :''')
        settingFrame.moneyLabel.lift()

        settingFrame.money = Label(settingFrame)
        settingFrame.money.place(relx=0.493, rely=0.1, height=34, width=70)
        settingFrame.money.configure(text=self.mainView.mc.user.money)
        settingFrame.money.lift()

        settingFrame.itemFrame = Frame(settingFrame, highlightbackground="green", highlightcolor="green",
                                       highlightthickness=1)
        settingFrame.itemFrame.place(relx=0.05, rely=0.18, relheight=0.7, relwidth=0.9)

        def on_configure(event):
            # update scroll region after starting 'mainloop'
            # when all widgets are in canvas
            settingFrame.canvas.configure(scrollregion=settingFrame.canvas.bbox('all'))

        # --- create canvas with scrollbar ---

        settingFrame.canvas = Canvas(settingFrame.itemFrame)
        settingFrame.canvas.pack(side=LEFT)

        settingFrame.scrollbar = Scrollbar(settingFrame.itemFrame, command=settingFrame.canvas.yview)
        settingFrame.scrollbar.pack(side=RIGHT, fill='y')
        settingFrame.canvas.configure(yscrollcommand=settingFrame.scrollbar.set)

        # update scrollregion after starting 'mainloop'
        # when all widgets are in canvas
        settingFrame.canvas.bind('<Configure>', on_configure)

        # --- put frame in canvas ---

        settingFrame.listframe = Frame(settingFrame.itemFrame)
        settingFrame.canvas.create_window((0, 0), window=settingFrame.listframe, anchor='nw')
        settingFrame.canvas.place(relx=0, rely=0, relheight=1, relwidth=1)

        # --- add widgets in frame ---\
        img = self.mainView.mc.openPhotoImage(self.path + "Change.png")
        panel = Label(settingFrame.itemFrame, image=img)
        panel.image = img
        label = Label(settingFrame.itemFrame, font=('08서울남산체 M', 15))
        label.configure(text='''Change Password''')
        panel.place(relx=0.01, rely=0.01)
        label.place(relx=0.27, rely=0.065)
        panel.bind('<Button-1>', self.changePW)

        img = self.mainView.mc.openPhotoImage(self.path + "Money.png")
        panel = Label(settingFrame.itemFrame, image=img)
        panel.image = img
        label = Label(settingFrame.itemFrame, font=('08서울남산체 M', 15))
        label.configure(text='''Charge Money''')
        panel.place(relx=0.01, rely=0.22)
        label.place(relx=0.32, rely=0.28)
        panel.bind('<Button-1>', self.chargeMoney)

        img = self.mainView.mc.openPhotoImage(self.path + "Barcode.png")
        panel = Label(settingFrame.itemFrame, image=img)
        panel.image = img
        label = Label(settingFrame.itemFrame, font=('08서울남산체 M', 15))
        label.configure(text='''Transaction List''')
        panel.place(relx=0.01, rely=0.43)
        label.place(relx=0.3, rely=0.495)
        panel.bind('<Button-1>', self.purchaseList)

        img = self.mainView.mc.openPhotoImage(self.path + "Cart.png")
        panel = Label(settingFrame.itemFrame, image=img)
        panel.image = img
        label = Label(settingFrame.itemFrame, font=('08서울남산체 M', 15))
        label.configure(text='''Auction List''')
        panel.place(relx=0.01, rely=0.64)
        label.place(relx=0.38, rely=0.71)
        panel.bind('<Button-1>', self.aucList)

        self.mainView.settingFrame = settingFrame
        self.settingFrame = settingFrame

    # Refresh User's Data
    def refreshData(self):
        name, id, money = self.mainView.mc.user.getUser()
        self.settingFrame.ID.configure(text=id)
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
