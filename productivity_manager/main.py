import customtkinter as ctk
import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os
sys.path.append(os.path.abspath("."))

from manager.task import Task
from manager.taskmanager import TaskManager
from manager.category import Category
from manager.usersettings import UserSettings

class TaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Tarefas")
        root.configure(bg="#f0f0f0")

        # Configurações do customtkinter
        ctk.set_appearance_mode("light")  # tema claro

        self.manager = TaskManager()
        self.user_settings = UserSettings()

        # Categorias iniciais
        self.manager.categories = [
            Category("Geral", "#d3d3d3"),    # cinza claro
            Category("Trabalho", "#add8e6"), # azul claro
            Category("Estudos", "#90ee90"),  # verde claro
            Category("Compras", "#ffa500")   # laranja
        ]

        # Treeview para tarefas
        self.task_tree = ttk.Treeview(
            root, columns=("Status", "Título", "Categoria"), show="headings", height=10
        )
        self.task_tree.pack(pady=10)

        self.task_tree.heading("Status", text="Status")
        self.task_tree.heading("Título", text="Título")
        self.task_tree.heading("Categoria", text="Categoria")

        # Entrada de título da tarefa
        self.entry_title = ctk.CTkEntry(root, width=300)
        self.entry_title.pack(pady=5)

        # Combobox para categoria
        self.category_combobox = ctk.CTkComboBox(
            root,
            values=[c.name for c in self.manager.categories]
        )
        self.category_combobox.set("Geral")
        self.category_combobox.pack(pady=5)

        # Botões arredondados e laranja
        self.add_button = ctk.CTkButton(
            root,
            text="Adicionar Tarefa",
            command=self.add_task,
            fg_color="#FFA500",
            hover_color="#FFB733"
        )
        self.add_button.pack(pady=5)

        self.complete_button = ctk.CTkButton(
            root,
            text="Concluir Tarefa",
            command=self.complete_task,
            fg_color="#FFA500",
            hover_color="#FFB733"
        )
        self.complete_button.pack(pady=5)

        self.remove_button = ctk.CTkButton(
            root,
            text="Remover Tarefa",
            command=self.remove_task,
            fg_color="#FFA500",
            hover_color="#FFB733"
        )
        self.remove_button.pack(pady=5)

        # Atualiza lista inicial
        self.update_listbox()

    def add_task(self):
        title = self.entry_title.get()
        category_name = self.category_combobox.get()

        if not title:
            messagebox.showwarning("Erro", "O título não pode ser vazio.")
            return

        category = next((c for c in self.manager.categories if c.name == category_name), None)
        if not category:
            category = Category("Geral", "#d3d3d3")

        task = Task(title, description="", priority=1, due_date="", category=category)
        self.manager.add_task(task)
        self.update_listbox()
        self.entry_title.delete(0, tk.END)

    def complete_task(self):
        selected = self.task_tree.selection()
        if not selected:
            messagebox.showwarning("Erro", "Selecione uma tarefa para concluir.")
            return
        item_id = selected[0]
        index = self.task_tree.index(item_id)
        task_id = list(self.manager.tasks.keys())[index]
        self.manager.complete_task(task_id)
        self.update_listbox()

    def remove_task(self):
        selected = self.task_tree.selection()
        if not selected:
            messagebox.showwarning("Erro", "Selecione uma tarefa para remover.")
            return
        item_id = selected[0]
        index = self.task_tree.index(item_id)
        task_id = list(self.manager.tasks.keys())[index]
        self.manager.remove_task(task_id)
        self.update_listbox()

    def update_listbox(self):
        # limpa itens antigos
        for i in self.task_tree.get_children():
            self.task_tree.delete(i)

        for task in self.manager.get_tasks():
            status = "✔" if task.completed else "✗"
            category_name = task.category.name if task.category else "Geral"
            color = task.category.color if task.category else "#d3d3d3"

            tag_name = f"task_{id(task)}"
            self.task_tree.insert(
                "", tk.END, values=(status, task.title, category_name), tags=(tag_name,)
            )
            self.task_tree.tag_configure(tag_name, background=color)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()
