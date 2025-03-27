from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import os

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    jwt.init_app(app)

    from app.routes import customer_routes, employee_routes, shipment_routes, office_routes, position_type_routes, auth_routes

    app.register_blueprint(customer_routes.bp)
    app.register_blueprint(employee_routes.bp)
    app.register_blueprint(shipment_routes.bp)
    app.register_blueprint(office_routes.bp)
    app.register_blueprint(position_type_routes.bp)
    app.register_blueprint(auth_routes.auth_bp)

    return app
