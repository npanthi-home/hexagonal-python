Project Name

Project description goes here.


Table of Contents

- Introduction
- Hexagonal Architecture
- Project Structure
- Installation
- Usage
- API Documentation
- Contributing
- License


Introduction

This project implements a Python application that follows the Hexagonal Architecture pattern. It provides a REST API for managing employees and departments. The application uses MySQL as the database for storing employee and department data.

The Hexagonal Architecture, also known as Ports and Adapters, is a software design pattern that promotes loose coupling, separation of concerns, and testability. It emphasizes the core business logic of the application and isolates it from external dependencies such as databases, frameworks, or APIs.

In this project, the core business logic is encapsulated in the domain layer, which consists of the employee and department entities. The application uses adapters to interact with external systems, such as the MySQL database and the REST API. This separation allows for flexibility and easy swapping of adapters if needed.


Hexagonal Architecture

The Hexagonal Architecture consists of the following components:

1. Domain Layer: Contains the core business logic and defines the employee and department entities. It represents the heart of the application and is independent of any external systems.
2. Adapters:
   - Persistence Adapter: Implements the logic to save and retrieve employee and department data from the MySQL database.
   - REST Adapter: Provides a RESTful API for interacting with the application. It handles incoming requests, maps them to the appropriate use cases, and returns responses.
3. Application Layer: Implements the use cases or application-specific operations. It acts as a bridge between the external systems and the domain layer, utilizing the adapters to perform operations on employee and department entities.
4. Infrastructure Layer: Contains the implementation details of the adapters and any other external dependencies. It provides the necessary configurations, drivers, and libraries required by the adapters to interact with the external systems.


Project Structure

The project follows the following structure:

project_name/
- app/
  - adapters/
    - persistence/
      - employee_repository.py
      - department_repository.py
    - rest/
      - employee_controller.py
      - department_controller.py
  - domain/
    - employee.py
    - department.py
  - application/
    - employee_service.py
    - department_service.py
- config/
  - database.py
  - app_config.py
- requirements.txt
- README.txt
- .gitignore
- LICENSE


Installation

1. Clone the project repository.
2. Create a virtual environment: `python -m venv env`
3. Activate the virtual environment:
   - For Windows: `env\Scripts\activate`
   - For Unix/macOS: `source env/bin/activate`
4. Install project dependencies: `pip install -r requirements.txt`


Usage

1. Configure the MySQL database connection in the `config/database.py` file.
2. Start the application: `python app/adapters/rest/employee_controller.py`
3. Access the REST API endpoints using a tool like cURL or Postman.


API Documentation

The API documentation can be found in the project's documentation folder or by accessing the API endpoints.


Contributing

Contributions are welcome! If you find any issues or want to enhance the project, please submit a pull request.


License

This project is licensed under the CC BY 4.0. You can find more details in the LICENSE file.

