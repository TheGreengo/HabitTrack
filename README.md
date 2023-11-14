# HabitTrack
Little TKinter habit tracker

The hope here is to create a little habit tracking window with tkinter, where it creates/checks for a tracking.json file in the current directory. It then has a setting to check if it's a positive habit or a negative habit and displays:
- days remaining in goal
- days needed to meet goal
- habit title
- percentage success so far
- goal success percentage

# Form 
So, procedure-wise, here's what I'm thinking:

1. check if tracking.json exists
2. either read in dictionary or create one and init tracking.json
3. calculate: success rate, days since last reported, days needed
4. set title, set fields, etc.

Then there should be a simple prompt and field which says: "It's been _ days since you last recorded your progress. How many of the last _ day(s) have been successes?"

Followed by a field to input the correct number of days. When the button is pressed, the days entered should be validated, and then the form updated.

It should also check and see if that day has already been recorded and, if it has, just display the current status.
