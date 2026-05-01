import time
import tkinter as tk
from datetime import datetime

# winsound is Windows-only; keep app working on Mac/Linux too
try:
    import winsound
except ImportError:
    winsound = None


# ----------------------------
# Phase 1: Core Math (Logic)
# ----------------------------
def format_mmss(total_seconds: int) -> str:
    """Convert seconds to MM:SS using // and %."""
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes:02d}:{seconds:02d}"


def terminal_countdown(total_seconds: int) -> None:
    """Print a countdown in the terminal (Phase 1 checklist item)."""
    while total_seconds >= 0:
        print(f"\rTime left: {format_mmss(total_seconds)}", end="")
        time.sleep(1)
        total_seconds -= 1
    print()  # newline when done


def get_session_seconds(is_break: bool) -> int:
    """Break switch (1500 focus vs 300 break)."""
    if is_break:
        return 300   # 5 min
    return 1500      # 25 min


# ----------------------------
# Phase 2-5: Tkinter App
# ----------------------------
FOCUS_SECONDS = get_session_seconds(is_break=False)
BREAK_SECONDS = get_session_seconds(is_break=True)

COLOR_FOCUS = "#B00020"  # red
COLOR_BREAK = "#1B5E20"  # green

LOG_FILE = "study_log.txt"

timer_id = None          # Phase 3: global timer variable for after_cancel
time_left = FOCUS_SECONDS
mode = "focus"           # "focus" or "break"


def set_mode(new_mode: str) -> None:
    """Phase 4: Color shifts based on state."""
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
    """Phase 4: Alarm on 00:00."""
    if winsound is not None:
        winsound.Beep(880, 250)
        winsound.Beep(880, 250)
    else:
        # fallback (may not beep depending on terminal)
        print("\a", end="")


def log_focus_completion() -> None:
    """Phase 5: Append a completed focus session line to the log file."""
    timestamp = datetime.now().strftime("%B %d, %I:%M %p")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"Session Completed: {timestamp}\n")


def refresh_time_label() -> None:
    """Phase 3: update UI with .config(text=...)."""
    timer_label.config(text=format_mmss(time_left))


def tick() -> None:
    """Phase 3: Heartbeat using root.after(1000, ...)."""
    global time_left, timer_id

    refresh_time_label()

    if time_left > 0:
        time_left -= 1
        timer_id = root.after(1000, tick)
        return

    # Hit 00:00
    timer_id = None
    play_alarm()

    if mode == "focus":
        log_focus_completion()
        set_mode("break")
    else:
        set_mode("focus")


def start_timer() -> None:
    """Start countdown if not already running (prevents double timers)."""
    global timer_id
    if timer_id is None:
        timer_id = root.after(0, tick)


def reset_timer() -> None:
    """Cancel timer and reset back to focus mode."""
    global timer_id
    if timer_id is not None:
        root.after_cancel(timer_id)
        timer_id = None
    set_mode("focus")


# ----------------------------
# Phase 2: GUI Skeleton
# ----------------------------
root = tk.Tk()
root.title("FocusShift")
root.geometry("360x260")
root.attributes("-topmost", True)  # Phase 4: Always on Top

mode_label = tk.Label(
    root,
    text="FOCUS",
    font=("Arial", 16, "bold"),
    fg="white"
)
mode_label.pack(pady=(20, 5))

timer_label = tk.Label(
    root,
    text="00:00",
    font=("Arial", 50, "bold"),
    fg="white"
)
timer_label.pack(pady=(0, 20))

buttons_frame = tk.Frame(root)
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

# Initialize to focus theme + 25:00
set_mode("focus")

root.mainloop()