from dataclasses import dataclass, field
import uuid
from entity.Department import Department


@dataclass
class Employee:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = None
    age: int = None
    department: Department = None
    salary: float = None