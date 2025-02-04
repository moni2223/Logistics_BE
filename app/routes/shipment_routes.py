from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.shipment_service import (
    get_all_shipments,
    get_shipment_by_id,
    create_shipment,
    update_shipment,
    delete_shipment
)

bp = Blueprint('shipment_routes', __name__)

@bp.route('/shipments', methods=['GET'])
@jwt_required()
def get_shipments():
    shipments = get_all_shipments()
    return jsonify([shipment.to_dict() for shipment in shipments])

@bp.route('/shipments/<int:id>', methods=['GET'])
def get_shipment(id):
    shipment = get_shipment_by_id(id)
    return jsonify(shipment.to_dict())

@bp.route('/shipments', methods=['POST'])
def create_shipment_route():
    data = request.get_json()
    new_shipment = create_shipment(data)
    return jsonify(new_shipment.to_dict()), 201

@bp.route('/shipments/<int:id>', methods=['PUT'])
def update_shipment_route(id):
    data = request.get_json()
    updated_shipment = update_shipment(id, data)
    return jsonify(updated_shipment.to_dict())

@bp.route('/shipments/<int:id>', methods=['DELETE'])
def delete_shipment_route(id):
    delete_shipment(id)
    return '', 204