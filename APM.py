from tkinter import *
import tkinter.messagebox
import random
import time


global R
R = 10

class APM:
    def __init__(self, main_window):
        self.status = False
        self.frame0 = Frame(main_window)
        self.frame1 = Frame(main_window)
        self.frame2 = Frame(main_window)
        self.cv = Canvas(self.frame0, width=800, height=600)
        self.bt1 = Button(self.frame1,
                         text='Start',
                         command=self.start)
        self.bt2 = Button(self.frame1,
                          text='End',
                          command=self.end)
        self.__apm = StringVar()
        self.__t = StringVar()
        self.__apm.set('0/0')
        self.rs = Label(self.frame2,
                        textvariable=self.__apm)
        self.tr = Label(self.frame2,
                        textvariable=self.__t)
        self.cv.pack()
        self.frame0.pack()
        self.bt1.pack(side='left')
        self.bt2.pack(side='left')
        self.frame1.pack()
        self.rs.pack(side='left')
        self.tr.pack(side='left')
        self.frame2.pack()

    def start(self):
        self.status = True
        self.__apm.set('0/0')
        self.ecount = 0
        self.count = 0
        self.time = time.time()
        self.tt()
        self.cx = random.randint(50, 750)
        self.cy = random.randint(50, 550)
        self.cv.destroy()
        self.cv = Canvas(self.frame0, width=800, height=600)
        self.d = self.cv.create_oval((self.cx-R, self.cy-R, self.cx+R, self.cy+R), fill='black')
        
        self.cv.bind('<Button-1>', self.change)
        self.cv.pack()


    def tt(self):
        t = time.time()
        self.__t.set(str('%.2f' %(t-self.time)))
        if self.status and t-self.time < 60:
            self.frame2.after(10, self.tt)
        else:
            self.status = False
            tkinter.messagebox.showinfo('Information',
                                        'APM: '+str(int(self.count/((t-self.time)/60)))+'\n'
                                        +'EAPM: '+str(int(self.ecount/((t-self.time)/60))))


    def end(self):
        self.status = False
        self.cv.destroy()

    def change(self,event):
        if self.status:
            if abs(self.cx-event.x) <= R and abs(self.cy-event.y) <= R:
                self.ecount += 1
                self.cx = random.randint(50, 750)
                self.cy = random.randint(50, 550)
                self.__apm.set(str(self.count))
                self.cv.coords(self.d, (self.cx-R, self.cy-R, self.cx+R, self.cy+R))
            self.count += 1
            self.__apm.set(str(self.ecount)+'/'+str(self.count))

win = Tk()
APM(win)
win.mainloop()