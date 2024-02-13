from dataclasses import dataclass


@dataclass
class Task:
    content: str
    user_id: int
    task_id: int
    is_done: bool
