from dataclasses import dataclass, field
import time

from entity.Employee import Employee

@dataclass
class Notification:
    employee: Employee = None
    timestamp: int = field(default=int(time.time()))
    message: str = None