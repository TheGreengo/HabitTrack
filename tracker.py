from tkinter import *
import json
import os.path
import datetime as dt

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
    start = dt.datetime(*tracker["start"])
    end = dt.datetime(*tracker["end"])
    goal = tracker["goal"]
    period = (start - end).days
    total = tracker["total"]
    streak = tracker["streak"]
    last = dt.datetime(*tracker["last"])
    left = (end - dt.datetime.now()).days

    main = Tk()
    main.title(f"{title} Tracker")
    main.geometry("640x360")

    days_in = Label(main, text=f"So far you are {(dt.datetime.now() - start).days + 1} days into your habit.")
    days_in.pack()
    days_left = Label(main, text=f"You still have {left} days left to go.")
    days_left.pack()
    successes = Label(main, text=f"Thusfar, you've had {total} successes.")
    successes.pack()
    successes_left = Label(main, text=f"And you need {goal - total} more successess to reach your goal.")
    successes_left.pack()

    if last.day != dt.datetime.now().day:
        enter_statement = Label(main, text=f"You last updated this tracker {(dt.datetime.now() - last).days} days ago")
        enter_statement.pack()
        other = Label(main, text="How many of those days were successes?")
        other.pack()
        new_days = IntVar()
        entry = Entry(main, textvariable=new_days)
        entry.pack()

        def update():
            tracker["total"] += new_days.get()
            enter_statement.destroy()
            other.destroy()

    main.mainloop()