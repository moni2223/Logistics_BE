from app import db
from .enums import ShipmentStatus, DeliveryType
from .client import Client
from .employee import Employee

class Shipment(db.Model):
    __tablename__ = 'shipments'
    shipment_id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('clients.client_id'), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey('clients.client_id'), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    delivery_type = db.Column(db.Enum(DeliveryType), nullable=False)
    delivery_address = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.Enum(ShipmentStatus), nullable=False, default=ShipmentStatus.REGISTERED)
    assigned_courier_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id'))

    def to_dict(self):
        sender = Client.query.get(self.sender_id)
        recipient = Client.query.get(self.recipient_id)
        assigned_courier = Employee.query.get(self.assigned_courier_id)
        return {
            'shipment_id': self.shipment_id,
            'sender': {
                'client_id': sender.client_id,
                'email': sender.email,
                'first_name': sender.first_name,
                'last_name': sender.last_name
            },
            'recipient': {
                'client_id': recipient.client_id,
                'email': recipient.email,
                'first_name': recipient.first_name,
                'last_name': recipient.last_name
            },
            'weight': self.weight,
            'delivery_type': self.delivery_type.value,
            'delivery_address': self.delivery_address,
            'price': self.price,
            'status': self.status.value,
            'assigned_courier': {
                'employee_id': assigned_courier.employee_id,
                'email': assigned_courier.email,
                'first_name': assigned_courier.first_name,
                'last_name': assigned_courier.last_name
            } if assigned_courier else None
        }