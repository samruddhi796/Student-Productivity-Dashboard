from modules.task_manager import add_task, view_tasks, complete_task


def menu():
    print("\n📊 STUDENT PRODUCTIVITY DASHBOARD")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Exit")


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
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")


main()
