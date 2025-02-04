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

        # Create initial offices
        offices = [
            Office(location="Main Office", phone="1234567890"),
            Office(location="Downtown Office", phone="2345678901"),
            Office(location="Uptown Office", phone="3456789012"),
            Office(location="Eastside Office", phone="4567890123"),
            Office(location="Westside Office", phone="5678901234")
        ]
        for office in offices:
            db.session.add(office)
        db.session.commit()

        # Create initial employees
        employees = [
            Employee(email="employee1@example.com", first_name="Alice", last_name="Johnson", position=Position.COURIER, office_id=offices[0].office_id, role=Role.COURIER),
            Employee(email="employee2@example.com", first_name="Bob", last_name="Williams", position=Position.COURIER, office_id=offices[0].office_id, role=Role.COURIER),
            Employee(email="employee3@example.com", first_name="Charlie", last_name="Davis", position=Position.OFFICE, office_id=offices[0].office_id, role=Role.OFFICE_CLERK),
            Employee(email="employee4@example.com", first_name="Diana", last_name="Evans", position=Position.CEO, office_id=offices[0].office_id, role=Role.CEO),
            Employee(email="employee5@example.com", first_name="Eve", last_name="Brown", position=Position.COURIER, office_id=offices[1].office_id, role=Role.COURIER),
            Employee(email="employee6@example.com", first_name="Frank", last_name="Miller", position=Position.OFFICE, office_id=offices[1].office_id, role=Role.OFFICE_CLERK),
            Employee(email="employee7@example.com", first_name="Grace", last_name="Wilson", position=Position.COURIER, office_id=offices[2].office_id, role=Role.COURIER),
            Employee(email="employee8@example.com", first_name="Hank", last_name="Moore", position=Position.OFFICE, office_id=offices[2].office_id, role=Role.OFFICE_CLERK),
            Employee(email="employee9@example.com", first_name="Ivy", last_name="Taylor", position=Position.COURIER, office_id=offices[3].office_id, role=Role.COURIER),
            Employee(email="employee10@example.com", first_name="Jack", last_name="Anderson", position=Position.OFFICE, office_id=offices[3].office_id, role=Role.OFFICE_CLERK),
            Employee(email="employee11@example.com", first_name="Karen", last_name="Thomas", position=Position.COURIER, office_id=offices[4].office_id, role=Role.COURIER),
            Employee(email="employee12@example.com", first_name="Leo", last_name="Jackson", position=Position.OFFICE, office_id=offices[4].office_id, role=Role.OFFICE_CLERK)
        ]
        for i, employee in enumerate(employees, start=1):
            employee.set_password(f"password{i}")
            db.session.add(employee)
        db.session.commit()

        # Create initial clients
        clients = [
            Client(email="client1@example.com", first_name="John", last_name="Doe"),
            Client(email="client2@example.com", first_name="Jane", last_name="Smith"),
            Client(email="client3@example.com", first_name="Emily", last_name="Brown"),
            Client(email="client4@example.com", first_name="Michael", last_name="Johnson"),
            Client(email="client5@example.com", first_name="Sarah", last_name="Davis"),
            Client(email="client6@example.com", first_name="David", last_name="Wilson"),
            Client(email="client7@example.com", first_name="Laura", last_name="Martinez"),
            Client(email="client8@example.com", first_name="James", last_name="Garcia"),
            Client(email="client9@example.com", first_name="Linda", last_name="Rodriguez"),
            Client(email="client10@example.com", first_name="Robert", last_name="Hernandez")
        ]
        for i, client in enumerate(clients, start=1):
            client.set_password(f"password{i}")
            db.session.add(client)
        db.session.commit()

        # Create initial shipments
        shipments = [
            Shipment(sender_id=clients[0].client_id, recipient_id=clients[1].client_id, weight=5.0, delivery_type=DeliveryType.OFFICE, delivery_address="123 Main St, City, Country", price=10.0, status=ShipmentStatus.REGISTERED, assigned_courier_id=employees[0].employee_id),
            Shipment(sender_id=clients[1].client_id, recipient_id=clients[0].client_id, weight=2.5, delivery_type=DeliveryType.ADDRESS, delivery_address="456 Elm St, City, Country", price=15.0, status=ShipmentStatus.REGISTERED, assigned_courier_id=employees[1].employee_id),
            Shipment(sender_id=clients[0].client_id, recipient_id=clients[2].client_id, weight=3.0, delivery_type=DeliveryType.ADDRESS, delivery_address="789 Oak St, City, Country", price=12.0, status=ShipmentStatus.REGISTERED, assigned_courier_id=employees[0].employee_id),
            Shipment(sender_id=clients[3].client_id, recipient_id=clients[4].client_id, weight=4.0, delivery_type=DeliveryType.OFFICE, delivery_address="321 Pine St, City, Country", price=8.0, status=ShipmentStatus.REGISTERED, assigned_courier_id=employees[4].employee_id),
            Shipment(sender_id=clients[5].client_id, recipient_id=clients[6].client_id, weight=6.0, delivery_type=DeliveryType.ADDRESS, delivery_address="654 Cedar St, City, Country", price=20.0, status=ShipmentStatus.REGISTERED, assigned_courier_id=employees[6].employee_id),
            Shipment(sender_id=clients[7].client_id, recipient_id=clients[8].client_id, weight=1.5, delivery_type=DeliveryType.OFFICE, delivery_address="987 Birch St, City, Country", price=5.0, status=ShipmentStatus.REGISTERED, assigned_courier_id=employees[8].employee_id),
            Shipment(sender_id=clients[9].client_id, recipient_id=clients[3].client_id, weight=7.0, delivery_type=DeliveryType.ADDRESS, delivery_address="135 Maple St, City, Country", price=25.0, status=ShipmentStatus.REGISTERED, assigned_courier_id=employees[10].employee_id)
        ]
        for shipment in shipments:
            db.session.add(shipment)
        db.session.commit()

if __name__ == '__main__':
    init_db()