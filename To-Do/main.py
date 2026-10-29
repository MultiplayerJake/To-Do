import sys

ToDos = []
ACTIONSTEXT = "Actions:\nHelp - Display this menu.\nAdd - Add a new task.\nShow - Display your to-do list.\nDone - Complete a task.\nExit - Exit the program."
ACTIONS = ["HELP", "ADD", "SHOW", "DONE", "EXIT"]


def appendingToDo():
    while True:
        output = input("What task would you like to add to the to-do list?\n> ").strip()
        if output == "":
            print("A task cannot be empty. Please type something.")
        else:
            break
    ToDos.append(output)

def printToDos():
    line = "-" * 8
    print("\n")
    print(f"{line}Tasks{line}")
    for i in range(len(ToDos)):
        print(f"{i+1}. {ToDos[i]}")
    print("\n")

def doneTask():
    # if there are no tasks there is nothing we can do
    if len(ToDos) == 0:
        print("There are no tasks to complete.")
        input("Press Enter to continue...\n")
        return

    printToDos()
    output = input("Which task would you like to remove?\n> ").strip()
    while True:
        booloutput = input(f"Do you really want to complete {output}? (y/n)\n> ").upper()
        if booloutput == "Y":
            break
        if booloutput == "N":
            return
        else:
            print('Invalid input. Type "Y" for yes or "N" for no.')

    removed = False

    # first look for a task with the same text (upper/lower does not matter)
    for i in range(len(ToDos)):
        if ToDos[i].lower() == output.lower():
            ToDos.pop(i)
            removed = True
            break

    # if no task had that text, maybe the user typed the task number
    if removed == False:
        try:
            number = int(output)
            if number >= 1 and number <= len(ToDos):
                ToDos.pop(number - 1)
                removed = True
            else:
                print("Invalid task number.")
        except ValueError:
            print("Task does not exist.")

    printToDos()
    # only say it worked when something was really removed
    if removed:
        print("Task completed successfully.")
    input("Press Enter to continue...\n")

def chosingAction():
    print(ACTIONSTEXT)
    output = input("Which action would you like to perform?\n> ").strip().upper()
    if output == ACTIONS[0]:
        print(ACTIONSTEXT)
    elif output == ACTIONS[1]:
        appendingToDo()
    elif output == ACTIONS[2]:
        printToDos()
        input("Press Enter to continue...\n")
    elif output == ACTIONS[3]:
        doneTask()
    elif output == ACTIONS[4]:
        sys.exit(0)
    else:
        print("Unknown action. Type Help to see the list of actions.")

# if the input is closed (for example an empty pipe) just exit nicely
try:
    while True:
        chosingAction()
except EOFError:
    print()
    sys.exit(0)
