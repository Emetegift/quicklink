import re
from ..models import Link
from flask_smorest import abort, Blueprint
from flask import redirect, make_response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask.views import MethodView
from ..schemas import LinkSchema, GetLinksSchema
from ..utils.validate_url import validate_url

from ..utils import check_if_user_is_still_logged_in
from ..extensions import db, cache


blp = Blueprint("urls", __name__, description="Operations on URLS")

@blp.route("/short-urls")
class CreateShortUrl(MethodView):
    @blp.arguments(LinkSchema)
    @jwt_required()
    def post(self, new_url):
        """Create a new short URL"""
        current_user = get_jwt_identity()
        url_pattern = r'https'  # Required URL pattern

        if not re.match(url_pattern, new_url["original_url"]):
            abort(400, message="Invalid URL format")
        
        if not new_url["original_url"].startswith('http://') and not new_url["original_url"].startswith('https://'):
            new_url["original_url"] = 'http://' + new_url["original_url"]
        
        link = Link(**new_url)
        link.save()
        response = {
            "original_url": link.original_url,
            "shortened_url": f"{request.host_url}{link.short_url}",
        }
        return response, 201

@blp.route("/<short_url>")
# @blp.route('/short-urls/<int:short-urls_id>')
class RedirectShortUrl(MethodView):
    @blp.response(302)
    @cache.memoize(timeout=3600)
    def get(self, short_url):
        """Redirect to the original url"""
        link = Link.query.filter_by(short_url=short_url).first()
        if not link:
            abort(404, message="Url not found")
        link.views += 1
        db.session.commit()
        return redirect(link.original_url)


@blp.route("/<short_url>/qr-code")
@jwt_required()
@cache.cached(timeout=3600)
def qr_code(short_url):
    """Get the QR code for a short url"""
    link = Link.query.filter_by(short_url=short_url).first_or_404()
    if not link.qr_code:
        # If the QR code hasn't been generated yet, generate it now
        link.qr_code = link.generate_qr_code()
        link.save()
    response = make_response(link.qr_code)
    response.headers.set("Content-Type", "image/jpeg")
    return response

@blp.route("/all-links")
@blp.response(200, GetLinksSchema(many=True))
@jwt_required()
@cache.cached(timeout=3600)
def GetLinks():
    # Check if token is valid
    current_user = get_jwt_identity()
    # check_if_user_is_still_logged_in(current_user)
    links = Link.query.filter_by(user_id=current_user).all()
    return links