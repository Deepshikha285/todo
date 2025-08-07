To-Do List (Console-Based)
A simple command-line To-Do List application written in Python. It allows users to add, view, and remove tasks with persistence using a text file.

Tech Stack
Language: Python 3

Editor: VS Code / Terminal

Storage: Plain text file (tasks.txt)

1.Features
2.Add new tasks
3.View existing tasks
4.Remove completed or unwanted tasks
5.Saves tasks to a file (tasks.txt) for persistent storage

* File Structure

* your_project_directory/
│
├── todo.py         # Main Python script
├── tasks.txt       # Automatically created to store tasks (if not present)
└── README.md       # Project documentation
How to Run
1. Clone or download this repository

git clone (https://github.com/Deepshikha285/News_Scraper)
cd todo-console-app
2. Run the app

python todo.py
Make sure you have Python 3 installed. You can check by running python --version.

Sample Usage

=== To-Do List Menu ===
1. View tasks
2. Add task
3. Remove task
4. Exit
Choose an option (1-4): 2
Enter a new task: Buy groceries

Task added: Buy groceries

tasks.txt
All tasks are stored in a plain text file named tasks.txt. This file is automatically created in the same directory as the script.
Future Improvements (Optional Ideas)
Mark tasks as completed 

Add due dates or priorities 

Use JSON or SQLite for advanced storage

Create a GUI version using Tkinter or PyQt
