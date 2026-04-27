import tkinter as tk


# ----------------------------
# Root window
# ----------------------------
root = tk.Tk()
root.title("FocusShift")
root.geometry("360x240")
root.configure(bg="#1E1E1E")  # dark background
root.attributes("-topmost", True)  # always on top (optional)


# ----------------------------
# Timer label
# ----------------------------
timer_label = tk.Label(
    root,
    text="00:00",
    font=("Arial", 50, "bold"),
    fg="white",
    bg="#1E1E1E"
)
timer_label.pack(pady=(30, 20))


# ----------------------------
# Button actions
# ----------------------------
def start_timer():
    print("Start clicked")  # placeholder for real countdown logic


def reset_timer():
    timer_label.config(text="00:00")
    print("Reset clicked")


# ----------------------------
# Buttons
# ----------------------------
buttons_frame = tk.Frame(root, bg="#1E1E1E")
buttons_frame.pack()

start_button = tk.Button(
    buttons_frame,
    text="Start",
    font=("Arial", 14),
    width=10,
    command=start_timer
)
start_button.grid(row=0, column=0, padx=10)

reset_button = tk.Button(
    buttons_frame,
    text="Reset",
    font=("Arial", 14),
    width=10,
    command=reset_timer
)
reset_button.grid(row=0, column=1, padx=10)


# ----------------------------
# Run app
# ----------------------------
root.mainloop()