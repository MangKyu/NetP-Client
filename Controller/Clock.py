import threading
import datetime
import time

class Clock(threading.Thread):
    sem = None
    tFlag = True
    sFlag = True
    roomFrame = None
    # Constructor for Room Thread
    def __init__(self, roomFrame):
        threading.Thread.__init__(self)
        self.tFlag = True
        self.roomFrame = roomFrame
        self.sem = threading.Semaphore(0)
        self.sFlag = False

    # Count time for auction time
    def run(self):
        while self.tFlag:

            now = datetime.datetime.now()
            curTime = now.strftime('%Y-%m-%d %H:%M:%S')
            self.roomFrame.roomFrame.curT.configure(text=curTime)
            time.sleep(1)
            if self.sFlag:
                self.sem.acquire()
        print('Clock Thread exit!')
