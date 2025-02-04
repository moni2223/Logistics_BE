from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from app import db
from app.services.customer_service import (
    get_all_customers,
    get_customer_by_id,
    create_customer,
    update_customer,
    delete_customer
)


bp = Blueprint('customer_routes', __name__)

@bp.route('/customers', methods=['GET'])
def get_customers():
    customers = get_all_customers()
    return jsonify([customer.to_dict() for customer in customers])

@bp.route('/customers/<int:id>', methods=['GET'])
def get_customer(id):
    customer = get_customer_by_id(id)
    return jsonify(customer.to_dict())

@bp.route('/customers', methods=['POST'])
def create_customer_route():
    data = request.get_json()
    try:
        new_customer = create_customer(data)
        return jsonify(new_customer.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Email already exists"}), 400

@bp.route('/customers/<int:id>', methods=['PUT'])
def update_customer_route(id):
    data = request.get_json()
    updated_customer = update_customer(id, data)
    return jsonify(updated_customer.to_dict())

@bp.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer_route(id):
    delete_customer(id)
    return '', 204