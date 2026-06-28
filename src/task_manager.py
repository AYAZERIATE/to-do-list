from storage import load_tasks, save_tasks
todo_list = load_tasks()
def add_task():
    task = input("Enter a task: ")

    todo_list.append({
        "task": task,
        "status": "pending"
    })
    save_tasks(todo_list)

    print("New Task Added Successfully!\n")


def view_tasks():
    print("\n===== Your Todo List =====")

    if len(todo_list) == 0:
        print("No Tasks Found.\n")
    else:
        for index, task in enumerate(todo_list, 1):
            print(f"{index}. {task['task']} - {task['status']}")
        print()


def remove_task():
    if len(todo_list) == 0:
        print("No Tasks to Remove.\n")
        return

    view_tasks()

    try:
        search_index = int(input("Enter the task number to remove: ")) - 1

        if 0 <= search_index < len(todo_list):
            removed_task = todo_list.pop(search_index)
            print(f"Task '{removed_task['task']}' removed successfully.\n")
            save_tasks(todo_list)

        else:
            print("Invalid task number.\n")

    except ValueError:
        print("Please enter a valid number.\n")


def mark_done():
    if len(todo_list) == 0:
        print("No Tasks Available.\n")
        return

    view_tasks()

    try:
        search_index = int(input("Enter the task number to mark as completed: ")) - 1

        if 0 <= search_index < len(todo_list):
            todo_list[search_index]["status"] = "Completed"
            print("Task marked as completed.\n")
            save_tasks(todo_list)

        else:
            print("Invalid task number.\n")

    except ValueError:
        print("Please enter a valid number.\n")