from flask import Flask
from injector import Injector
from injector import singleton

from adapter.input.http.rest.DepartmentApiGateway import DepartmentApiGateway
from adapter.input.http.rest.EmployeeApiGateway import EmployeeApiGateway
from adapter.output.mysql.DepartmentMysqlGateway import DepartmentMysqlGateway
from adapter.output.mysql.EmployeeMysqlGateway import EmployeeMysqlGateway

from usecase.input.employee.CreateEmployee import CreateEmployee
from usecase.input.department.CreateDepartment import CreateDepartment
from usecase.input.department.GetDepartmentById import GetDepartmentById
from usecase.output.DepartmentEntityGateway import DepartmentEntityGateway
from usecase.output.EmployeeEntityGateway import EmployeeEntityGateway

class Application:
    def __init__(self) -> None:
        self.runner = Flask(__name__)
        self.injector = Injector()
        self.injector.binder = self.configure

    def configure(self, binder):
        binder.bind(DepartmentApiGateway, to=DepartmentApiGateway, scope=singleton)
        binder.bind(EmployeeApiGateway, to=EmployeeApiGateway, scope=singleton)
        binder.bind(CreateDepartment, to=CreateDepartment, scope=singleton)
        binder.bind(CreateEmployee, to=CreateEmployee, scope=singleton)
        binder.bind(GetDepartmentById, to=GetDepartmentById, scope=singleton)
        binder.bind(DepartmentEntityGateway, to=DepartmentMysqlGateway, scope=singleton)
        binder.bind(EmployeeEntityGateway, to=EmployeeMysqlGateway, scope=singleton)

    def run(self):
        department_api_gateway = self.injector.get(DepartmentApiGateway)
        self.runner.add_url_rule('/department', 'create', department_api_gateway.create, methods=['POST'])
        self.runner.add_url_rule('/department/<id>', 'getById', department_api_gateway.getById, methods=['GET'])
        self.runner.run()