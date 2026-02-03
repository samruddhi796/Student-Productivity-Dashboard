from modules.task_manager import add_task, view_tasks, complete_task
from modules.pomodoro import start_pomodoro, today_stats
from modules.habit_tracker import add_habit, mark_habit_complete, view_habits


def menu():
    print("\n📊 STUDENT PRODUCTIVITY DASHBOARD")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Start Pomodoro")
    print("5. Pomodoro Stats (Today)")
    print("6. Add Habit")
    print("7. Mark Habit Complete")
    print("8. View Habits")
    print("9. Exit")


def main():
    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            start_pomodoro()
        elif choice == '5':
            today_stats()
        elif choice == '6':
            add_habit()
        elif choice == '7':
            mark_habit_complete()
        elif choice == '8':
            view_habits()
        elif choice == '9':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")


main()

