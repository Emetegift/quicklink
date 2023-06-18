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
    # @jwt_required()
    # @cache.cached(timeout=3600)
    def get(self):
        """Get all users"""
        users = User.query.all()
        cache.set("users", users, timeout=3600)
        return users


# @blp.route("/dashboard")
# class DashboardResource(MethodView):
#     @blp.response(200, UserDashboardSchema)
#     @jwt_required()
#     def get(self):
#         """Get the current user's dashboard"""
#         current_user = get_jwt_identity()
#         user = User.query.filter_by(id=current_user).first_or_404()
#         return user
    
  
  
  


# @blp.route("/dashboard")
# class DashboardResource(MethodView):
#     @blp.response(200, UserDashboardSchema)
#     @jwt_required()
#     def get(self):
#         """Get the current user's dashboard"""
#         current_user = get_jwt_identity()
#         user = User.query.filter_by(id=current_user).first_or_404()

#         # Get the analytics data for the user's shortened URLs
#         shortened_urls = Link.query.filter_by(user_id=user.id).all()
#         analytics = {
#             'totalClicks': 0,
#             'clicksBySource': {}
#         }

#         for url in shortened_urls:
#             clicks = Click.query.filter_by(link_id=url.id).all()
#             analytics['totalClicks'] += len(clicks)

#             for click in clicks:
#                 source = click.source
#                 if source in analytics['clicksBySource']:
#                     analytics['clicksBySource'][source] += 1
#                 else:
#                     analytics['clicksBySource'][source] = 1

#         user.analytics = analytics
#         db.session.commit()

#         serialized_user = UserDashboardSchema().dump(user)
#         return jsonify(serialized_user)





@blp.route("/dashboard")
class DashboardResource(MethodView):
    @blp.response(200, UserDashboardSchema)
    @jwt_required()
    def get(self):
        """Get the current user's dashboard"""
        current_user = get_jwt_identity()
        user = User.query.filter_by(id=current_user).first_or_404()

        # Get the analytics data for the user's shortened URLs
        shortened_urls = Link.query.filter_by(user_id=user.id).all()
        # analytics = {
        #     'totalClicks': +1,
        #     'clicksBySource': {}
        # }

        # for url in shortened_urls:
        #     clicks = Click.query.filter_by(link_id=url.id).all()
        #     analytics['totalClicks'] += len(clicks)

        #     for click in clicks:
        #         source = click.source
        #         if source in analytics['clicksBySource']:
        #             analytics['clicksBySource'][source] += 1
        #         else:
        #             analytics['clicksBySource'][source] = 1

        user.all_shortened_urls = shortened_urls
        db.session.commit()

        serialized_user = UserDashboardSchema().dump(user)
        return jsonify(serialized_user)
