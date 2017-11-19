try:
    from Tkinter import *
except ImportError:
    from tkinter import *

class SignUpFrame:
    mainView = None
    signUpFrame = None

    # Create Frame for Sign Up
    def __init__(self, mainView, root):
        self.root = root
        self.mainView = mainView

        signUpFrame = Frame(root)
        signUpFrame.place(relx=0.00, rely=0.00, relheight=1.00, relwidth=1.00)
        signUpFrame.configure(relief=GROOVE)
        signUpFrame.configure(width=265)

        signUpFrame.imageLabel = Label(signUpFrame)
        signUpFrame.imageLabel.place(relx=0.04, rely=0.02, height=59, width=81)
        signUpFrame._img1 = PhotoImage(file='../View/Pictures/SignUpFrame/logo.png')
        signUpFrame.imageLabel.configure(image=signUpFrame._img1)

        signUpFrame.nameLabel = Label(signUpFrame)
        signUpFrame.nameLabel.place(relx=0.02, rely=0.175, height=34, width=37)
        signUpFrame.nameLabel.configure(text='''Name :''')

        signUpFrame.nameEntry = Entry(signUpFrame)
        signUpFrame.nameEntry.place(relx=0.2, rely=0.185, relheight=0.048, relwidth=0.55)

        signUpFrame.IDBool = False
        signUpFrame.id = ''
        signUpFrame.IDLabel = Label(signUpFrame)
        signUpFrame.IDLabel.place(relx=0.02, rely=0.265, height=34, width=37)
        signUpFrame.IDLabel.configure(text='''ID     :''')

        signUpFrame.IDEntry = Entry(signUpFrame)
        signUpFrame.IDEntry.place(relx=0.2, rely=0.275, relheight=0.048, relwidth=0.55)

        signUpFrame.checkButton = Button(signUpFrame, command=self.chkID)
        signUpFrame.checkButton.place(relx=0.8, rely=0.27, height=26, width=49)
        signUpFrame.checkButton.configure(text='''Chk''')

        signUpFrame.PWLabel = Label(signUpFrame)
        signUpFrame.PWLabel.place(relx=0.02, rely=0.355, height=34, width=37)
        signUpFrame.PWLabel.configure(text='''PW    :''')

        signUpFrame.PWEntry = Entry(signUpFrame, show='*')
        signUpFrame.PWEntry.place(relx=0.2, rely=0.365, relheight=0.048, relwidth=0.55)

        signUpFrame.PW2Label = Label(signUpFrame)
        signUpFrame.PW2Label.place(relx=0.02, rely=0.445, height=34, width=37)
        signUpFrame.PW2Label.configure(text='''PW2  :''')

        signUpFrame.PW2Entry = Entry(signUpFrame, show='*')
        signUpFrame.PW2Entry.place(relx=0.2, rely=0.455, relheight=0.048, relwidth=0.55)

        signUpFrame.mailBool = False

        signUpFrame.mail = ''
        signUpFrame.mailLabel = Label(signUpFrame)
        signUpFrame.mailLabel.place(relx=0.02, rely=0.53, height=34, width=37)
        signUpFrame.mailLabel.configure(text='''mail :''')

        signUpFrame.mailEntry = Entry(signUpFrame)
        signUpFrame.mailEntry.place(relx=0.2, rely=0.54, relheight=0.048, relwidth=0.55)

        signUpFrame.sendButton = Button(signUpFrame, command=self.sendMail)
        signUpFrame.sendButton.place(relx=0.8, rely=0.535, height=26, width=49)
        signUpFrame.sendButton.configure(text='''Send''')

        signUpFrame.codeLabel = Label(signUpFrame)
        signUpFrame.codeLabel.place(relx=0.02, rely=0.615, height=34, width=37)
        signUpFrame.codeLabel.configure(text='''Code :''')

        signUpFrame.code = ''
        signUpFrame.codeEntry = Entry(signUpFrame)
        signUpFrame.codeEntry.place(relx=0.2, rely=0.625, relheight=0.048, relwidth=0.55)

        signUpFrame.moneyLabel = Label(signUpFrame)
        signUpFrame.moneyLabel.place(relx=0.07, rely=0.68, height=52, width=250)
        signUpFrame.moneyLabel.configure(text='''At First, You have [ 0 won ] in your account''')

        signUpFrame.signUpButton = Button(signUpFrame, command=self.signUp)
        signUpFrame.signUpButton.place(relx=0.07, rely=0.78, height=52, width=109)
        signUpFrame.signUpButton.configure(text='''Sign-Up''')

        signUpFrame.cancelButton = Button(signUpFrame, command=self.cancel)
        signUpFrame.cancelButton.place(relx=0.56, rely=0.78, height=52, width=109)
        signUpFrame.cancelButton.configure(text='''Cancel''')

        signUpFrame.copyrightLabel = Label(signUpFrame)
        signUpFrame.copyrightLabel.place(relx=0.11, rely=0.92, height=24, width=242)
        signUpFrame.copyrightLabel.configure(text='''Made by 201411317 Cho MinKyu''')

        self.signUpFrame = signUpFrame
        self.mainView.signUpFrame = signUpFrame

    # Check whether ID was duplicated
    def chkID(self):
        # Get ID from Entry
        id = self.signUpFrame.IDEntry.get()

        # Send the Request to the Controller
        cFlag, msg = self.mainView.mc.eventHandler.signUpHandler.chkID(id)

        # Get the Message from Controller whether check request was succeeded
        if cFlag:
            self.signUpFrame.IDBool = True
            self.signUpFrame.id = id
            self.signUpFrame.moneyLabel.configure(text=msg)
        else:
            self.mainView.mc.showMessage('Check ID Error', msg)

    # Send Mail for Authorization
    def sendMail(self):
        # Get mail from Entry
        mail = self.signUpFrame.mailEntry.get()

        # Get the Message from Controller whether Authorization was succeeded
        mailFlag, msg = self.mainView.mc.eventHandler.signUpHandler.sendMail(mail)

        if mailFlag:
            self.signUpFrame.code = msg
            self.signUpFrame.mailBool = True
            self.signUpFrame.mail = mail
            self.signUpFrame.moneyLabel.configure(text='''Send mail Pass''')
        else:
            self.mainView.mc.showMessage('Send Mail Error', msg)

    # Sign Up Action for Button
    def signUp(self):
        name = self.signUpFrame.nameEntry.get()
        id = self.signUpFrame.IDEntry.get()
        pw = self.signUpFrame.PWEntry.get()
        pw2 = self.signUpFrame.PW2Entry.get()
        mail = self.signUpFrame.mailEntry.get()
        code = self.signUpFrame.codeEntry.get()

        # Send the Request to the Controller
        signUpFlag, msg = self.mainView.mc.eventHandler.signUpHandler.signUp(name, id, pw, pw2, mail, code,self.signUpFrame.IDBool,
                        self.signUpFrame.mailBool, self.signUpFrame.id, self.signUpFrame.mail, self.signUpFrame.code)

        # Get the Message from Controller whether Sign Up was succeeded
        if signUpFlag:
            self.mainView.mc.eventHandler.changeFrame(self.mainView.frameList['main'].mainFrame)
        else:
            self.mainView.mc.showMessage('Sign Up Error', msg)
            if msg == 'Please Check your ID':
                self.signUpFrame.IDBool = False
            elif msg == 'Please send mail and right code':
                self.signUpFrame.mailBool = False

    # Cancel Sign Up Action for Button
    def cancel(self):
        # Send the Request to the Controller
        cancelFlag = self.mainView.mc.eventHandler.signUpHandler.cancel()

        # Get the Message from Controller whether cancle was succeeded
        if cancelFlag:
            self.mainView.mc.eventHandler.changeFrame(self.mainView.frameList['login'].loginFrame)
            self.mainView.frameList['login'].loginFrame.IDEntry.delete(0, 'end')
            self.mainView.frameList['login'].loginFrame.PWEntry.delete(0, 'end')
            self.mainView.frameList['sign'].signUpFrame.nameEntry.delete(0, 'end')
            self.mainView.frameList['sign'].signUpFrame.IDEntry.delete(0, 'end')
            self.mainView.frameList['sign'].signUpFrame.PWEntry.delete(0, 'end')
            self.mainView.frameList['sign'].signUpFrame.PW2Entry.delete(0, 'end')
            self.mainView.frameList['sign'].signUpFrame.mailEntry.delete(0, 'end')
            self.mainView.frameList['sign'].signUpFrame.codeEntry.delete(0, 'end')
