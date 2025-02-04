from app import db
from app.models import  Office

def get_all_offices():
    return Office.query.all()

def get_office_by_id(office_id):
    return Office.query.get_or_404(office_id)

def create_office(data):
    new_office = Office(**data)
    db.session.add(new_office)
    db.session.commit()
    return new_office

def update_office(office_id, data):
    office = Office.query.get_or_404(office_id)
    for key, value in data.items():
        setattr(office, key, value)
    db.session.commit()
    return office

def delete_office(office_id):
    office = Office.query.get_or_404(office_id)
    db.session.delete(office)
    db.session.commit()