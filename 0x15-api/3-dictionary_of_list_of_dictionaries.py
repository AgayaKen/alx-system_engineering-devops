#!/usr/bin/python3
"""
Employee TODO List Progress

This script fetches and displays the TODO list progress for all employees using a REST API.
It also exports the data in JSON format.
"""

import json
import requests


def get_all_employees_todo_progress():
    """
    Fetch and display the TODO list progress for all employees.
    Export the data in JSON format.

    Returns:
        None
    """
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch all employees
    users_response = requests.get(f"{base_url}/users")
    users_data = users_response.json()

    # Dictionary to hold all tasks for all employees
    all_tasks = {}

    for user in users_data:
        employee_id = user.get("id")
        username = user.get("username")

        # Fetch employee's TODO list
        todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
        todos_data = todos_response.json()

        # Prepare tasks for the current employee
        tasks = [{"username": username, "task": task.get("title"),
                  "completed": task.get("completed")} for task in todos_data]
        all_tasks[str(employee_id)] = tasks

    # Export data to JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file, indent=4)


if __name__ == "__main__":
    get_all_employees_todo_progress()

