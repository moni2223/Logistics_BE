from enum import Enum

class Role(Enum):
    CEO = "CEO"
    MANAGER = "Manager"
    OFFICE_CLERK = "Office_clerk"
    COURIER = "Courier"

class Position(Enum):
    OFFICE = 1
    COURIER = 2
    MANAGER = 3
    CEO = 4

class ShipmentStatus(Enum):
    REGISTERED = "Registered"
    IN_TRANSIT = "In Transit"
    DELIVERED = "Delivered"

class DeliveryType(Enum):
    OFFICE = "Office"
    ADDRESS = "Address"