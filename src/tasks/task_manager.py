def display_tasks(task_list):
    print("\nCurrent To-Do List:")
    for index, task in enumerate(task_list, start=1):
        print(f"{index}. {task}")
    # """Displays the list of tasks."""
    # print(f"\nDisplaying all tasks is not yet implemented")

def filter_tasks(task_list, keyword):
    filtered = [task for task in task_list if keyword.lower() in task.lower()]
    print(f"\nTasks matching '{keyword}'")
    display_tasks(filtered)
    # """Placeholder for filtering tasks (students will implement)."""
    # print(f"\nFiltering for '{keyword}' is not yet implemented.")

def task_generator(task_list, keyword):
    return (task for task in task_list if keyword.lower() in task.lower())
    # """Placeholder for generator-based filtering (students will implement)."""
    # print(f"\nLazy evaluation for '{keyword}' is not yet implemented.")
