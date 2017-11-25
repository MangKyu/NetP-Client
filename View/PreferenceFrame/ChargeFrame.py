try:
    from Tkinter import *
except ImportError:
    from tkinter import *

class ChargeFrame:
    mainView = None

    # Create Frame for Charge Money
    def __init__(self, mainView):
        self.mainView = mainView
        self.main = Tk()
        self.main.title('Authentication Box')
        self.main.geometry('225x150')

        self.moneyLabel = Label(self.main, font=('08서울남산체 M', 12))
        self.moneyLabel.configure(text=''' Money : ''')
        self.moneyLabel.place(relx=0.01, rely=0.34)

        self.moneyEntry = Entry(self.main)
        self.moneyEntry.place(relx=0.33, rely=0.3,height =30)

        # adds changePW button and defines its properties
        self.chargeButton = Button(self.main, text='Charge Money', command=self.chargeMoney)
        self.chargeButton.bind('<Return>', self.chargeMoney)
        self.chargeButton.place(relx=0.27, rely=0.7, height=40, width=100)
        self.main.lift()
        self.main.mainloop()

    # Charge Money Action for Button
    def chargeMoney(self, *event):
        # Get Money for charge from Entry
        money = self.moneyEntry.get()

        # Send the Request to the Controller
        chargeFlag, msg = self.mainView.mc.eventHandler.settingHandler.chargeMoney(money)

        # Get the Message from Controller whether Charge Money was succeeded
        if chargeFlag:
            self.mainView.mc.eventHandler.changeFrame(self.mainView.frameList['main'].mainFrame)
            self.main.destroy()
            self.mainView.mc.showMessage('Charge Money Complete', msg)
        else:
            self.mainView.mc.showMessage('Charge Money Error', msg)
