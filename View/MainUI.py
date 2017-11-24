from Controller import MainController
from View import MainFrame, LoginFrame, SignUpFrame, SettingFrame, SellingFrame, RoomFrame, WatchlistFrame

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

class MainUI:
    root = None
    frameList = None
    mc = None

    # Create Basis of Graphic User Interface
    def __init__(self):
        self.root = Tk()
        self.root.resizable(width=False, height=False)

        self.root.geometry("300x500")
        self.root.title("What is Title")
        self.root.configure(background="black")
        self.mc = MainController.MainController()
        frameList = {
                    'sign': SignUpFrame.SignUpFrame(self, self.root),
                    'main': MainFrame.MainFrame(self, self.root),
                    'selling': SellingFrame.SellingFrame(self, self.root),
                    'setting': SettingFrame.SettingFrame(self, self.root),
                    'login': LoginFrame.LoginFrame(self, self.root),
                    'room': RoomFrame.RoomFrame(self, self.root),
                    'watch': WatchlistFrame.WatchlistFrame(self, self.root)
                     }

        self.mc.createHandler(frameList)
#        self.mc.eventHandler['room'].clock.sem.acquire()
        # Set the Frame for LoginFrame
        self.mc.eventHandler.changeFrame(self.mc.frameList['login'].loginFrame)
        self.frameList = frameList
        self.root.mainloop()
        self.quit()

    # Quit and Destroy Resources
    def quit(self):
        self.mc.exit()
