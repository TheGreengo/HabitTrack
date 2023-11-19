from tkinter import *
import json
import datetime as dt

tracker = {}
entered = False

def loadTrack():
    file = open('tracking.json','r')
    return json.load(file)

def thang():
    print("called")

tracker = loadTrack()
title = tracker["habit title"]
start = dt.datetime(*tracker["start"])
end = dt.datetime(*tracker["end"])
goal = tracker["goal"]
period = (start - end).days
total = tracker["total"]
streak = tracker["streak"]
last = dt.datetime(*tracker["last"])
left = (end - dt.datetime.now()).days

displaystring = '''
So far you are %d days into your habit.
You still have %d days left to go.
Thusfar, you've had %d successes.
And you need %d more successess to reach your goal.
''' % (((dt.datetime.now() - start).days + 1),left, total, (goal - total))

enterstring = '''
You last updated this tracker {(dt.datetime.now() - last).days} days ago.
How many of those days were successes?
''' % ()

main = Tk()
main.title(f"{title} Tracker")
main.geometry("640x360")

lab = Label(master=main, text=displaystring)
lab.pack()

enter_statement = Label(master=main, text=enterstring)
enter_statement.pack()

new_days = IntVar()
new_days.set(0)
entry = Entry(master=main, textvariable=new_days)
entry.pack()

btn = Button(master=main, text="Update", command=thang)
btn.pack()

main.mainloop()