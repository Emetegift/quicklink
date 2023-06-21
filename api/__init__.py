from flask import Flask, jsonify, make_response
from api.extensions import db, migrate, jwt, api, cache
# from .extensions import db, migrate, jwt, api, cache
from flask_jwt_extended import JWTManager
from .config.config import config_dict
# from .config import config_object
from .models import User, Link, RevokedToken, Click
from .auth import blp as auth_blp
from .views.users import blp as users_blp
from .views.urls import blp as urls_blp
from flask_cors import CORS
from flask_migrate import Migrate

def create_app(config=config_dict['dev']):
    # Create the Flask application
    app = Flask(__name__)
    
    # Load the application configuration from the config object
    app.config.from_object(config)
    
    # Initialize the database extension
    db.init_app(app)
    
    # Initialize the migration extension
    migrate = Migrate(app,db)
    
    # Initialize the migration commands for the Flask-Script extension
    migrate.init_app(app, db)
    
    # Initialize the API extension
    api.init_app(app)
    
    # Initialize the JWTManager extension
    JWTManager(app)
    
    # Enable CORS for the application, allowing requests from http://localhost:3000
    CORS(app, resources={r"/*": {"origins": "https://quicklink-d8m7n36ma-emetegift.vercel.app"}})
    # CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
    # CORS(app, resupports_credentials=True)
    
    # Initialize the cache extension
    cache.init_app(app)
    
    # Initialize the JWT extension
    jwt.init_app(app)

    # Configure the response headers after each request to allow CORS and other headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        # response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    # Define the callback function for revoked tokens
    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {"description": "The token has been revoked.", "error": "token_revoked"}
            ),
            401,
        )

    # Define the callback function to add additional claims to the JWT payload
    @jwt.additional_claims_loader
    def add_additional_claims(identity):
        if identity == 1:
            return {"is_admin": True}
        return {"is_admin": False}

    # Define the callback function for fresh tokens
    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {
                    "description": "The token is not fresh.",
                    "error": "fresh_token_required",
                }
            ),
            401,
        )

    # Define the callback function to check if a JWT exists in the database blocklist
    @jwt.token_in_blocklist_loader
    def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
        jti = jwt_payload["jti"]
        token = db.session.query(RevokedToken.id).filter_by(jti=jti).scalar()

        return token is not None

    # Define the callback function for expired tokens
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has expired.", "error": "token_expired"}),
            401,
        )

    # Define the callback function for invalid tokens
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )

    # Define the callback function for missing tokens
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
            ),
            401,
        )

    # Register the blueprints for authentication, users, and URLs
    api.register_blueprint(auth_blp)
    api.register_blueprint(users_blp)
    api.register_blueprint(urls_blp)

    # Define the error handler for 404 Not Found
    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({"error": "Not found"}), 404)

    # Define the shell context for the Flask CLI
    @app.shell_context_processor
    def make_shell_context():
        return {
            'db': db, 
            'User': User, 
            'Link': Link,
            'Click': Click
        }

    return app
