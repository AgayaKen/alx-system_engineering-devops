#!/usr/bin/python3
"""
Employee TODO List Progress

This script fetches and displays the TODO list progress for a given employee ID using a REST API.
It also exports the data in CSV format.
"""

import csv
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetch and display the TODO list progress for a given employee ID.
    Export the data in CSV format.

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

    # Prepare data for CSV export
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for task in todos_data:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": username,
                "TASK_COMPLETED_STATUS": task.get("completed"),
                "TASK_TITLE": task.get("title")
            })

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
