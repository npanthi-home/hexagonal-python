from flask import Flask
from injector import Injector

from adapter.input.http.rest.DepartmentApiGateway import DepartmentApiGateway
from adapter.input.http.rest.EmployeeApiGateway import EmployeeApiGateway
from framework.app.AdapterModule import AdapterModule
from framework.app.FrameworkModule import FrameworkModule
from framework.app.UsecaseModule import UsecaseModule

class Application:
    def __init__(self) -> None:
        self.runner = Flask(__name__)
        modules = [AdapterModule, UsecaseModule, FrameworkModule]
        self.injector = Injector(modules)

    def run(self):
        department_api_gateway = self.injector.get(DepartmentApiGateway)
        self.runner.add_url_rule('/department', 'create', department_api_gateway.create, methods=['POST'])
        self.runner.add_url_rule('/department/<id>', 'getById', department_api_gateway.getById, methods=['GET'])
        self.runner.run()