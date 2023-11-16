from tkinter import *
import json
import os.path
import datetime as dt

'''
Todos:
- 
'''
tracker_made = os.path.isfile('./tracking.json')
tracker = {}
is_new = False

if not tracker_made:
    unprep = Tk()
    unprep.title("Habit Tracker")
    label = Label(
        unprep,
        '''
        Error: tracking.json file expected.
        In order to use the tracker, please create a tracking.json
        file in the same directory as the tracker.py script
        and give it the following fields:
        - "habit title"
        - "start"
        - "end"
        - "goal"
        - "total"
        - "streak"
        - "last"
        '''
        )
    label.pack()
    unprep.geometry("640x360")
    unprep.mainloop()
else:
    with open('tracking.json', 'r') as openfile:
        tracker = json.load(openfile)

    title = tracker["habit title"]
    start = dt.datetime(tracker["start"])
    end = dt.datetime(tracker["end"])
    goal = tracker["goal"]
    period = (start - end).days
    total = tracker["total"]
    streak = tracker["streak"]
    last = dt.datetime(tracker["last"])

    main = Tk()
    main.title(f"{title} Tracker")
    main.geometry("640x360")

    days_in = Label(main, "So far you are {} days into your habit.")
    days_in.pack()
    days_left = Label(main, "You still have {} days left to go.")
    days_left.pack()
    successes = Label(main, "Thusfar, you've had {} successes.")
    successes.pack()
    successes_left = Label(main, "And you need {} more successess to reach your goal.")
    successes_left.pack()

    if last.day != dt.datetime.now().day:
        enter_statement = Label()
    main.mainloop()