try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from PIL import ImageTk, Image
class ImageFrame:
    mainView = None

    # Create Frame for Change Password
    def __init__(self, mainView, path):
        self.mainView = mainView
        self.main = Toplevel()#Tk()
        self.main.title('Authentication Box')
        #self.main.geometry('225x150')
        bgImg = Image.open(path)
        x, y = bgImg.size
        path = '../Controller/'+path
        if x > 900:
            x = 900
        elif y > 600:
            y = 600
        size = str(x)+'x'+str(y)

        self.main.geometry(size)

        self.imgLabel= Label(self.main)
        img = Image.open(path)
        img = img.resize((x, y), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self._img1 = img
        self.imgLabel.configure(image=self._img1)
        self.imgLabel.place(x=0, y=0, relwidth=1, relheight=1)
        self.imgLabel.bind('<Button-1>', self.exit)
        self.main.lift()
        self.main.mainloop()

    def exit(self, *event):
        self.main.destroy()
