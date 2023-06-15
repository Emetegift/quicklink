from ..models import User, Link
from flask_smorest import abort, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask.views import MethodView
from ..schemas import UserSchema, UserDashboardSchema
from ..extensions import cache



blp = Blueprint("users", __name__, description="Operations on users")


# @blp.route("/users")
# class UsersResource(MethodView):
#     @blp.response(200, UserSchema(many=True))
#     @jwt_required()
#     def get(self):
#         """Get all users"""
#         users = User.query.all()
#         return users
    
    
@blp.route("/users")
class UsersResource(MethodView):
    @blp.response(200, UserSchema(many=True))
    # @jwt_required()
    # @cache.cached(timeout=3600)
    def get(self):
        """Get all users"""
        users = User.query.all()
        cache.set("users", users, timeout=3600)
        return users


@blp.route("/dashboard")
class DashboardResource(MethodView):
    @blp.response(200, UserDashboardSchema)
    @jwt_required()
    def get(self):
        """Get the current user's dashboard"""
        current_user = get_jwt_identity()
        user = User.query.filter_by(id=current_user).first_or_404()
        return user
    
    
    
    
    
    
    from ..models import User, Link
from flask_smorest import abort, Blueprint
from flask_jwt_extended import jwt_required
from flask.views import MethodView
from ..schemas import UserSchema