def menu():
    print("\nTO-DO-LIST-MENU")
    print("1.View Task")
    print("2.Add Task")
    print("3.Mark Task as Done")
    print("4.Delete Task")
    print("5.Exit")

tasks = []

while True:
    menu()
    choice = input("Enter the Choice (1-5): ")

    if choice == "1":
        if not tasks:
            print("No Tasks to show")
        else:
            print("Your Tasks")
            for i in tasks:
                print(i)

    elif choice == "2":
        new_task = input("Enter the task: ")
        tasks.append(new_task)
        print("Task Added")

    elif choice == "3":
        task_number = int(input("Enter the task number to mask as done: "))
        if 0 <= task_number < len(tasks):
            tasks[task_number] += "✅"
            print("Task Done")
        else:
            print("Invalid Task Number: ")

    elif choice == "4":
        task_number = int(input("Enter the task number to be deleted: "))
        if 0<= task_number < len(tasks):
            removed = tasks.pop(task_number)
            print("Task removed")
        else:
            print("Invalid Task Number")
    
    elif choice == "5":
        print("Goodbye! Have a great day!")
        break

    else:
        print("Enter the Number between 1 and 5: ")