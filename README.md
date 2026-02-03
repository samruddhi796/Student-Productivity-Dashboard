# 📊 Student Productivity Dashboard

A modular **Python-based productivity system** designed for students to track tasks, focus sessions, habits, and overall productivity in one place.

This project integrates multiple productivity tools into a **single cohesive dashboard**, demonstrating system design, data persistence, and real-world logic.

---

## 🚀 Features

### ✅ Task Manager
- Add tasks with priority
- Mark tasks as completed
- Persistent storage using JSON

### 🍅 Pomodoro Timer
- 25-minute focused work sessions
- Tracks daily pomodoro count
- Session history stored locally

### 📅 Habit Tracker
- Add daily habits
- Mark habits as completed
- Automatic **current streak** and **longest streak** calculation

### 📊 Productivity Score
Daily productivity score out of **100**, based on:
- Tasks completed (40%)
- Pomodoro sessions (40%)
- Habits completed (20%)

### 📄 Weekly Productivity Report
- Auto-generates a weekly text report
- Summarizes:
  - Tasks completed
  - Pomodoros done
  - Habit consistency
  - Current productivity score
- Saved to `/reports/weekly_report.txt`

---

## 🗂 Project Structure

