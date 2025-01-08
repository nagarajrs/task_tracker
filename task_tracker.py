import datetime
import json
import argparse

"""initialize parser

description_msg = ""
usage:
    tasky [option] ... [-h help | -l list_task | -a add_task | -u update_task | -d delete_task | -c change_process | -ls list_by_status]

Options:
    -h,  --help             : Print this help message and exit (also -? or --help)
    -l,  --list_task        : List all existing task
    -a,  --add_task         : Add new task
    -u,  --update_task      : Update existing task
    -d,  --delete_task      : Delete task
    -c,  --change_status    : Change status of the task
    -ls, --list_by_status   : List tasks by using status as filter
"""
#parser = argparse.ArgumentParser(description=description_msg)
#parser.add_argument("-l","--list_task", help="List all existing task")
#parser.parse_args()

def read_file():
#Open the task.json file and store the list as type list using json loads and close the file.
    try:
        with open('task.json','r') as r:
            task_list = r.read()
            task_list = json.loads(task_list)
            r.close()
#Create file if does not exist
    except FileNotFoundError:
        open('task.json','x')
        task_list = []
    return task_list
#    pass

def write_file():
    pass

def list_task():
    # Opens the JSON file and stores the list under a variable
    with open('task.json', 'r') as r:
        json_content = r.read()
    # Loading in from file makes it data type as string, so using json.loads to change the type to list
    content_dict = json.loads(json_content)
    # Print task name
    for dict in range(0, len(content_dict)):
        print(content_dict[dict])

def get_next_id(task_list):
    existing_ids = {task["id"] for task in task_list}
    next_id = 1
    while next_id in existing_ids:
        next_id +=1
    return next_id

def add_task():
    task_list = read_file()
#get current date and time when the task is added
    time = str(datetime.datetime.now())
    next_id = get_next_id(task_list)
#get user inputs for task
    task_n = {
        "id": next_id,
        "Task": input("Task: "),
        "Description": input("Description: "),
        "Status": input("Status: "),
        "createdAt": time
    }
    print(f"Your task ID is {next_id}")
#Create a new list if the task.json file is new
    if len(task_list) == 0:
        task_list = [task_n]
#Append the dictionary to existing list using append.
    else:
        task_list.append(task_n)
        sorted_tasks = sorted(task_list, key=lambda x: x["id"])
#Write the task list in json format in the task.json file
    json_object = json.dumps(sorted_tasks,indent=4)
    with open('task.json','w+') as outfile:
        outfile.write(json_object)

def update_task():
    task_id = int(input("Enter the task ID you want to update: "))
    task_list = read_file()
    found = False
#    task = [task if task_list["id"]==task_id else print("Task ID not found") for task in task_list]
#    task = next((task for task in task_list if task['id'] == task_id),None)
#   if task is None:
    for task in task_list:
        if task_id == task["id"]:
            found = True
            id = int(task["id"])
            Task = task["Task"]
            Description = task["Description"]
            Status = task["Status"]
            createdAt = task["createdAt"]
            task_list.remove(task)
#            task = (task for task in task_list if task_id["id"] != task_id)
            Task_update = input(f'Task ({Task}): Enter New Task Name: \n>>> ').strip()
            Description_update = input(f'Description ({Description}): Enter New Description:\n>>> ').strip()
            Status_update = input(f'Status: ({Status}): Enter New Status:\n>>> ').strip()

            if not Task_update: 
                Task_update = Task
            if not Description_update:
                Description_update = Description
            if not Status_update:
                Status_update = Status
            updatedAt = str(datetime.datetime.now())
            updated_task = {
                "id" : id,
                "Task" : Task_update,
                "Description" : Description_update,
                "Status" : Status_update,
                "createdAt" : createdAt,
                "updatedAt" : updatedAt
            }
            task_list.append(updated_task)
            sorted_task = sorted(task_list, key=lambda x:x["id"])
            json_object = json.dumps(sorted_task, indent=4)
            with open('task.json','w') as outfile:
                outfile.write(json_object)
            print("Task updated successully")
            break
    if not found:
            print("Task ID not found")

def delete_task():
    task_list = read_file()
    task_id = int(input('Enter the Task ID that you want to delete: '))
    found = False
    for task in task_list:
        if task["id"]==task_id:
            found = True
            print(f'(Check the below task details \n{task}\n )')
            confirmation = input("Final Confirmation: Do you want to delete?\n(Yes or No) >> ")
            if confirmation.upper() == "YES":
                task = [task for task in task_list if task["id"]!=task_id]
                json_object = json.dumps(task,indent=4)
                with open('task.json','w+') as outfile:
                    outfile.write(json_object)
                print("The task has been deleted")
                break
            elif confirmation.upper() == "NO":
                print("Task deletion has been aborted")
                break
            else:
                print("Please enter only Yes or No")
                break
    if not found:
        print("Task ID not found")
        

            
#    task = [task for task in task_list if task["id"]==task_id]        

def change_process():
    pass

#add_task()
list_task()
#delete_task()
#task_list = read_file()
#get_next_id(task_list)
#update_task()