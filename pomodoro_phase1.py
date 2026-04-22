import time


def format_mmss(total_seconds: int) -> str:
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes:02d}:{seconds:02d}"


def run_countdown(total_seconds: int) -> None:
    while total_seconds >= 0:
        print(f"\rTime left: {format_mmss(total_seconds)}", end="")
        time.sleep(1)
        total_seconds -= 1
    print()


def get_session_seconds(is_break: bool) -> int:
    if is_break:
        return 300   # 5 min
    else:
        return 1500  # 25 min


if __name__ == "__main__":
    print("Starting Focus Session...")
    run_countdown(get_session_seconds(is_break=False))

    print("Break Time!")
    run_countdown(get_session_seconds(is_break=True))

    print("Cycle complete.")