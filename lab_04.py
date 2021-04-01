tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

def uncompleted_tasks(list):
    uncompleted_task = []
    for each_task in list:
        if (each_task["completed"]== False):
            uncompleted_task.append(each_task)
    return uncompleted_task

print("# 1")

print(uncompleted_tasks(tasks))


def completed_tasks(list):
    completed_task = []
    for each_task in list:
        if (each_task["completed"]== True):
            completed_task.append(each_task)
    return completed_task

print("# 2")
print(completed_tasks(tasks))

#3

def task_descriptions(list):
    task_descriptions = []
    for description in list:
        if(description["description"]):
            task_descriptions.append(description["description"])
    return task_descriptions

print("# 3")
print(task_descriptions(tasks))


#4
def time_taken (input_time,list):
    updatedTask=[]
    for each_task in list:
        if(input_time >=each_task["time_taken"]):
            updatedTask.append(each_task)
        
    return updatedTask
print("# 4")
print(time_taken(5,tasks))

#5
def descriptive_task (input_description,list):
    updatedTask=["Task not found"]
    for each_task in list:
        if(each_task["description"]==input_description):
            updatedTask.append(each_task)
        
    return updatedTask
print("# 5")
print(descriptive_task('Clean Windows',tasks))


#6
def description_update(specificTask, updatedTask,list):
    updatedTask= []
    for each_task in list:
        if(each_task["description"]==specificTask["description"]):
            each_task["completed"]=True
            updatedTask.append(each_task)
        else :
            updatedTask.append(each_task)
    return updatedTask
print("# 6")
print(description_update({"description": "Wash Dishes"},"Washed Dishes", tasks))


#7
def add_task(newTask):
    tasks.append(newTask)
    return tasks


print("# 7")
print(add_task({ "description": "Lights off", "completed": False, "time_taken": 5 }))


#8

mainMenu = [
    "Menu:",
    {
        "2": "Display Uncompleted Tasks",
        "3": "Display Completed Tasks",
        "4": "Mark Task as Complete",
        "5": "Get Tasks Which Take Longer Than a Given Time",
        "6": "Find Task by Description",
        "7": "Add a new Task to list",
        "M": "Display this menu",
        "m": "Display this menu",
        "Q": "Quit",
        "q": "Quit"


    }

]
#8 & 9
# 9 partially done
def called_item(user_selection, list):
    print (user_selection)
    if(user_selection==2):
        return uncompleted_tasks(tasks)
    elif (user_selection==3):
        return completed_tasks(tasks)
    




def menu():
   userInput = input("Please enter from the menu options")
   while(mainMenu[1][userInput]):
       print (mainMenu[1][userInput])
       print(called_item(int(userInput),tasks))
       break
   
print("# 8")
menu()



































