import json
import os
import time
from datetime import datetime

POMODORO_FILE = os.path.join("data", "pomodoro.json")
WORK_TIME = 25 * 60  # 25 minutes


def load_sessions():
    if not os.path.exists(POMODORO_FILE):
        return []
    with open(POMODORO_FILE, "r") as file:
        return json.load(file)


def save_sessions(sessions):
    with open(POMODORO_FILE, "w") as file:
        json.dump(sessions, file, indent=4)


def countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f"\r🍅 Focus Time: {mins:02}:{secs:02}", end="")
        time.sleep(1)
        seconds -= 1
    print()


def start_pomodoro():
    print("\n🍅 Pomodoro started. Stay focused!")
    countdown(WORK_TIME)

    sessions = load_sessions()
    sessions.append({
        "date": datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.now().strftime("%H:%M")
    })
    save_sessions(sessions)

    print("✅ Pomodoro completed and recorded.")


def today_stats():
    sessions = load_sessions()
    today = datetime.now().strftime("%Y-%m-%d")
    count = sum(1 for s in sessions if s["date"] == today)

    print(f"\n📊 Pomodoros completed today: {count}")
