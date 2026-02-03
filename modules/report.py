import json
import os
from datetime import datetime, timedelta
from modules.stats import productivity_score

TASK_FILE = os.path.join("data", "tasks.json")
POMODORO_FILE = os.path.join("data", "pomodoro.json")
HABIT_FILE = os.path.join("data", "habits.json")
REPORT_FILE = os.path.join("reports", "weekly_report.txt")


def load_json(path, default):
    if not os.path.exists(path):
        return default
    with open(path, "r") as file:
        return json.load(file)


def generate_weekly_report():
    today = datetime.now().date()
    week_dates = [(today - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(7)]

    tasks = load_json(TASK_FILE, [])
    pomodoros = load_json(POMODORO_FILE, [])
    habits = load_json(HABIT_FILE, {})

    completed_tasks = sum(1 for t in tasks if t.get("completed"))
    weekly_pomodoros = sum(1 for p in pomodoros if p.get("date") in week_dates)

    habit_summary = {}
    for name, data in habits.items():
        count = sum(1 for d in data.get("dates", []) if d in week_dates)
        habit_summary[name] = count

    score = productivity_score()

    lines = []
    lines.append("📅 WEEKLY PRODUCTIVITY REPORT")
    lines.append("=" * 30)
    lines.append(f"Date Range: {week_dates[-1]} to {week_dates[0]}")
    lines.append("")
    lines.append(f"✔ Tasks Completed: {completed_tasks}")
    lines.append(f"🍅 Pomodoros Completed: {weekly_pomodoros}")
    lines.append("")
    lines.append("📌 Habits Summary:")
    for habit, count in habit_summary.items():
        lines.append(f"- {habit}: {count}/7 days")
    lines.append("")
    lines.append("📊 Current Productivity Score:")
    lines.append(f"- Total Score: {score['total']} / 100")
    lines.append("")
    lines.append("🔥 Keep building consistency!")

    os.makedirs("reports", exist_ok=True)
    with open(REPORT_FILE, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))

    print(f"📄 Weekly report generated: {REPORT_FILE}")
