# To-Do List CLI

![Python](https://img.shields.io/badge/python-3.6%2B-blue)

## Features

- Add new tasks
- Show a numbered list of your current tasks
- Complete (remove) a task by its **number** or by its **exact text**
- Confirmation prompt (`y/n`) before a task is completed

## Installation

1. Make sure Python 3.6+ is installed. You can download it from [python.org](https://www.python.org/downloads/).
2. Download or clone this project:

   ```bash
   git clone <your-repository-url>
   cd <your-repository-folder>
   ```


## Usage

Run the program from the project folder:

```bash
python main.py
```

(Use `python3 main.py` if `python` points to Python 2 on your system.)

The program shows the list of actions and asks what you want to do. Type the action name (not case-sensitive) and press **Enter**.

### Available actions

| Action | Description |
|--------|-------------|
| `Help` | Shows the list of actions |
| `Add`  | Adds a new task |
| `Show` | Shows your To-Do list |
| `Done` | Completes (removes) a task |
| `Exit` | Exits the program |

### Example session

```text
Actions:
Help - Shows you this menu.
Add  - Adds new task
Show - Shows you To-Do list.
Done - Complites a task.
Exit - Exits the program
What action do you want to do?
> add
What task would you like to add to the to-do list?
>Buy milk

What action do you want to do?
> show

--------Tasks--------
1. Buy milk

If you want to continue press enter...

What action do you want to do?
> done

--------Tasks--------
1. Buy milk

What do you want to remove?
>1
Do you really want to complite 1? (y/n)
>y
```

### Completing a task

When you choose `Done`, you can identify the task in one of two ways:

- **By number**, e.g. `1` (the number shown in the task list)
- **By exact text**, e.g. `Buy milk` (must match what you originally typed)

You'll then be asked to confirm with `y` (yes) or `n` (no).

## Ideas for future improvements

- Save and load tasks from a file (e.g. JSON) so they persist between runs
- Mark tasks as done instead of deleting them
- Edit existing tasks
