from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from .enums import Role, Position
from .office import Office

class Employee(db.Model):
    __tablename__ = 'employees'
    employee_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    position = db.Column(db.Enum(Position), nullable=False)
    office_id = db.Column(db.Integer, db.ForeignKey('offices.office_id'), nullable=False)
    role = db.Column(db.Enum(Role), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, value):
        self.set_password(value)

    def to_dict(self):
        office = Office.query.get(self.office_id)
        return {
            'employee_id': self.employee_id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'position': {
                'position_id': self.position.value,
                'position_name': self.position.name
            },
            'office': {
                'office_id': office.office_id,
                'location': office.location,
                'phone': office.phone
            } if office else None,
            'role': self.role.value
        }