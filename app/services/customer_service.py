from app import db
from app.models import Client

class CustomerService:
    def create_customer(self, name, email):
        new_customer = Client(name=name, email=email)
        db.session.add(new_customer)
        db.session.commit()
        return new_customer

    def get_customer(self, customer_id):
        return Client.query.get_or_404(customer_id)

    def update_customer(self, customer_id, name=None, email=None):
        customer = self.get_customer(customer_id)
        if customer:
            if name:
                customer.name = name
            if email:
                customer.email = email
            db.session.commit()
        return customer

    def delete_customer(self, customer_id):
        customer = self.get_customer(customer_id)
        if customer:
            db.session.delete(customer)
            db.session.commit()
        return customer

def get_all_customers():
    return Client.query.all()

def get_customer_by_id(customer_id):
    return Client.query.get_or_404(customer_id)

def create_customer(data):
    new_customer = Client(**data)
    db.session.add(new_customer)
    db.session.commit()
    return new_customer

def update_customer(customer_id, data):
    customer = Client.query.get_or_404(customer_id)
    for key, value in data.items():
        setattr(customer, key, value)
    db.session.commit()
    return customer

def delete_customer(customer_id):
    customer = Client.query.get_or_404(customer_id)
    db.session.delete(customer)
    db.session.commit()