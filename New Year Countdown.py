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
    seconds=seconds.days*24*60*60+seconds.seconds
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    #print ("%d:%02d:%02d" % (h, m, s))
    lbl.config(bg='white')
    while h!=0 or m!=0 or s!=0:
        lbl["text"]=h,m,s
        time.sleep(1)
        window.update()
        s-=1
        if s==0 and m==0 and h==0:
            break
        if m==0 and s==0:
            h-=1
            m=59
            s=59
        if s==0:
            s=59
            m-=1

    lbl.config(bg="black",fg="#FFD700")
    lbl["text"]="Happy new year!"
window=tk.Tk()
window.title("Countdown timer")
window.geometry("980x660")
lbl=tk.Label(window,font=("Arial Bold",88),fg="black")
lbl.pack(fill='both',expand=1)
countDown()
window.mainloop()


