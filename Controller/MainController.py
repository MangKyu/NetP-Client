from Controller import Client, EventHandler, AdminRoom
from Model import User
from PIL import ImageTk, Image
from tkinter.messagebox import showinfo
import threading

# Main Controller to access Controller package
class MainController:
    client = None
    user = None
    eventHandler = None
    frameList = None
    adminRoom = None

    # Constructor for Main Controller instance
    def __init__(self):
        self.user = User.User()
        #self.adminRoom = AdminRoom.AdminRoom(self.user)
        self.adminRoom = AdminRoom.AdminRoom()

    # Exit
    def exit(self):
        self.client.exit()

    # create event handler and client
    def createHandler(self, frameList):
        self.frameList = frameList
        self.client = Client.Client(self.user, self.eventHandler, self.adminRoom)
        self.eventHandler = EventHandler.EventHandler(self.client, frameList)
        self.client.eventHandler = self.eventHandler

    # Open Image
    def openPhotoImage(self, path):
        img = Image.open(path)
        img = ImageTk.PhotoImage(img)
        return img

    # Create simple thread for message box
    def showMessage(self, title, msg):
        t = threading.Thread(target=self.createMessage, args=(title, msg))
        t.start()

    # Create Message Box
    def createMessage(self, title, msg):
        showinfo(title, msg)
