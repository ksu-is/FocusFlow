import time
import tkinter as tk
from datetime import datetime

try:
    import winsound
except ImportError:
    winsound = None


# ----------------------------
# Phase 1: Core Math (Logic)
# ----------------------------
def format_mmss(total_seconds: int) -> str:
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes:02d}:{seconds:02d}"


def terminal_countdown(total_seconds: int) -> None:
    while total_seconds >= 0:
        print(f"\rTime left: {format_mmss(total_seconds)}", end="")
        time.sleep(1)
        total_seconds -= 1
    print()


def get_session_seconds(is_break: bool) -> int:
    if is_break:
        return 300
    return 1500


# ----------------------------
# Settings
# ----------------------------
FOCUS_SECONDS = get_session_seconds(is_break=False)
BREAK_SECONDS = get_session_seconds(is_break=True)
COLOR_FOCUS = "#B00020"
COLOR_BREAK = "#1B5E20"
LOG_FILE = "study_log.txt"

# ----------------------------
# Global timer state
# ----------------------------
timer_id = None
time_left = FOCUS_SECONDS
mode = "focus"  # "focus" or "break"


# ----------------------------
# Tkinter UI setup (create widgets FIRST)
# ----------------------------
root = tk.Tk()
root.title("FocusShift")
root.geometry("360x300")
root.attributes("-topmost", True)

mode_label = tk.Label(root, text="FOCUS", font=("Arial", 16, "bold"), fg="white")
mode_label.pack(pady=(20, 5))

timer_label = tk.Label(root, text="00:00", font=("Arial", 50, "bold"), fg="white")
timer_label.pack(pady=(0, 20))

buttons_frame = tk.Frame(root)
buttons_frame.pack()

start_button = tk.Button(buttons_frame, text="Start", font=("Arial", 14), width=10)
start_button.grid(row=0, column=0, padx=10)

reset_button = tk.Button(buttons_frame, text="Reset", font=("Arial", 14), width=10)
reset_button.grid(row=0, column=1, padx=10)

switch_button = tk.Button(buttons_frame, text="Switch", font=("Arial", 14), width=22)
switch_button.grid(row=1, column=0, columnspan=2, pady=(10, 0))


# ----------------------------
# Behavior (functions)
# ----------------------------
def set_mode(new_mode: str) -> None:
    global mode, time_left
    mode = new_mode

    if mode == "focus":
        bg = COLOR_FOCUS
        time_left = FOCUS_SECONDS
        mode_label.config(text="FOCUS")
    else:
        bg = COLOR_BREAK
        time_left = BREAK_SECONDS
        mode_label.config(text="BREAK")

    root.configure(bg=bg)
    mode_label.configure(bg=bg)
    timer_label.configure(bg=bg)
    buttons_frame.configure(bg=bg)

    timer_label.config(text=format_mmss(time_left))


def play_alarm() -> None:
    if winsound is not None:
        winsound.Beep(880, 250)
        winsound.Beep(880, 250)
    else:
        print("\a", end="")


def log_focus_completion() -> None:
    timestamp = datetime.now().strftime("%B %d, %I:%M %p")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"Session Completed: {timestamp}\n")


def refresh_time_label() -> None:
    timer_label.config(text=format_mmss(time_left))


def tick() -> None:
    global time_left, timer_id

    refresh_time_label()

    if time_left > 0:
        time_left -= 1
        timer_id = root.after(1000, tick)
        return

    timer_id = None
    play_alarm()

    if mode == "focus":
        log_focus_completion()
        set_mode("break")
    else:
        set_mode("focus")


def start_timer() -> None:
    global timer_id
    if timer_id is None:
        timer_id = root.after(0, tick)


def reset_timer() -> None:
    global timer_id
    if timer_id is not None:
        root.after_cancel(timer_id)
        timer_id = None
    set_mode("focus")


def switch_mode() -> None:
    global timer_id
    if timer_id is not None:
        root.after_cancel(timer_id)
        timer_id = None

    if mode == "focus":
        set_mode("break")
    else:
        set_mode("focus")


# Wire up button commands AFTER functions exist
start_button.config(command=start_timer)
reset_button.config(command=reset_timer)
switch_button.config(command=switch_mode)

# Initialize UI
set_mode("focus")

root.mainloop()