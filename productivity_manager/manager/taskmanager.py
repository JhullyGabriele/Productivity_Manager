#TaskManager

class TaskManager:
	def __init__(self):
		self.tasks = {}

	def add_task(self, task):
		self.tasks[task.id] = task

	def remove_task(self, task_id):
		# Remove a task pelo ID, se existir
		if task_id in self.tasks:
			del self.tasks[task_id]
		else:
			print(f"Tarefa com ID {task_id} não encontrada.")

	def complete_task(self, task_id):
		if task_id in self.tasks:
			self.tasks[task_id].mark_completed()
		else:
			print(f"Tarefa com ID {task_id} não encontrada.")

	def get_tasks(self, show_completed=True):
		if show_completed:
			return list(self.tasks.values())
		else:
			return [task for task in self.tasks.values() if not task.completed]
