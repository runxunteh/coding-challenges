"""
This program can be used for 2019 New Year Countdown
Besides that, the date and time can be changed anytime for other purposes such as
timer for the boiling egg
"""
#Tkinter is a GUI library for python

import tkinter as tk
from datetime import datetime
import time
def countDown():
    target=datetime.strptime('2019-01-01 00:00:00','%Y-%m-%d %H:%M:%S')
    now=datetime.now()
    seconds=target-now
    #convert to all seconds
    seconds=seconds.days*24*60*60+seconds.seconds
    lbl.config(bg='white')
    for i in range(seconds,-1,-1):
        lbl["text"]=i
        time.sleep(1)
        window.update()
    lbl.config(bg='white')
    lbl["text"]="Happy new year!"
window=tk.Tk()
window.title("Countdown timer")
window.geometry("1920x1080")
lbl=tk.Label(window, font=("Arial Bold",88))
lbl.pack(fill='both',expand=1)
countDown()
window.mainloop()





