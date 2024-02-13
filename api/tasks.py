import requests
from data_classes import Task


class TaskAPI:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def create_task(self, task: Task) -> int:
        url = f"{self.base_url}/create-task"
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        json_data = {
            "content": task.content,
            "user_id": str(task.user_id),
            "task_id": str(task.task_id),
            "is_done": task.is_done
        }
        response = requests.put(url, headers=headers, json=json_data)
        return response.status_code

    def create_task_res_json(self, task: Task) -> int:
        url = f"{self.base_url}/create-task"
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        json_data = {
            "content": task.content,
            "user_id": str(task.user_id),
            "task_id": str(task.task_id),
            "is_done": task.is_done
        }
        response = requests.put(url, headers=headers, json=json_data)
        return response.json()

    def update_task(self, updated_task: Task) -> int:
        url = f"{self.base_url}/update-task"

        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        json_data = {
            "content": updated_task.content,
            "user_id": str(updated_task.user_id),
            "task_id": str(updated_task.task_id),
            "is_done": updated_task.is_done
        }

        response = requests.put(url, headers=headers, json=json_data)

        return response.status_code

    def get_task_by_id(self, task_id: str) -> int:
        url = f"{self.base_url}/get-task/{task_id}"

        headers = {
            'accept': 'application/json'
        }

        response = requests.get(url, headers=headers)
        return response.status_code

    def get_task_details(self, task_id: str) -> dict:
        url = f"{self.base_url}/get-task/{task_id}"

        headers = {
            'accept': 'application/json'
        }

        response = requests.get(url, headers=headers)
        return response.json()

    def create_multiple_tasks(self, tasks: list) -> list:
        url = f"{self.base_url}/create-task"
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        created_tasks = []

        for task in tasks:
            task_data = {
                "content": task.content,
                "user_id": str(task.user_id),
                "task_id": str(task.task_id),
                "is_done": task.is_done
            }

            response = requests.put(url, json=task_data, headers=headers)
            if response.status_code == 200:
                created_tasks.append(task_data)
        return created_tasks

    def list_tasks(self, user_id: str) -> list:

        url = f"{self.base_url}/list-tasks/{user_id}"
        headers = {
            'accept': 'application/json'
        }
        response = requests.get(url, headers=headers)

        return response.json()['tasks']

    def delete_all_tasks(self, task_ids: list) -> list:
        headers = {
            'accept': 'application/json'
        }

        deletion_status_codes = []
        for task_id in task_ids:
            url = f"{self.base_url}/delete-task/{task_id}"

            response = requests.delete(url, headers=headers)

            deletion_status_codes.append(response.status_code)
        return deletion_status_codes
