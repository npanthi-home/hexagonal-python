from injector import inject, singleton
from entity.Department import Department
from usecase.output.DepartmentEntityGateway import DepartmentEntityGateway

@singleton
class CreateDepartment:
    @inject
    def __init__(self, gateway: DepartmentEntityGateway):
        self.gateway = gateway

    def apply(self, department: Department) -> Department:
        return self.gateway.create(department)