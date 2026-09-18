ToDos = []
booloutput = ""
ACTIONSTEXT = "Actions:\nHelp - Shows you this menu.\nAdd  - Adds new task\nShow - Shows you To-Do list. \nDone - Complites a task.\nExit - Exits the program"
ACTIONS = ["HELP", "ADD", "SHOW", "DONE", "EXIT"]


def appendingToDo():
    output = input("Napiš co chceš přidat To-DO:\n>")
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
    output = input("What do you want to remove?\n>")
    while True:
        booloutput = input(f"Do you really want to complite {output}? (y/n)\n>").upper()
        if booloutput == "Y":
            break
        if booloutput == "N":
            return
        else:
            print('You typed it wrong! You need to type "Y" for yes or "N" for no.')

    if booloutput.upper() == "y".upper():
        try:
            output = int(output)
            try:
                ToDos.pop(int(output)-1)
            except:
                print("Number is wrong!")
        except:
            try:
                ToDos.remove(output)
            except:
                print("Task dosent exist!")

    booloutput =""
    printToDos()
    print("Task was succesfuly complited")
    input("If you want to continue press enter...\n")

def chosingAction():
    print(ACTIONSTEXT)
    output = input("What action do you want to do?\n> ").strip().upper()
    if output == ACTIONS[0]:
        print(ACTIONSTEXT)
    if output == ACTIONS[1]:
        appendingToDo()
    if output == ACTIONS[2]:
        printToDos()
        input("If you want to continue press enter...\n")
    if output == ACTIONS[3]:
        doneTask()
    if output == ACTIONS[4]:
        exit(0)

while True: 
    chosingAction()
