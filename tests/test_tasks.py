import pytest
from api.tasks import TaskAPI
from data_classes import Task


@pytest.fixture
def task_api():
    base_url = "https://todo.pixegami.io"
    return TaskAPI(base_url)


def test_create_task(task_api):
    new_task = Task(content="Do something", user_id=1, task_id=2, is_done=False)

    response_code = task_api.create_task(new_task)

    assert response_code == 200


def test_update_task(task_api):
    updated_task = Task(content="Updated content", user_id=1, task_id=2, is_done=False)

    response_code = task_api.update_task(updated_task)

    assert response_code == 200


def test_get_task_by_id(task_api):
    sample_task = Task(content="Sample Task", user_id=1, task_id=1, is_done=False)

    response = task_api.create_task_res_json(sample_task)

    created_task_id = response['task']['task_id']

    get_task_status_code = task_api.get_task_by_id(created_task_id)

    assert get_task_status_code == 200


def test_get_task_details(task_api):
    sample_task = Task(content="Sample Task", user_id=1, task_id=1, is_done=False)

    creation_response = task_api.create_task_res_json(sample_task)

    created_task_id = creation_response['task']['task_id']

    response = task_api.get_task_details(created_task_id)

    assert response is not None

    expected_keys = ['content', 'task_id', 'is_done']
    for key in expected_keys:
        assert key in response


def test_create_multiple_tasks(task_api):
    user_id = 1

    tasks_to_create = [
        Task(content="Task 1", user_id=user_id, task_id=1, is_done=False),
        Task(content="Task 2", user_id=user_id, task_id=2, is_done=False),
        Task(content="Task 3", user_id=user_id, task_id=2, is_done=False)
    ]

    created_tasks = task_api.create_multiple_tasks(tasks_to_create)

    assert len(created_tasks) == len(tasks_to_create)

    for task in created_tasks:
        assert task['user_id'] == str(user_id)


def test_list_tasks(task_api):
    user_id = str(1)

    tasks = task_api.list_tasks(user_id)

    assert tasks is not None

    assert isinstance(tasks, list)


def test_delete_all_tasks(task_api):
    task_ids = [str(1), str(2), str(3)]

    deletion_status_codes = task_api.delete_all_tasks(task_ids)

    assert len(deletion_status_codes) == len(task_ids)

    for status_code in deletion_status_codes:
        assert status_code in [200, 204]
