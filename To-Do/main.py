ToDos = []
booloutput = ""
ACTIONSTEXT = "Actions:\nHelp - Display this menu.\nAdd - Add a new task.\nShow - Display your to-do list.\nDone - Complete a task.\nExit - Exit the program."
ACTIONS = ["HELP", "ADD", "SHOW", "DONE", "EXIT"]


def appendingToDo():
    output = input("What task would you like to add to the to-do list?\n> ")
    ToDos.append(output)

def printToDos():
    line = "-" * 8
    print("\n")
    print(f"{line}Tasks{line}")
    for i in range(len(ToDos)):
        print(f"{i+1}. {ToDos[i]}")
    print("\n")

def doneTask():
    printToDos()
    output = input("Which task would you like to remove?\n> ")
    while True:
        booloutput = input(f"Do you really want to complete {output}? (y/n)\n> ").upper()
        if booloutput == "Y":
            break
        if booloutput == "N":
            return
        else:
            print('Invalid input. Type "Y" for yes or "N" for no.')

    if booloutput.upper() == "y".upper():
        try:
            output = int(output)
            try:
                ToDos.pop(int(output)-1)
            except:
                print("Invalid task number.")
        except:
            try:
                ToDos.remove(output)
            except:
                print("Task does not exist.")

    booloutput =""
    printToDos()
    print("Task completed successfully.")
    input("Press Enter to continue...\n")

def chosingAction():
    print(ACTIONSTEXT)
    output = input("Which action would you like to perform?\n> ").strip().upper()
    if output == ACTIONS[0]:
        print(ACTIONSTEXT)
    if output == ACTIONS[1]:
        appendingToDo()
    if output == ACTIONS[2]:
        printToDos()
        input("Press Enter to continue...\n")
    if output == ACTIONS[3]:
        doneTask()
    if output == ACTIONS[4]:
        exit(0)

while True: 
    chosingAction()
