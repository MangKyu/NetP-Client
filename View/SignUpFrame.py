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
        myFont=('08서울남산체 M', 12)
        signUpFrame = Frame(root)
        signUpFrame.place(relx=0.00, rely=0.00, relheight=1.00, relwidth=1.00)
        signUpFrame.configure(relief=GROOVE)
        signUpFrame.configure(width=265)

        signUpFrame.bgLabel = Label(signUpFrame)
        signUpFrame.bgLabel.place(x=0, y=0, relwidth=1, relheight=1)
        signUpFrame.bgImage = PhotoImage(file = "../View/Pictures/SignUpFrame/background.png")
        signUpFrame.bgLabel.configure(image=signUpFrame.bgImage)

        signUpFrame.nameEntry = Entry(signUpFrame)
        signUpFrame.nameEntry.place(relx=0.35, rely=0.2, relheight=0.048, relwidth=0.4)
        signUpFrame.nameEntry.configure(bg='#547296', fg='white', font=myFont)

        signUpFrame.IDBool = False
        signUpFrame.id = ''

        signUpFrame.IDEntry = Entry(signUpFrame)
        signUpFrame.IDEntry.place(relx=0.35, rely=0.288, relheight=0.048, relwidth=0.4)
        signUpFrame.IDEntry.configure(bg='#547296', fg='white', font=myFont)

        signUpFrame.checkButton = Label(signUpFrame)
        signUpFrame.checkButton.place(relx=0.775, rely=0.288, relheight=0.048, relwidth=0.15)
        signUpFrame.checkButton.bind('<Button-1>', self.chkID)
        signUpFrame.checkButton.configure(text='''Chk''', bg='#597fab', fg='white', font=myFont)

        signUpFrame.PWEntry = Entry(signUpFrame, show='*')
        signUpFrame.PWEntry.place(relx=0.35, rely=0.375, relheight=0.048, relwidth=0.4)
        signUpFrame.PWEntry.configure(bg='#547296', fg='white', font=myFont)

        signUpFrame.PW2Entry = Entry(signUpFrame, show='*')
        signUpFrame.PW2Entry.place(relx=0.35, rely=0.46, relheight=0.048, relwidth=0.4)
        signUpFrame.PW2Entry.configure(bg='#547296', fg='white', font=myFont)

        signUpFrame.mailBool = False
        signUpFrame.mail = ''

        signUpFrame.mailEntry = Entry(signUpFrame)
        signUpFrame.mailEntry.place(relx=0.35, rely=0.546, relheight=0.048, relwidth=0.4)
        signUpFrame.mailEntry.configure(bg='#547296', fg='white', font=myFont)

        signUpFrame.sendButton = Label(signUpFrame)
        signUpFrame.sendButton.place(relx=0.77, rely=0.546, relheight=0.048, relwidth=0.15)
        signUpFrame.sendButton.configure(text='''Send''', bg='#586f8a', fg='white', font=myFont)
        signUpFrame.sendButton.bind('<Button-1>', self.sendMail)

        signUpFrame.code = ''
        signUpFrame.codeEntry = Entry(signUpFrame)
        signUpFrame.codeEntry.place(relx=0.35, rely=0.632, relheight=0.048, relwidth=0.4)
        signUpFrame.codeEntry.configure(bg='#547296', fg='white', font=myFont)

        signUpFrame.moneyLabel = Label(signUpFrame)
        signUpFrame.moneyLabel.place(relx=0.07, rely=0.725, relheight=0.052, relwidth=0.867)
        signUpFrame.moneyLabel.configure(bg='#556180', text='''At First, You have [ 0 won ] in your account''', fg='white', font=('08서울남산체 M', 10))

        signUpFrame.signUpButton = Label(signUpFrame)
        signUpFrame.signUpButton.place(relx=0.07, rely=0.805, relheight=0.07, relwidth=0.4)
        signUpFrame.signUpButton.bind('<Button-1>', self.signUp)
        signUpFrame.signUpButton.configure(bg='#556180', text='''Sign-Up''', fg='white', font=myFont)

        signUpFrame.cancelButton = Label(signUpFrame)
        signUpFrame.cancelButton.place(relx=0.541, rely=0.805, relheight=0.07, relwidth=0.4)
        signUpFrame.cancelButton.bind('<Button-1>', self.cancel)
        signUpFrame.cancelButton.configure(bg='#556180', text='''Cancel''', fg='white', font=myFont)

        signUpFrame.copyrightLabel = Label(signUpFrame)
        signUpFrame.copyrightLabel.place(relx=0.11, rely=0.92, height=24, width=242)
        signUpFrame.copyrightLabel.configure(bg='#15183b', fg='white', text='''Made by 201411317 Cho MinKyu''', font=('08서울남산체 M', 10))

        self.signUpFrame = signUpFrame
        self.mainView.signUpFrame = signUpFrame

    # Check whether ID was duplicated
    def chkID(self, *event):
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
    def sendMail(self, *event):
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
    def signUp(self, *event):
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
    def cancel(self, *event):
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
