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
        - "period"
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

    creating = Tk()
    creating.title("Habit Tracker")
    creating.geometry("640x360")
    creating.mainloop()