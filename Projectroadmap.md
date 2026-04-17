Phase 1: The Core Math (Logic)
- [ ] Create the Countdown: Write a function that takes a number of seconds and prints the countdown in your terminal.

- [ ] The "MM:SS" Converter: Use floor division (//) and modulo (%) to format seconds into minutes and seconds.

- [ ] The Break Switch: Write an if/else statement that switches between 1500 seconds (25 mins) and 300 seconds (5 mins).

Phase 2: The Window (GUI Skeleton)
- [ ] Import Tkinter: Start your script with import tkinter.

- [ ] Create the "Root": Setup the main window and give it a title like "FocusShift."

- [ ] Add the Timer Label: Create a large text label (e.g., Font: Arial, 50pt) that says "00:00."

- [ ] Add Buttons: Create a "Start" button and a "Reset" button.

- [ ] Layout: Use .grid() or .pack() to position the label and buttons so they look centered.

Phase 3: Making it Tick (The Connection)
- [ ] The Heartbeat: Use root.after(1000, function) to make your countdown run every second.

- [ ] Update the UI: Inside that function, use .config(text=new_time) to refresh the numbers on the screen.

- [ ] Global Timer Variable: Set up a variable to store the timer so you can "Cancel" it when the Reset button is pressed.

Phase 4: The Visuals (Polishing)
- [ ] Color Shifts: Add a line to change the background (bg) to Red when focusing and Green when resting.

- [ ] The Alarm: Use the winsound library (on Windows) to play a beep when the timer hits 00:00.

- [ ] Always on Top: Add root.attributes('-topmost', True) so the timer stays visible over your other windows while you study.\

Phase 5: The Log (Final Touch)
- [ ] Open the File: Use open("study_log.txt", "a") to prepare a text file.

- [ ] Write the Success: Every time a 25-minute session ends, automatically save a line like: "Session Completed: April 17, 4:30 PM".

- [ ] Close and Save: Ensure the file closes properly so your data isn't lost.
