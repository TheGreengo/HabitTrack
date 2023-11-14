from tkinter import *
import json

# Opening JSON file
with open('tracking.json', 'r') as openfile:
    json_object = json.load(openfile)

root = Tk()
root.title("Habit Tracker")
root.geometry("640x360")

root.mainloop()