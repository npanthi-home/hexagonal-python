from flask import Flask
from injector import Injector
from adapter.input.http.rest.DepartmentApiGateway import DepartmentApiGateway, department_blueprint
from adapter.input.http.rest.EmployeeApiGateway import EmployeeApiGateway, employee_blueprint 

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
        employee_api_gateway = self.injector.get(EmployeeApiGateway)
        self.runner.register_blueprint(department_api_gateway.get_blue_print())
        self.runner.register_blueprint(employee_api_gateway.get_blue_print())
        self.__log_site_map()
        self.runner.run()

    def __log_site_map(self):
        for rule in self.runner.url_map.iter_rules():
            print("{}".format(rule.endpoint))

    