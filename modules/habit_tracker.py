import json
import os
from datetime import datetime, timedelta

HABIT_FILE = os.path.join("data", "habits.json")


def load_habits():
    if not os.path.exists(HABIT_FILE):
        return {}
    with open(HABIT_FILE, "r") as file:
        return json.load(file)


def save_habits(habits):
    with open(HABIT_FILE, "w") as file:
        json.dump(habits, file, indent=4)


def add_habit():
    habits = load_habits()
    name = input("Habit name: ").strip()

    if not name:
        print("❌ Habit name cannot be empty.")
        return

    if name in habits:
        print("ℹ Habit already exists.")
        return

    habits[name] = {
        "dates": [],
        "streak": 0,
        "longest_streak": 0
    }

    save_habits(habits)
    print("✅ Habit added.")


def calculate_streak(dates):
    if not dates:
        return 0, 0

    date_objs = sorted(
        datetime.strptime(d, "%Y-%m-%d") for d in dates
    )

    current = longest = 1

    for i in range(1, len(date_objs)):
        if date_objs[i] - date_objs[i - 1] == timedelta(days=1):
            current += 1
            longest = max(longest, current)
        else:
            current = 1

    return current, longest


def mark_habit_complete():
    habits = load_habits()
    name = input("Habit name: ").strip()

    if name not in habits:
        print("❌ Habit not found.")
        return

    today = datetime.today().strftime("%Y-%m-%d")

    if today in habits[name]["dates"]:
        print("ℹ Habit already marked for today.")
        return

    habits[name]["dates"].append(today)

    streak, longest = calculate_streak(habits[name]["dates"])
    habits[name]["streak"] = streak
    habits[name]["longest_streak"] = max(
        habits[name]["longest_streak"], longest
    )

    save_habits(habits)
    print("🔥 Habit marked complete for today!")


def view_habits():
    habits = load_habits()

    if not habits:
        print("📭 No habits added yet.")
        return

    print("\n📅 HABIT TRACKER")
    for name, data in habits.items():
        print(
            f"- {name} | Current Streak: {data['streak']} | Longest: {data['longest_streak']}"
        )
