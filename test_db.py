from app import create_app, db
from app.models.enums import Role, Position, ShipmentStatus, DeliveryType
from app.models.client import Client
from app.models.office import Office
from app.models.employee import Employee
from app.models.shipment import Shipment

def init_db():
    app = create_app()
    with app.app_context():
        # Clear database
        db.drop_all()
        db.create_all()

        # Create initial office
        office = Office(
            location="Main Office",
            phone="1234567890"
        )
        db.session.add(office)
        db.session.commit()

        # Create initial employees
        employee1 = Employee(
            email="employee1@example.com",
            first_name="Alice",
            last_name="Johnson",
            position=Position.COURIER,
            office_id=office.office_id,
            role=Role.COURIER
        )
        employee1.set_password("password1")
        db.session.add(employee1)

        employee2 = Employee(
            email="employee2@example.com",
            first_name="Bob",
            last_name="Williams",
            position=Position.COURIER,
            office_id=office.office_id,
            role=Role.COURIER
        )
        employee2.set_password("password2")
        db.session.add(employee2)

        employee3 = Employee(
            email="employee3@example.com",
            first_name="Charlie",
            last_name="Davis",
            position=Position.OFFICE,
            office_id=office.office_id,
            role=Role.OFFICE_CLERK
        )
        employee3.set_password("password3")
        db.session.add(employee3)

        employee4 = Employee(
            email="employee4@example.com",
            first_name="Diana",
            last_name="Evans",
            position=Position.CEO,
            office_id=office.office_id,
            role=Role.CEO
        )
        employee4.set_password("password4")
        db.session.add(employee4)
        db.session.commit()

        # Create initial clients
        client1 = Client(
            email="client1@example.com",
            first_name="John",
            last_name="Doe"
        )
        client1.set_password("password1")
        db.session.add(client1)

        client2 = Client(
            email="client2@example.com",
            first_name="Jane",
            last_name="Smith"
        )
        client2.set_password("password2")
        db.session.add(client2)

        client3 = Client(
            email="client3@example.com",
            first_name="Emily",
            last_name="Brown"
        )
        client3.set_password("password3")
        db.session.add(client3)
        db.session.commit()

        # Create initial shipments
        shipment1 = Shipment(
            sender_id=client1.client_id,
            recipient_id=client2.client_id,
            weight=5.0,
            delivery_type=DeliveryType.OFFICE,
            delivery_address="123 Main St, City, Country",
            price=10.0,
            status=ShipmentStatus.REGISTERED,
            assigned_courier_id=employee1.employee_id
        )
        db.session.add(shipment1)

        shipment2 = Shipment(
            sender_id=client2.client_id,
            recipient_id=client1.client_id,
            weight=2.5,
            delivery_type=DeliveryType.ADDRESS,
            delivery_address="456 Elm St, City, Country",
            price=15.0,
            status=ShipmentStatus.REGISTERED,
            assigned_courier_id=employee2.employee_id
        )
        db.session.add(shipment2)

        shipment3 = Shipment(
            sender_id=client1.client_id,
            recipient_id=client3.client_id,
            weight=3.0,
            delivery_type=DeliveryType.ADDRESS,
            delivery_address="789 Oak St, City, Country",
            price=12.0,
            status=ShipmentStatus.REGISTERED,
            assigned_courier_id=employee1.employee_id
        )
        db.session.add(shipment3)
        db.session.commit()

if __name__ == '__main__':
    init_db()