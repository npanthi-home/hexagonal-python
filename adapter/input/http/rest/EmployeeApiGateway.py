from injector import inject, singleton
from flask import Blueprint, request
from entity.Employee import Employee
from usecase.output.EmployeeEntityGateway import EmployeeEntityGateway

employee_blueprint = Blueprint('employee', __name__)

@singleton
class EmployeeApiGateway:
    @inject
    def __init__(self, employeeGateway: EmployeeEntityGateway):
        self.employeeGateway = employeeGateway

    @employee_blueprint.post('/employee')
    def create(self):
        employee_data = request.get_json()
        employee = self.employeeGateway.create(Employee(**employee_data))
        return employee

    @employee_blueprint.delete('/employee/<employee_id>')
    def delete_by_id(self, employee_id):
        success = self.employeeGateway.delete(employee_id)
        if success:
            return "Employee deleted successfully"
        else:
            return "Employee not found", 404

    @employee_blueprint.get('/employee/<employee_id>')
    def get_by_id(self, employee_id):
        employee = self.employeeGateway.getById(employee_id)
        if employee:
            return employee
        else:
            return "Employee not found", 404

    @employee_blueprint.get('/employee/department/<department_id>')
    def get_by_department_id(self, department_id):
        employees = self.employeeGateway.getByDepartment(department_id)
        if employees:
            return employees
        else:
            return "No employees found for the department", 404


    def get_blue_print(self):
        return employee_blueprint 
