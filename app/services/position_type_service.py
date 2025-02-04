from app import db
from app.models import  PositionType

def get_all_position_types():
    return PositionType.query.all()

def get_position_type_by_id(position_type_id):
    return PositionType.query.get_or_404(position_type_id)

def create_position_type(data):
    new_position_type = PositionType(**data)
    db.session.add(new_position_type)
    db.session.commit()
    return new_position_type

def update_position_type(position_type_id, data):
    position_type = PositionType.query.get_or_404(position_type_id)
    for key, value in data.items():
        setattr(position_type, key, value)
    db.session.commit()
    return position_type

def delete_position_type(position_type_id):
    position_type = PositionType.query.get_or_404(position_type_id)
    db.session.delete(position_type)
    db.session.commit()