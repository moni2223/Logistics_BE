from app import db
from app.models import Employee

class EmployeeService:
    def __init__(self, db):
        self.db = db

    def create_employee(self, name, role):
        new_employee = Employee(name=name, role=role)
        self.db.session.add(new_employee)
        self.db.session.commit()
        return new_employee

    def get_employee(self, employee_id):
        return Employee.query.get(employee_id)

    def update_employee(self, employee_id, name=None, role=None):
        employee = self.get_employee(employee_id)
        if employee:
            if name:
                employee.name = name
            if role:
                employee.role = role
            self.db.session.commit()
        return employee

    def delete_employee(self, employee_id):
        employee = self.get_employee(employee_id)
        if employee:
            self.db.session.delete(employee)
            self.db.session.commit()
            return True
        return False

    def get_all_employees(self):
        return Employee.query.all()

def get_all_employees():
    return Employee.query.all()

def get_employee_by_id(employee_id):
    return Employee.query.get_or_404(employee_id)

def create_employee(data):
    new_employee = Employee(**data)
    db.session.add(new_employee)
    db.session.commit()
    return new_employee

def update_employee(employee_id, data):
    employee = Employee.query.get_or_404(employee_id)
    for key, value in data.items():
        setattr(employee, key, value)
    db.session.commit()
    return employee

def delete_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    db.session.delete(employee)
    db.session.commit()