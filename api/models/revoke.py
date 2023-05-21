# from ..extensions import db
# from datetime import datetime


# class RevokedToken(db.Model):
#     __tablename__ = 'revoked_tokens'
#     id = db.Column(db.Integer, primary_key=True)
#     jti = db.Column(db.Text, nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.now)

#     def save(self):
#         db.session.add(self)
#         db.session.commit()

#     @classmethod
#     def is_jti_blacklisted(cls, jti):
#         query = cls.query.filter_by(jti=jti).first()
#         return bool(query)