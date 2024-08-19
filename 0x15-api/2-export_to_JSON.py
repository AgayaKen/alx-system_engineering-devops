#!/usr/bin/python3
"""
Employee TODO List Progress

This script fetches and displays the TODO list progress for a given employee ID using a REST API.
It also exports the data in JSON format.
"""

import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetch and display the TODO list progress for a given employee ID.
    Export the data in JSON format.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee details
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data.get("name")
    username = user_data.get("username")

    # Fetch employee's TODO list
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todos_data = todos_response.json()

    # Calculate the number of completed and total tasks
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get("completed")]
    number_of_done_tasks = len(done_tasks)

    # Display the TODO list progress
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

    # Prepare data for JSON export
    tasks = [{"task": task.get("title"), "completed": task.get("completed"), "username": username} for task in todos_data]
    data = {str(employee_id): tasks}

    # Export data to JSON file
    with open(f"{employee_id}.json", "w") as json_file:
        json.dump(data, json_file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

