#  Todo List Python

A simple and clean command-line Todo List application built with Python.  
Tasks are saved automatically to a local JSON file so nothing is lost between sessions.

---

##  Features

-  Add new tasks
- View all tasks with their status
- Remove tasks by number
- Mark tasks as completed
-  Auto-save to `data/tasks.json`
- Screen clearing and date utilities

---

## Project Structure

```
todo-list-python/
│
├── data/
│   └── tasks.json        # Auto-generated — stores your tasks
│
├── src/
│   ├── main.py           # Entry point
│   ├── menu.py           # Menu loop and user interaction
│   ├── task_manager.py   # Core logic (add, view, remove, complete)
│   ├── storage.py        # Load and save tasks to JSON
│   └── utils.py          # Helper functions (clear screen, date, etc.)
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/AYAZERIATE/todo-list-python.git
cd todo-list-python
```

### 2. Run the app

```bash
python src/main.py
```

> No external dependencies required — uses Python standard library only.

---

## Usage

```
========================================
        TODO LIST APP
========================================
*** To Do List ***
1. Add task
2. View tasks
3. Remove task
4. Mark completed
5. Exit

Choice:
```

### Example — Adding a task

```
Enter a task: Buy groceries
New Task Added Successfully!
```

### Example — Viewing tasks

```
===== Your Todo List =====
1. Buy groceries - pending
2. Finish project report - Completed
```

---

##  Data Storage

Tasks are stored in `data/tasks.json` in this format:

```json
[
  {
    "task": "Buy groceries",
    "status": "pending"
  },
  {
    "task": "Finish project report",
    "status": "Completed"
  }
]
```

The file is created automatically on first use.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.10+ | Core language |
| `json` (stdlib) | Task persistence |
| `os` (stdlib) | Cross-platform screen clearing |
| `datetime` (stdlib) | Timestamps |

---

##  Author

**Aya Zeriate**  
[GitHub](https://github.com/AYAZERIATE) · [LinkedIn](https://www.linkedin.com/in/aya-zeriate-0b123a338/)

---

## License

This project is licensed under the MIT License.
