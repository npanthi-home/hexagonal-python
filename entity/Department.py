from dataclasses import dataclass, field
import uuid

@dataclass(frozen=True, kw_only=True, slots=True)
class Department:
    id: str = field(init=False, default_factory=lambda: str(uuid.uuid4()))
    name: str = None
    employee_count: int = 0
