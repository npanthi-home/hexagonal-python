from injector import inject, singleton
from entity.Employee import Employee
from usecase.output.EmployeeEntityGateway import EmployeeEntityGateway

@singleton
class CreateEmployee:
    @inject
    def __init__(self, gateway: EmployeeEntityGateway):
        self.gateway = gateway

    def apply(self, employee: Employee) -> Employee:
        return self.gateway.create(employee)
