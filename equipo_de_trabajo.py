# task_manager.py

# Preload the list of tasks
def preload_tasks():
    # List of tasks, each represented as a dictionary
    tasks = [
        {"title": "Task 1", "description": "Complete the report", "assigned_to": "Alice", "priority": "High", "status": "Pending"},
        {"title": "Task 2", "description": "Develop the UI", "assigned_to": "Bob", "priority": "Medium", "status": "In progress"},
        {"title": "Task 3", "description": "Test the application", "assigned_to": "Charlie", "priority": "Low", "status": "Pending"},
        {"title": "Task 4", "description": "Fix bugs", "assigned_to": "Alice", "priority": "High", "status": "Done"},
        {"title": "Task 5", "description": "Deploy to production", "assigned_to": "Bob", "priority": "Medium", "status": "Done"}
    ]
    return tasks

# Function to register a new task
def register_task(tasks, title, description, assigned_to, priority, status):
    # Validate the status (must be one of "Pending", "In progress", or "Done")
    if status not in ["Pending", "In progress", "Done"]:
        print("Error: Status must be 'Pending', 'In progress', or 'Done'.")
        return
    
    # Create a new task as a dictionary and add it to the tasks list
    task = {"title": title, "description": description, "assigned_to": assigned_to, "priority": priority, "status": status}
    tasks.append(task)
    print(f"Task '{title}' registered successfully.")

# Function to search tasks by member name or status
def search_task(tasks, query):
    # List to store matching tasks
    results = []
    for task in tasks:
        if query.lower() in task["assigned_to"].lower() or query.lower() in task["status"].lower():
            results.append(task)
    return results

# Function to update task priority or status
def update_task(tasks, task_title, new_priority=None, new_status=None):
    for task in tasks:
        if task["title"].lower() == task_title.lower():
            # Validate new status
            if new_status and new_status not in ["Pending", "In progress", "Done"]:
                print("Error: Status must be 'Pending', 'In progress', or 'Done'.")
                return
            # Update priority if provided
            if new_priority:
                task["priority"] = new_priority
            # Update status if provided and valid
            if new_status:
                task["status"] = new_status
            print(f"Task '{task_title}' updated successfully.")
            return
    print(f"Task '{task_title}' not found.")

# Function to delete a task if its status is 'Done'
def delete_task(tasks, task_title):
    for task in tasks:
        if task["title"].lower() == task_title.lower():
            if task["status"] == "Done":
                confirm = input(f"Are you sure you want to delete the completed task '{task_title}'? (yes/no): ")
                if confirm.lower() == 'yes':
                    tasks.remove(task)
                    print(f"Task '{task_title}' deleted successfully.")
                    return
                else:
                    print("Deletion canceled.")
                    return
            else:
                print(f"Task '{task_title}' is not completed. It cannot be deleted.")
                return
    print(f"Task '{task_title}' not found.")

# Function to generate reports
def generate_reports(tasks):
    # Report for percentage of tasks completed by each member
    members = {}
    for task in tasks:
        if task["assigned_to"] not in members:
            members[task["assigned_to"]] = {"total": 0, "completed": 0}
        members[task["assigned_to"]]["total"] += 1
        if task["status"] == "Done":
            members[task["assigned_to"]]["completed"] += 1
    
    print("\nPercentage of tasks completed by each member:")
    for member, data in members.items():
        completed_percentage = (data["completed"] / data["total"]) * 100 if data["total"] > 0 else 0
        print(f"{member}: {completed_percentage:.2f}% completed tasks")

    # Report for pending tasks
    print("\nPending tasks:")
    for task in tasks:
        if task["status"] == "Pending":
            print(f"Task: {task['title']}, Assigned to: {task['assigned_to']}, Priority: {task['priority']}")

# Main interactive menu function
def menu():
    # Preload the list of tasks
    tasks = preload_tasks()

    while True:
        # Display the menu
        print("\n--- Task Management System ---")
        print("1. Register Task")
        print("2. Search Task")
        print("3. Update Task")
        print("4. Delete Completed Task")
        print("5. Generate Reports")
        print("6. Exit")
        
        # Get user choice
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # Prompt for task details and register the task
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            assigned_to = input("Enter name of person assigned to the task: ")
            priority = input("Enter task priority (Low, Medium, High): ")
            status = input("Enter task status (Pending, In progress, Done): ")
            register_task(tasks, title, description, assigned_to, priority, status)

        elif choice == '2':
            # Prompt for search query and display matching tasks
            query = input("Enter task assignee or status to search: ")
            results = search_task(tasks, query)
            if results:
                for result in results:
                    print(f"Task: {result['title']}, Description: {result['description']}, Assigned to: {result['assigned_to']}, Priority: {result['priority']}, Status: {result['status']}")
            else:
                print("No tasks found.")

        elif choice == '3':
            # Prompt for task title to update and new values for priority or status
            task_title = input("Enter task title to update: ")
            new_priority = input("Enter new priority (Low, Medium, High, or leave blank to skip): ")
            new_status = input("Enter new status (Pending, In progress, Done, or leave blank to skip): ")
            update_task(tasks, task_title, new_priority if new_priority else None, new_status if new_status else None)

        elif choice == '4':
            # Prompt for task title to delete
            task_title = input("Enter task title to delete: ")
            delete_task(tasks, task_title)

        elif choice == '5':
            # Generate reports
            generate_reports(tasks)

        elif choice == '6':
            # Exit the system
            print("Exiting the task management system.")
            break

        else:
            # Handle invalid menu choice
            print("Invalid choice. Please try again.")

# Entry point for the program
if __name__ == "__main__":
    menu()
