# Productivity_Manager
Personal task organizer

Productivity Manager is a task management application developed in Python using Tkinter and CustomTkinter. It allows users to create, complete, and remove tasks, categorize them, and view categories with distinct colors.

The app was designed to be lightweight, intuitive, and visually appealing, featuring rounded, colorful buttons and tasks with category-colored backgrounds.

## Features

- Create new tasks with title and category.
- Mark tasks as completed.
- Remove tasks.
- View tasks with background colors according to their category.
- Modern interface with rounded orange buttons using CustomTkinter.
- Customizable categories (General, Work, Study, Shopping) with configurable colors.
- Task list organized in Treeview.

## Technologies

- Python 3.10 or higher
- Tkinter (Python standard GUI)
- CustomTkinter (for modern rounded buttons)
- ttk.Treeview (for task list with background colors)
- Modular structure with classes: Task, TaskManager, Category, UserSettings

## Installation

1. git clone https://github.com/JhullyGabriele/Productivity_Manager.git
2. code:
cd Productivity_Manager
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate in Windows
pip install -r requirements.txt
python main.py


## Usage

1. Run the main file:
2. In the interface:

- Enter the task title in the input field.
- Select the category from the dropdown menu.
- Click Add Task.
- To complete a task, select it in the list and click Complete Task.
- To remove a task, select it and click Remove Task.

## Customization

- Category colors: change the `color` attribute in the Category class.
- Buttons: change the color and hover effect using the `fg_color` and `hover_color` parameters in CTkButton.
- Interface theme: change `ctk.set_appearance_mode("light")` to "dark" for dark mode.

## Notes

- The project is developed with modularity for easy maintenance and expansion.
- Can be extended to save tasks in JSON files or a database.
- Suitable for users who want a lightweight and customizable productivity app in Python.

## Example
<img width="595" height="461" alt="Captura de tela 2026-02-15 020800" src="https://github.com/user-attachments/assets/fee37726-7a62-41b9-b2ec-476a577f09a2" />


