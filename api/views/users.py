from ..models import User
from flask_smorest import abort, Blueprint
from flask_jwt_extended import jwt_required
from flask.views import MethodView
from ..schemas import UserSchema

blp = Blueprint("users", __name__, description="Operations on users")


@blp.route("/users")
class UsersResource(MethodView):
    @blp.response(200, UserSchema(many=True))
    @jwt_required()
    def get(self):
        """Get all users"""
        users = User.query.all()
        return users
    
    
    
    
    