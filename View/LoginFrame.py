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

        myFont = ('08서울남산체 M', 16)

        loginFrame = Frame(root)
        loginFrame.place(relx=0.00, rely=0.00, relheight=1.00, relwidth=1.00)
        loginFrame.configure(relief=GROOVE)
        loginFrame.configure(width=265)

        loginFrame.bgLabel = Label(loginFrame)
        loginFrame.bgLabel.place(x=0, y=0, relwidth=1, relheight=1)
        loginFrame.bgImage = PhotoImage(file = "../View/Pictures/LoginFrame/background.png")
        loginFrame.bgLabel.configure(image=loginFrame.bgImage)

        loginFrame.IDEntry = Entry(loginFrame, bg = "#1c4478", fg="white")
        loginFrame.IDEntry.place(relx=0.328, rely=0.462, relheight=0.06, relwidth=0.59)
        loginFrame.IDEntry.insert(0, 'Enter Username')
        loginFrame.IDEntry.bind("<FocusIn>", self.clearEntry)
        loginFrame.IDEntry.bind('<FocusOut>', self.repopulateEntry)

        loginFrame.PWEntry = Entry(loginFrame, show='*', bg = "#1c4478", fg="white")
        loginFrame.PWEntry.place(relx=0.328, rely=0.54, relheight=0.06, relwidth=0.59)
        loginFrame.PWEntry.insert(0, '     ')
        loginFrame.PWEntry.bind("<FocusIn>", self.clearEntry)
        loginFrame.PWEntry.bind('<FocusOut>', self.repopulateEntry)

        loginFrame.loginButton = Label(loginFrame)
        loginFrame.loginButton.place(relx=0.12, rely=0.687, relheight=0.09, relwidth=0.7)
        loginFrame.loginButton.configure(bg='#556180', text='Login', fg='white', font=myFont)
        loginFrame.loginButton.bind('<Button-1>', self.login)

        loginFrame.signUpButton = Label(loginFrame)
        loginFrame.signUpButton.place(relx=0.12, rely=0.825, relheight=0.09, relwidth=0.7)
        loginFrame.signUpButton.configure(bg='#556180', text='Sign-Up', fg='white', font=myFont)
        loginFrame.signUpButton.bind('<Button-1>', self.signUp)

        loginFrame.copyrightLabel = Label(loginFrame)
        loginFrame.copyrightLabel.place(relx=0.05, rely=0.93, relheight=0.04, relwidth=0.9)
        loginFrame.copyrightLabel.configure(bg='#15183b', fg='white', text='''CopyRight by 201411317 Cho MinKyu''', font=('08서울남산체 M', 10))
        self.loginFrame = loginFrame
        self.mainView.loginFrame = loginFrame

    # Login Action for Button
    def login(self, event):
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

    def signUp(self, event):
        self.mainView.mc.eventHandler.changeFrame(self.mainView.frameList['sign'].signUpFrame)