import tkinter
import tkinter as tk
import threading
import time


class Timer:

    def __init__(self):
        self.imp=tk.Tk()
        self.imp.geometry("500x300")
        self.imp.config(bg="cyan")
        self.imp.title("Count Down")
        self.hours=0
        self.minutes=0
        self.seconds=0
        self.label1=tk.Label(self.imp,font=20,text="Enter the count down time")
        self.label1.grid(row=0,column=0,columnspan=10,padx=105,pady=10)
        self.text=tk.Entry(self.imp,font=20)
        self.text.grid(row=1,column=0,columnspan=10,padx=105,pady=15)
        self.start=tk.Button(self.imp,font=20,text="START",command=self.start_thread,activebackground="green")
        self.start.place(x=150,y=150)
        self.stop = tk.Button(self.imp, font=20, text="RESET",command=self.reset,activebackground="red")
        self.stop.place(x=250, y=150)
        self.pause = tk.Button(self.imp, font=20, text="PAUSE",command=self.time_pause,activebackground="blue")
        self.pause.place(x=150, y=195)
        self.resume = tk.Button(self.imp, font=20, text="RESUME",command=self.time_resume,activebackground="yellow")
        self.resume.place(x=250, y=195)
        self.timelabel=tk.Label(self.imp,font=('Arial',15),text="Time=00:00:00 ")
        self.timelabel.place(x=150,y=105)
        ##elf.timeup=tk.Label(self.root,font=40,text=" ")
        ##self.timeup.grid()
        self.pause=False
        self.stop_lopp=False
        self.imp.mainloop()

    def start_thread(self):
        t=threading.Thread(target=self.start_timer)
        t.start()

    def start_timer(self):
        self.stop_loop=False
        time_split=self.text.get().split(":")
        if len(time_split)==3:
            self.hours=int(time_split[0])
            self.minutes = int(time_split[1])
            self.seconds = int(time_split[2])
        elif len(time_split)==2:
            self.minutes = int(time_split[0])
            self.seconds = int(time_split[1])
        elif len(time_split)==1:
            self.seconds=int(time_split[0])
        else:
            print("INVALID TIME FORMAT....")
            return

        self.full_seconds=self.hours * 3600 + self.minutes * 60 +self.seconds
        while self.full_seconds > 0 and not self.stop_loop:
            self.full_seconds=self.full_seconds-1
            self.minutes,self.seconds=divmod(self.full_seconds,60)
            self.hours,self.minutes=divmod(self.minutes,60)
            self.timelabel.config(text=f"Time {self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")
            self.imp.update()
            time.sleep(1)
        self.imp.update()

    def time_pause(self):
        self.pause=True
        self.stop_loop=True
        self.hours=self.hours
        self.minutes=self.minutes
        self.seconds=self.seconds
        self.timelabel.config(text=f"Time  {self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")
        self.timelabel.update()

    def time_resume(self):
        self.pause=False
        self.stop_loop=False
        while self.full_seconds > 0 and not self.stop_loop:
            self.full_seconds=self.full_seconds-1
            self.minutes,self.seconds=divmod(self.full_seconds,60)
            self.hours, self.minutes= divmod(self.minutes, 60)
            self.timelabel.config(text=f"Time  {self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")
            self.imp.update()
            time.sleep(1)

    def reset(self):
        self.stop_loop=True
        self.timelabel.config(text="Time:00:00:00")
        self.imp.update()




Timer()






