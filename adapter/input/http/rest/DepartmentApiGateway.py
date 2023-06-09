from flask import Flask, jsonify, request
from entity.Department import Department
from usecase.input.department.CreateDepartment import CreateDepartment
from injector import singleton, inject

app = Flask(__name__)

@singleton
class DepartmentApiGateway:
    @inject
    def __init__(self, createDepartment: CreateDepartment) -> None:
        self.createDepartment = createDepartment

    @app.route('/department', methods=['POST'])
    def create(self):
        department_data = request.get_json()
        department = self.createDepartment.apply(Department(**department_data))
        return department

    @app.route('/department/<id>', methods=['GET'])
    def getById(self, id):
        department = self.getDepartmentById.execute(id)
        if department:
            return department
        else:
            return "Department not found", 404
