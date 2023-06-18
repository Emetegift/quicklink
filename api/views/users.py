from flask import jsonify
from ..models import User, Link, Click
from flask_smorest import abort, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask.views import MethodView
from ..schemas import UserSchema, UserDashboardSchema
from ..extensions import cache
from ..extensions import db


blp = Blueprint("users", __name__, description="Operations on users")


@blp.route("/users")
class UsersResource(MethodView):
    @blp.response(200, UserSchema(many=True))
    def get(self):
        """Get all users"""
        users = User.query.all()
        cache.set("users", users, timeout=3600)  # Cache the users data for 3600 seconds (1 hour)
        return users


@blp.route("/dashboard")
class DashboardResource(MethodView):
    @blp.response(200, UserDashboardSchema)
    @jwt_required()
    def get(self):
        """Get the current user's dashboard"""
        current_user = get_jwt_identity()  # Get the current user's id from the JWT
        user = User.query.filter_by(id=current_user).first_or_404()

        shortened_urls = Link.query.filter_by(user_id=user.id).all()  # Get all shortened URLs for the user
        analytics = {
            'totalClicks': +1,  # Increment the total clicks count by 1
            'clicksBySource': {}
        }

        for url in shortened_urls:
            clicks = Click.query.filter_by(link_id=url.id).all()  # Get all clicks for the URL
            analytics['totalClicks'] += len(clicks)  # Update the total clicks count

            for click in clicks:
                source = click.source
                if source in analytics['clicksBySource']:
                    analytics['clicksBySource'][source] += 1  # Increment the clicks count by source
                else:
                    analytics['clicksBySource'][source] = 1

        user.all_shortened_urls = shortened_urls  # Update the user's shortened URLs
        db.session.commit()  # Save the changes to the database

        serialized_user = UserDashboardSchema().dump(user)  # Serialize the user object
        return jsonify(serialized_user)  # Return the serialized user object as JSON
