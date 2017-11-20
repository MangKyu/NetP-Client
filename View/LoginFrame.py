try:
    from Tkinter import *
except ImportError:
    from tkinter import *

class LoginFrame:
    mainView = None
    loginFrame = None

    # Create Frame for Login
    def __init__(self, mainView, root):
        self.root = root
        self.mainView = mainView

        loginFrame = Frame(root)
        loginFrame.place(relx=0.00, rely=0.00, relheight=1.00, relwidth=1.00)
        loginFrame.configure(relief=GROOVE)
        loginFrame.configure(width=265)

        loginFrame.imageLabel = Label(loginFrame)
        loginFrame.imageLabel.place(relx=0.18, rely=0.13, height=129, width=191)
        loginFrame._img1 = PhotoImage(file='../View/Pictures/LoginFrame/logo.png')
        loginFrame.imageLabel.configure(image=loginFrame._img1)

        loginFrame.IDLabel = Label(loginFrame)
        loginFrame.IDLabel.place(relx=0.02, rely=0.50, height=34, width=37)
        loginFrame.IDLabel.configure(text='''ID   :''')

        loginFrame.IDEntry = Entry(loginFrame)
        loginFrame.IDEntry.place(relx=0.2, rely=0.50, relheight=0.08, relwidth=0.70)
        loginFrame.IDEntry.insert(0, 'Enter Username')
        loginFrame.IDEntry.bind("<FocusIn>", self.clearEntry)
        loginFrame.IDEntry.bind('<FocusOut>', self.repopulateEntry)

        loginFrame.PWLabel = Label(loginFrame)
        loginFrame.PWLabel.place(relx=0.02, rely=0.605, height=34, width=37)
        loginFrame.PWLabel.configure(text='''PW  :''')

        loginFrame.PWEntry = Entry(loginFrame, show='*')
        loginFrame.PWEntry.place(relx=0.2, rely=0.60, relheight=0.08, relwidth=0.70)
        loginFrame.PWEntry.insert(0, '     ')
        loginFrame.PWEntry.bind("<FocusIn>", self.clearEntry)
        loginFrame.PWEntry.bind('<FocusOut>', self.repopulateEntry)

        loginFrame.loginButton = Button(loginFrame, command=self.login)
        loginFrame.loginButton.place(relx=0.07, rely=0.76, height=52, width=109)
        loginFrame.loginButton.configure(text='''Login''')

        loginFrame.signUpButton = Button(loginFrame, command=lambda: self.mainView.mc.eventHandler.changeFrame(
            self.mainView.frameList['sign'].signUpFrame))
        loginFrame.signUpButton.place(relx=0.53, rely=0.76, height=52, width=109)
        loginFrame.signUpButton.configure(text='''Sign-Up''')

        loginFrame.copyrightLabel = Label(loginFrame)
        loginFrame.copyrightLabel.place(relx=0.08, rely=0.92, height=24, width=242)
        loginFrame.copyrightLabel.configure(text='''CopyRight by 201411317 Cho MinKyu''')
        self.loginFrame = loginFrame
        self.mainView.loginFrame = loginFrame

    # Login Action for Button
    def login(self):
        # Get id, pw from Entry
        id = self.loginFrame.IDEntry.get()
        pw = self.loginFrame.PWEntry.get()

        # Send the Request to the Controller
        loginFlag, msg = self.mainView.mc.eventHandler.loginHandler.login(id, pw)

        # Get the Message from Controller whether Login was succeeded
        if loginFlag:
            self.mainView.mc.eventHandler.changeFrame(self.mainView.frameList['main'].mainFrame)
        else:
            self.mainView.mc.showMessage('Login Error', msg)

    def clearEntry(self, event):
        # will clear out any entry boxes defined below when the user shifts
        # focus to the widgets defined below
        if self.loginFrame.IDEntry == self.loginFrame.focus_get() and self.loginFrame.IDEntry.get() == 'Enter Username':
            self.loginFrame.IDEntry.delete(0, END)
        elif self.loginFrame.PWEntry == self.loginFrame.PWEntry.focus_get() and self.loginFrame.PWEntry.get() == '     ':
            self.loginFrame.PWEntry.delete(0, END)

    def repopulateEntry(self, event):
        # will repopulate the default text previously inside the entry boxes defined below if
        # the user does not put anything in while focused and changes focus to another widget
        if self.loginFrame.IDEntry != self.loginFrame.focus_get() and self.loginFrame.IDEntry.get() == '':
            self.loginFrame.IDEntry.insert(0, 'Enter Username')
        elif self.loginFrame.PWEntry != self.loginFrame.focus_get() and self.loginFrame.PWEntry.get() == '':
            self.loginFrame.PWEntry.insert(0, '     ')