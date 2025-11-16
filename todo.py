# Simple To-Do List Application

tasks = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter task to add: ")
        tasks.append(task)
        print(f"Task added: {task}")

    elif choice == "2":
        print("\n--- Your Tasks ---")
        if not tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        print("\n--- Remove Task ---")
        if not tasks:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                remove_index = int(input("Enter task number to remove: "))
                removed = tasks.pop(remove_index - 1)
                print(f"Removed: {removed}")
            except:
                print("Invalid choice. Try again.")

    elif choice == "4":
        print("Exiting... Bye!")
        break

    else:
        print("Invalid option. Please choose 1–4.")
