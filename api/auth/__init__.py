from flask import jsonify, request
from werkzeug.exceptions import BadRequest
from ..models import User, RevokedToken, Link
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from ..schemas import UserSchema, LoginSchema
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required, get_jwt
from ..utils import check_if_email_is_unique, check_if_username_is_unique
from passlib.hash import pbkdf2_sha256 as sha256
from datetime import timedelta
from ..extensions import db
from ..extensions import cache
from werkzeug.security import generate_password_hash, check_password_hash

blp = Blueprint("auth", __name__, description="Operations on Authentication")




@blp.route('/register', methods=['POST'])
@blp.arguments(UserSchema, as_kwargs=True)
@blp.response(200, UserSchema(many=False))
def register(username, email, first_name, last_name, password, confirm_password):
    try:
        data = request.get_json()  # Get JSON data from the request
        
        # Check if username or email already exists
        if User.query.filter_by(username=username).first():
            return jsonify({'error': 'Username already exists.'}), 400
        if User.query.filter_by(email=email).first():
            return jsonify({'error': 'Email already exists.'}), 400
        
        # Create the user and save it to the database
        user = User.create_user(username, password, email, first_name, last_name)
        
        # Update the user_links for the created user
        # Assuming you have the link data available in the request payload
        link_data = data.get('links', [])
        for link in link_data:
            # Create Link objects and associate them with the user
            link_obj = Link(original_url=link['original_url'], short_url=link['short_url'], user_links=user)  # Update the variable names
            db.session.add(link_obj)
        
        db.session.commit()  # Commit the changes to the database
        
        return jsonify({'message': 'User created successfully'}), 201
    except KeyError as e:
        raise BadRequest(f"Missing required field: {str(e)}")
    except Exception as e:
        raise BadRequest(f"An error occurred: {str(e)}")



@blp.route("/login")
class LoginUserResource(MethodView):
    @blp.arguments(LoginSchema)
    def post(self, user):
        """Login a user"""
        current_user = User.query.filter_by(email=user["email"].lower()).first()
        # Find the user with the provided email in the database

        if not current_user:
            # If user not found, return an error response
            abort(404, message="User not found")

        if not check_password_hash(current_user.password, user["password"]):
            # Verify the provided password with the stored hashed password
            abort(401, message="Invalid password")

        access_token = cache.get(current_user.id)
        if not access_token:
            # If no access token found in cache, create a new one and store it in cache
            access_token = create_access_token(identity=current_user.id)
            cache.set(current_user.id, access_token, timeout=None)

        refresh_token = create_refresh_token(identity=current_user.id)  # Generate a refresh token

        return {"access_token": access_token, "refresh_token": refresh_token}, 200






@blp.route("/logout", methods=["DELETE"])
@blp.doc(
    description="Logout a user", summary="Logout a user by revoking their access token"
)
@jwt_required()  # Requires a valid access token for access
def revoke_auth():
    jti = get_jwt()["jti"]  # Get the JWT ID from the current JWT
    current_user = get_jwt_identity()  # Get the current user's id from the JWT
    cached_data = cache.get(current_user)
    if cached_data:
        cache.delete(current_user)  # Delete the access token from the cache
    token = RevokedToken(jti=jti)
    token.save()  # Save the revoked token to the database

    return jsonify(msg="Successfully logged out")
