from . import db

class DeliveryHistory(db.Model):
    __tablename__ = 'delivery_history'
    history_id = db.Column(db.Integer, primary_key=True)
    shipment_id = db.Column(db.Integer, db.ForeignKey('shipments.shipment_id'), nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id'), nullable=False)
    action = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def to_dict(self):
        return {
            'history_id': self.history_id,
            'shipment_id': self.shipment_id,
            'employee_id': self.employee_id,
            'action': self.action,
            'timestamp': self.timestamp
        }