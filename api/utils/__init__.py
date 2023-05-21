from ..models import User
from flask_smorest import abort
from ..extensions import cache


def check_if_username_is_unique(username):
    """Check if email and username are unique"""
    user = User.query.filter_by(username=username).first()
    if user:
        abort(409, message='Username already exists')


def check_if_email_is_unique(email):
    """Check if email is unique"""
    user = User.query.filter_by(email=email).first()
    if user:
        abort(409, message='Email already exists')


def check_if_user_is_still_logged_in(current_user):
    if current_user is None:
        abort(401, message='You are logged out')


def email_not_found(email):
    """Check if the email exists"""
    user = User.query.filter_by(email=email).first()
    if not user:
        abort(404, message='User not found')