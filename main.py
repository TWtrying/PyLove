#coding:utf-8

from tkinter import Tk,Label
from ctypes import windll
from threading import Thread
from random import randint
from math import sqrt

class Pywin:
    SCW = None
    SCH = None
    SF = None
    R = None
    STOP = None

    def __init__(self,sw,sh) -> None:
        self.SCH = sh//2-40
        self.SCW = sw//2-155
        self.R = self.SCH*2//4
        windll.shcore.SetProcessDpiAwareness(1)
        self.SF=windll.shcore.GetScaleFactorForDevice(0)

    def win(self):
        win = Tk()
        win.title('Love')
        win.tk.call('tk', 'scaling', self.SF/75)
        win.geometry('310x80+'+self.cy())
        Label(win,text="♥",font=('楷体',32),fg='red').grid(column=0,row=0)
        Label(win,text="爱你哟",font=('楷体',32)).grid(column=1,row=0)
        Label(win,text="♥",font=('楷体',32),fg='red').grid(column=4,row=0)
        win.after(5000,win.destroy)
        win.mainloop()


    def cy(self) -> str:
        x = randint(-2*self.R,2*self.R)
        if x==0 :
            a = randint(1,100)
            if a != 1:
                return str(self.SCW)+'+'+str(int(self.SCH+a-0.5*self.R//1+200))
            return str(self.SCW)+'+'+str(self.SCH+1.5*self.R//1+200)
            
        if randint(1,2) == 1:
            return str(self.SCW+x)+'+'+str(int(self.R-sqrt(self.R**2-((x if x>0 else x*-1)-self.R)**2)//1+200))
        else:
            return str(self.SCW+x)+'+'+str(int(self.R+sqrt(4*(self.R**2)-x**2)//1+200))
    
    
    def display(self,n):
        for i in range(n):
            Thread(target=self.win).start()


def readconfig():
    try:
        f = open("config",'r')
    except :
        print("配置文件无法打开")
    else:
        w = int(f.readline()[:-1])
        h = int(f.readline())
        return w,h

w,h = readconfig()
a = Pywin(w,h)
a.display(200)