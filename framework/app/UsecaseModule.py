from injector import Module, singleton
from usecase.input.department.CreateDepartment import CreateDepartment
from usecase.input.department.GetDepartmentById import GetDepartmentById
from usecase.input.employee.CreateEmployee import CreateEmployee


class UsecaseModule(Module):
    def configure(self, binder):
        binder.bind(CreateDepartment, to=CreateDepartment, scope=singleton)
        binder.bind(CreateEmployee, to=CreateEmployee, scope=singleton)
        binder.bind(GetDepartmentById, to=GetDepartmentById, scope=singleton)
