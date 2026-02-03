import json
import os
from datetime import datetime

TASK_FILE = os.path.join("data", "tasks.json")
POMODORO_FILE = os.path.join("data", "pomodoro.json")
HABIT_FILE = os.path.join("data", "habits.json")


def load_json(path, default):
    if not os.path.exists(path):
        return default
    with open(path, "r") as file:
        return json.load(file)


def productivity_score():
    today = datetime.now().strftime("%Y-%m-%d")

    tasks = load_json(TASK_FILE, [])
    pomodoros = load_json(POMODORO_FILE, [])
    habits = load_json(HABIT_FILE, {})

    # ----- TASK SCORE (40) -----
    total_tasks = len(tasks)
    completed_tasks = sum(1 for t in tasks if t.get("completed"))

    task_score = 0
    if total_tasks > 0:
        task_score = (completed_tasks / total_tasks) * 40

    # ----- POMODORO SCORE (40) -----
    today_pomos = [p for p in pomodoros if p.get("date") == today]
    pomo_score = min(len(today_pomos) * 10, 40)  # 4 pomos = full score

    # ----- HABIT SCORE (20) -----
    habits_completed_today = 0
    for habit in habits.values():
        if today in habit.get("dates", []):
            habits_completed_today += 1

    habit_score = min(habits_completed_today * 10, 20)

    total_score = round(task_score + pomo_score + habit_score)

    return {
        "tasks": round(task_score),
        "pomodoro": pomo_score,
        "habits": habit_score,
        "total": total_score
    }

def daily_summary():
    score = productivity_score()

    print("\n📊 DAILY PRODUCTIVITY SUMMARY")
    print(f"Tasks Score:     {score['tasks']} / 40")
    print(f"Pomodoro Score:  {score['pomodoro']} / 40")
    print(f"Habits Score:    {score['habits']} / 20")
    print("-" * 30)
    print(f"🔥 TOTAL SCORE:  {score['total']} / 100")

