from injector import inject, singleton
from flask import Flask, request
from entity.Employee import Employee
from usecase.output.EmployeeEntityGateway import EmployeeEntityGateway

app = Flask(__name__)

@singleton
class EmployeeApiGateway:
    @inject
    def __init__(self, employeeGateway: EmployeeEntityGateway):
        self.employeeGateway = employeeGateway

    @app.route('/employee', methods=['POST'])
    def createEmployee(self):
        employee_data = request.get_json()
        employee = self.employeeGateway.create(Employee(**employee_data))
        return employee

    @app.route('/employee/<employee_id>', methods=['DELETE'])
    def deleteEmployee(self, employee_id):
        success = self.employeeGateway.delete(employee_id)
        if success:
            return "Employee deleted successfully"
        else:
            return "Employee not found", 404

    @app.route('/employee/<employee_id>', methods=['GET'])
    def getEmployeeById(self, employee_id):
        employee = self.employeeGateway.getById(employee_id)
        if employee:
            return employee
        else:
            return "Employee not found", 404

    @app.route('/employee/department/<department_id>', methods=['GET'])
    def getEmployeeByDepartmentId(self, department_id):
        employees = self.employeeGateway.getByDepartment(department_id)
        if employees:
            return employees
        else:
            return "No employees found for the department", 404
