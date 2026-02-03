from tasks.task_manager import display_tasks, filter_tasks, task_generator

# Initial list of tasks
tasks = ["Buy groceries", "Finish project", "Call mom", "Send email", "Clean room", "Finish coding"]

# Displaying Existing Tasks
# print("\nAll Tasks:")
# display_tasks(tasks)

# Filtering Tasks with List Comprehensions
# filter_tasks(tasks, "finish")

# Processing Tasks Using Generator Expression

project_tasks = task_generator(tasks, "finish")
print(next(project_tasks))