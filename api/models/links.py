# # from flask_sqlalchemy import SQLAlchemy
# from ..extensions import db
# import string
# from random import choices
# from datetime import datetime
# import qrcode
# from io import BytesIO
# from PIL import Image


# # db = SQLAlchemy()

# class Link(db.Model):
#     __tablename__='links'
#     id = db.Column(db.Integer, primary_key=True)
#     original_url = db.Column(db.String(200), nullable=False)
#     short_url = db.Column(db.String(6), unique=True)
#     views = db.Column(db.Integer, default=0)
#     qr_code = db.Column(db.LargeBinary())
#     date_created = db.Column(db.DateTime, default=datetime.now)
    
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#     # user = db.relationship('User', backref='links', primaryjoin='Link.user_id == User.id')
   
#     # user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    
#     # user = db.relationship("User", back_populates="links", lazy=True)
    

#     # user = db.relationship("User", backref='links', lazy=True)
    
    
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         # Create short url
#         self.short_url = self.generate_short_link()
#         self.qr_code = self.generate_qr_code()
        
#     def __repr__(self):
#         return f'<Link {self.original_url}>'

#     def save(self):
#         # self.short_url=self.create_short_url()
#         db.session.add(self)
#         db.session.commit()

#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()
        
#     def generate_short_link(self):
#         characters = string.digits + string.ascii_letters
#         short_url = ''.join(choices(characters, k=6 ))
            
#         # Check if link exist
#         link = self.query.filter_by(short_url=short_url).first()
            
#         if link:
#             return self.generate_short_link()
#         return short_url


#     def generate_qr_code(self):
#         qr = qrcode.QRCode(version=1, box_size=10, border=5)
#         qr.add_data(self.short_url)
#         qr.make(fit=True)
#         img = qr.make_image(fill='black', back_color='white')
#         buffer = BytesIO()
#         img.save(buffer, format='JPEG')
#         buffer.seek(0)
#         qr_code = buffer.getvalue()
#         return qr_code