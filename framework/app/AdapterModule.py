from injector import Module
from injector import singleton

from adapter.input.http.rest.DepartmentApiGateway import DepartmentApiGateway
from adapter.input.http.rest.EmployeeApiGateway import EmployeeApiGateway
from adapter.output.mysql.DepartmentMysqlGateway import DepartmentMysqlGateway
from adapter.output.mysql.EmployeeMysqlGateway import EmployeeMysqlGateway

from usecase.output.DepartmentEntityGateway import DepartmentEntityGateway
from usecase.output.EmployeeEntityGateway import EmployeeEntityGateway

class AdapterModule(Module):
    def configure(self, binder):
        binder.bind(DepartmentApiGateway, to=DepartmentApiGateway, scope=singleton)
        binder.bind(EmployeeApiGateway, to=EmployeeApiGateway, scope=singleton)
        binder.bind(DepartmentEntityGateway, to=DepartmentMysqlGateway, scope=singleton)
        binder.bind(EmployeeEntityGateway, to=EmployeeMysqlGateway, scope=singleton)
