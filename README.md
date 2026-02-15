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

1. Clone the repository:
2. Create a virtual environment (recommended):
3. Install dependencies:

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

## Exemple
<img width="599" height="460" alt="image" src="https://github.com/user-attachments/assets/ba76e179-1566-46fb-9fd0-b44533b0f111" />


