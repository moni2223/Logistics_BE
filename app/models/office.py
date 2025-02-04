from app import db

class Office(db.Model):
    __tablename__ = 'offices'
    office_id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.Text, nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {
            'office_id': self.office_id,
            'location': self.location,
            'phone': self.phone
        }