# To-Do List CLI

![Python](https://img.shields.io/badge/python-3.6%2B-blue)

## Features

- Add new tasks
- Show a numbered list of your current tasks
- Complete (remove) a task by its **number** or by its **text** (capitalization doesn't matter)
- Confirmation prompt (`y/n`) before a task is completed

## Installation

This app is a single script (`To-Do/main.py`) with **no third-party dependencies** — there's nothing to `pip install` and no build step. You only need:

1. **Python 3.6 or newer** — the code uses f-strings. Download it from [python.org](https://www.python.org/downloads/) and check your version with `python --version`.
2. **This repository's code** — clone it with git:

   ```bash
   git clone https://github.com/MultiplayerJake/To-Do.git
   ```

   Or click **Code → Download ZIP** on [github.com/MultiplayerJake/To-Do](https://github.com/MultiplayerJake/To-Do) and unzip it.

That's the whole installation. Continue with Usage below to run the app.

## Usage

The script lives in a `To-Do/` subfolder **inside** the repository. From the repository root (the folder that contains this README), run:

```bash
cd To-Do
python main.py
```

or without changing directory:

```bash
python To-Do\main.py    # Windows
python To-Do/main.py    # macOS / Linux
```

(Use `python3` instead of `python` if `python` points to Python 2 on your system.)

The program shows the list of actions and asks what you want to do. Type the action name (not case-sensitive) and press **Enter**. Unrecognized input prints `Unknown action. Type Help to see the list of actions.` and then the action menu is shown again.

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
Help - Display this menu.
Add - Add a new task.
Show - Display your to-do list.
Done - Complete a task.
Exit - Exit the program.
Which action would you like to perform?
> add
What task would you like to add to the to-do list?
> Buy milk
Actions:
Help - Display this menu.
Add - Add a new task.
Show - Display your to-do list.
Done - Complete a task.
Exit - Exit the program.
Which action would you like to perform?
> show


--------Tasks--------
1. Buy milk


Press Enter to continue...

Actions:
Help - Display this menu.
Add - Add a new task.
Show - Display your to-do list.
Done - Complete a task.
Exit - Exit the program.
Which action would you like to perform?
> done


--------Tasks--------
1. Buy milk


Which task would you like to remove?
> 1
Do you really want to complete 1? (y/n)
> y


--------Tasks--------


Task completed successfully.
Press Enter to continue...
```

### Adding a task

When you choose `Add`, you're asked for the task text. Spaces around what you type are ignored, and a blank task is rejected with `A task cannot be empty. Please type something.` — you'll be asked again until you type something.

### Completing a task

If the list is empty, choosing `Done` just prints `There are no tasks to complete.` and returns to the action menu.

Otherwise the current task list is shown and you're asked which task to remove. You can identify the task in one of two ways:

- **By number**, e.g. `1` (the number shown in the task list)
- **By its text**, e.g. `buy milk` (capitalization doesn't matter, and spaces around what you type are ignored)

You'll then be asked to confirm with `y` (yes) or `n` (no). Typing `n` cancels and returns to the action menu without changing anything; any other input repeats the confirmation prompt with a hint. The task list is shown again after the attempt — if a task was really removed you also see `Task completed successfully.`

If the number is out of range you get `Invalid task number.`; if what you typed matches neither a task's text nor a valid number you get `Task does not exist.`

## Ideas for future improvements

- Save and load tasks from a file (e.g. JSON) so they persist between runs
- Mark tasks as done instead of deleting them
- Edit existing tasks
