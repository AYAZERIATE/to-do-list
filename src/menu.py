from task_manager import (
    add_task,
    view_tasks,
    remove_task,
    mark_done
)
def menu ():
    print("***To Do List ***" )
    print("1.Add task")
    print("2.view task")
    print("3.Remove Task")
    print("4.Mark completed")
    print ("5.Exit")

    choice=input("Choice :")
