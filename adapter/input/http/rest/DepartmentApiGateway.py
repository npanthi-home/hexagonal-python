from flask import Blueprint, request
from entity.Department import Department
from usecase.input.department.CreateDepartment import CreateDepartment
from injector import singleton, inject

department_blueprint = Blueprint('department', __name__)

@singleton
class DepartmentApiGateway:
    @inject
    def __init__(self, createDepartment: CreateDepartment) -> None:
        self.createDepartment = createDepartment

    @department_blueprint.route('/department', methods=['POST'])
    def create(self):
        department_data = request.get_json()
        department = self.createDepartment.apply(Department(**department_data))
        return department

    @department_blueprint.route('/department/<id>', methods=['GET'])
    def get_by_id(self, id):
        department = self.getDepartmentById.execute(id)
        if department:
            return department
        else:
            return "Department not found", 404

    def get_blue_print(self):
        return department_blueprint 
