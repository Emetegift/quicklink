from flask import Flask, jsonify, make_response
from api.extensions import db, migrate, jwt, api, cache
# from .extensions import db, migrate, jwt, api, cache
from flask_jwt_extended import JWTManager
from .config.config import config_dict
# from .config import config_object
from .models import User, Link, RevokedToken
from .auth import blp as auth_blp
from .views.users import blp as users_blp
from .views.urls import blp as urls_blp
from flask_cors import CORS
from flask_migrate import Migrate

def create_app(config=config_dict['dev']):
    
    app = Flask(__name__)
    
    app.config.from_object(config)
    
    db.init_app(app)
    
    migrate = Migrate(app,db)
    
    migrate.init_app(app, db)
    
    api.init_app(app)
    
    JWTManager(app)
    
    # Enable CORS
    CORS(app, resupports_credentials=True)
    cache.init_app(app)
    jwt.init_app(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {"description": "The token has been revoked.", "error": "token_revoked"}
            ),
            401,
        )

    @jwt.additional_claims_loader
    def add_additional_claims(identity):
        if identity == 1:
            return {"is_admin": True}
        return {"is_admin": False}

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

    # Callback function to check if a JWT exists in the database blocklist
    @jwt.token_in_blocklist_loader
    def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
        jti = jwt_payload["jti"]
        token = db.session.query(RevokedToken.id).filter_by(jti=jti).scalar()

        return token is not None

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has expired.", "error": "token_expired"}),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )

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

    api.register_blueprint(auth_blp)
    api.register_blueprint(users_blp)
    api.register_blueprint(urls_blp)

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({"error": "Not found"}), 404)

    @app.shell_context_processor
    def make_shell_context():
        return {
            'db': db, 
            'User': User, 
            'Link': Link
            }

    return app
