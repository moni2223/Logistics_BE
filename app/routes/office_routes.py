from flask import Blueprint, request, jsonify
from app.services.office_service import (
    get_all_offices,
    get_office_by_id,
    create_office,
    update_office,
    delete_office
)

bp = Blueprint('office_routes', __name__)

@bp.route('/offices', methods=['GET'])
def get_offices():
    offices = get_all_offices()
    return jsonify([office.to_dict() for office in offices])

@bp.route('/offices/<int:id>', methods=['GET'])
def get_office(id):
    office = get_office_by_id(id)
    return jsonify(office.to_dict())

@bp.route('/offices', methods=['POST'])
def create_office_route():
    data = request.get_json()
    new_office = create_office(data)
    return jsonify(new_office.to_dict()), 201

@bp.route('/offices/<int:id>', methods=['PUT'])
def update_office_route(id):
    data = request.get_json()
    updated_office = update_office(id, data)
    return jsonify(updated_office.to_dict())

@bp.route('/offices/<int:id>', methods=['DELETE'])
def delete_office_route(id):
    delete_office(id)
    return '', 204