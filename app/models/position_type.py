from . import db

class PositionType(db.Model):
    __tablename__ = 'positionTypes'
    position_id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String, nullable=False)

    def to_dict(self):
        return {
            'position_id': self.position_id,
            'position': self.position
        }