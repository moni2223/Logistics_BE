from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models.client import Client
from app.models.employee import Employee
from app.models.enums import Role, Position
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    new_client = Client(
        email=data['email'],
        first_name=data['first_name'],
        last_name=data['last_name']
    )
    new_client.set_password(data['password'])
    db.session.add(new_client)
    db.session.commit()
    print(f"Registered client: {new_client.to_dict()}")
    return jsonify(new_client.to_dict()), 201

@auth_bp.route('/register_employee', methods=['POST'])
@jwt_required()
def register_employee():
    try:
        current_user = get_jwt_identity()
        user_type, user_id = current_user.split(':')
        
        if user_type != "employee":
            return jsonify({"msg": "Access forbidden"}), 403

        employee = Employee.query.get(int(user_id))
        if employee is None or employee.role not in [Role.CEO, Role.MANAGER]:
            return jsonify({"msg": "Access forbidden"}), 403

        data = request.get_json()
        new_employee = Employee(
            email=data['email'],
            password=data['password'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            position=Position.OFFICE if data['position'] == 'OFFICE' else Position.COURIER,
            office_id=data['office_id'],
            role=Role.OFFICE_CLERK if data['role'] == 'OFFICE_CLERK' else Role.COURIER
        )
        db.session.add(new_employee)
        db.session.commit()
        
        return jsonify(new_employee.to_dict()), 201
    except Exception as e:
        print(f"Error registering employee: {str(e)}")
        return jsonify({"msg": "Internal server error"}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        if not data or 'email' not in data or 'password' not in data:
            return jsonify({"msg": "Missing email or password"}), 400

        client = Client.query.filter_by(email=data['email']).first()
        if client and client.check_password(data['password']):
            identity = f"client:{client.client_id}"
            access_token = create_access_token(identity=identity)
            return jsonify(access_token=access_token, user_info=client.to_dict()), 200

        employee = Employee.query.filter_by(email=data['email']).first()
        if employee and employee.check_password(data['password']):
            identity = f"employee:{employee.employee_id}"
            access_token = create_access_token(identity=identity)
            return jsonify(access_token=access_token, user_info=employee.to_dict()), 200

        return jsonify({"msg": "Invalid email or password"}), 401
    except Exception as e:
        print(f"Login error: {str(e)}")
        return jsonify({"msg": "Internal server error"}), 500