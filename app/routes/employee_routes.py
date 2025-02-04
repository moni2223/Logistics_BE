from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.employee_service import (
    get_all_employees,
    get_employee_by_id,
    create_employee,
    update_employee,
    delete_employee
)
from app.models import Employee

bp = Blueprint('employee_routes', __name__)

def check_role(required_roles):
    def wrapper(fn):
        @jwt_required()
        def decorator(*args, **kwargs):
            current_user = get_jwt_identity()
            if current_user["type"] != "employee":
                return jsonify({"msg": "Access forbidden"}), 403

            employee = Employee.query.get(current_user["id"])
            if employee is None:
                return jsonify({"msg": "User not found"}), 404
            if employee.role not in required_roles:
                return jsonify({"msg": "Access forbidden"}), 403
            return fn(*args, **kwargs)
        return decorator
    return wrapper

@bp.route('/employees', methods=['GET'], endpoint='get_employees')
@jwt_required()
def get_employees():
    employees = get_all_employees()
    return jsonify([employee.to_dict() for employee in employees])

@bp.route('/employees/<int:id>', methods=['GET'], endpoint='get_employee')
@jwt_required()
def get_employee(id):
    employee = get_employee_by_id(id)
    return jsonify(employee.to_dict())

@bp.route('/employees', methods=['POST'], endpoint='create_employee')
@check_role(['CEO', 'Manager'])
def create_employee_route():
    data = request.get_json()
    new_employee = create_employee(data)
    return jsonify(new_employee.to_dict()), 201

@bp.route('/employees/<int:id>', methods=['PUT'], endpoint='update_employee')
@check_role(['CEO', 'Manager'])
def update_employee_route(id):
    data = request.get_json()
    updated_employee = update_employee(id, data)
    return jsonify(updated_employee.to_dict())

@bp.route('/employees/<int:id>', methods=['DELETE'], endpoint='delete_employee')
@check_role(['CEO'])
def delete_employee_route(id):
    delete_employee(id)
    return '', 204