try:
    from Tkinter import *
except ImportError:
    from tkinter import *

class ChangePWFrame:
    mainView = None

    # Create Frame for Change Password
    def __init__(self, mainView):
        self.mainView = mainView
        self.main = Tk()
        self.main.title('Authentication Box')
        self.main.geometry('225x150')

        # adds username entry widget and defines its properties
        self.curPWLabel = Label(self.main)
        self.curPWLabel.configure(text=''' Cur PW  : ''')
        self.curPWLabel.place(relx=0.02, rely=0.1)

        self.curPWEntry = Entry(self.main, show='*')
        self.curPWEntry.place(relx=0.3, rely=0.1)

        # adds password entry widget and defines its properties
        self.newPWLabel = Label(self.main)
        self.newPWLabel.configure(text=''' New PW :''')
        self.newPWLabel.place(relx=0.019, rely=0.3)

        self.newPWEntry = Entry(self.main, show='*')
        self.newPWEntry.place(relx=0.3, rely=0.3)

        self.newPW2Label = Label(self.main)
        self.newPW2Label.configure(text='''New PW2 :''')
        self.newPW2Label.place(relx=0.006, rely=0.5)

        self.newPW2Entry = Entry(self.main, show='*')
        self.newPW2Entry.place(relx=0.3, rely=0.5)

        # adds changePW button and defines its properties
        self.changePWButton= Button(self.main, text='Change PW', command=self.changePW)
        self.changePWButton.bind('<Return>', self.changePW)
        self.changePWButton.place(relx=0.27, rely=0.7, height=40, width=100)
        self.main.lift()
        self.main.mainloop()

    # Change Password Action for Button
    def changePW(self, *event):
        # Get Current PW, New PW, NewPW 2 from Entry
        curPW = self.curPWEntry.get()
        newPW = self.newPWEntry.get()
        newPW2 = self.newPW2Entry.get()

        # Send the Request to the Controller
        changeFlag, msg = self.mainView.mc.eventHandler.settingHandler.changePW(self.mainView.mc.user.id, curPW, newPW, newPW2)

        # Get the Message from Controller whether Change Password was succeeded
        if changeFlag:
            self.mainView.mc.eventHandler.changeFrame(self.mainView.frameList['main'].mainFrame)
            self.main.destroy()
            self.mainView.mc.showMessage('Change PW Complete', msg)
        else:
            self.mainView.mc.showMessage('Change PW Error', msg)

