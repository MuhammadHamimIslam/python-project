# todo list

allTasks = [] # all tasks 

while True:
    mode = input("Enter the mode: ")
    if mode == "a": 
        taskName = input("Enter the task name: ")
        taskTime = input("Enter the time: ")
        allTasks.append({taskName: taskTime})
        for i in allTasks: 
            print(i)
    elif mode == "r":
        taskName = input("Enter the task name: ")
        for x in allTasks: 
            if taskName in x.keys(): 
                del allTasks[allTasks.index(x)]
        print("Task removed!")
    elif mode == "c":
        for i in allTasks: 
            print(i)
    elif mode == "e": break
    else:
        print("Invalid mode")

