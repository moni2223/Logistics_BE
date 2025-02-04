from flask import Blueprint

bp = Blueprint('routes', __name__)

from . import customer_routes, employee_routes, shipment_routes, office_routes, position_type_routes, auth_routes