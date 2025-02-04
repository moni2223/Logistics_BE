from flask_jwt_extended import get_jwt_identity
from app import db
from app.models import Shipment, Client, Employee
from app.models.enums import Role

def get_all_shipments():
    current_user = get_jwt_identity()
    user_type, user_id = current_user.split(':')

    if user_type == 'employee':
        employee = Employee.query.get(int(user_id))
        if employee.role == Role.OFFICE_CLERK:
            return Shipment.query.all()
        elif employee.role == Role.COURIER:
            return Shipment.query.filter(Shipment.assigned_courier_id ==user_id).all()
        else:
            return []
    elif user_type == 'client':
        return Shipment.query.filter(
            (Shipment.sender_id == user_id) | (Shipment.recipient_id == user_id)
        ).all()
    else:
        return []

def get_shipment_by_id(shipment_id):
    return Shipment.query.get_or_404(shipment_id)

def create_shipment(data):
    new_shipment = Shipment(**data)
    db.session.add(new_shipment)
    db.session.commit()
    return new_shipment

def update_shipment(shipment_id, data):
    shipment = Shipment.query.get_or_404(shipment_id)
    for key, value in data.items():
        setattr(shipment, key, value)
    db.session.commit()
    return shipment

def delete_shipment(shipment_id):
    shipment = Shipment.query.get_or_404(shipment_id)
    db.session.delete(shipment)
    db.session.commit()