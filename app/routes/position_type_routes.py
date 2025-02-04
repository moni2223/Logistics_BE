from flask import Blueprint, request, jsonify
from app.services.position_type_service import (
    get_all_position_types,
    get_position_type_by_id,
    create_position_type,
    update_position_type,
    delete_position_type
)

bp = Blueprint('position_type_routes', __name__)

@bp.route('/position_types', methods=['GET'])
def get_position_types():
    position_types = get_all_position_types()
    return jsonify([position_type.to_dict() for position_type in position_types])

@bp.route('/position_types/<int:id>', methods=['GET'])
def get_position_type(id):
    position_type = get_position_type_by_id(id)
    return jsonify(position_type.to_dict())

@bp.route('/position_types', methods=['POST'])
def create_position_type_route():
    data = request.get_json()
    new_position_type = create_position_type(data)
    return jsonify(new_position_type.to_dict()), 201

@bp.route('/position_types/<int:id>', methods=['PUT'])
def update_position_type_route(id):
    data = request.get_json()
    updated_position_type = update_position_type(id, data)
    return jsonify(updated_position_type.to_dict())

@bp.route('/position_types/<int:id>', methods=['DELETE'])
def delete_position_type_route(id):
    delete_position_type(id)
    return '', 204