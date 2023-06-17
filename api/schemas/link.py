from marshmallow import Schema, fields
# from ..schemas import UserSchema


class LinkSchema(Schema):
    id = fields.Integer(dump_only=True)
    # user = fields.Nested(UserSchema, only=("id", "first_name", "last_name","password", "confirm_password", "username", "email"))
    user_id = fields.Integer(required=True)
    original_url = fields.String(required=True)
    custom_url = fields.String(required=True)
    short_url = fields.String(dump_only=True)
    date_created = fields.DateTime(dump_only=True)


class GetLinksSchema(Schema):
    id = fields.Integer()
    user_id = fields.Integer()
    original_url = fields.String()
    short_url = fields.String()
    custom_url = fields.String()
    visit = fields.Integer()
    date_created = fields.String()
    views = fields.String()
    

class ClickSchema(Schema):
    id = fields.Integer(dump_only=True)
    link_id = fields.Integer(required=True)
    source = fields.String(required=True)
    timestamp = fields.DateTime(dump_only=True)
