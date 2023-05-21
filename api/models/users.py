# from ..extensions import db


# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True, nullable=False)
#     first_name = db.Column(db.String(100), nullable=True)
#     last_name = db.Column(db.String(100), nullable=True)
#     email = db.Column(db.String(200), unique=True, nullable=False)
#     password = db.Column(db.Text, nullable=False)
    
    
#     # links = db.relationship('Link', backref='user')
    
#     # links = db.relationship('Link', backref='user', lazy=True)
    
#     user_links = db.relationship("Link", backref="user", lazy=True)

#     def __init__(self, username, password, email, first_name, last_name):
#         self.username = username
#         self.password = password
#         self.email = email
#         self.first_name = first_name
#         self.last_name = last_name

#     def __repr__(self):
#         return f'<User {self.username}>'

#     def save(self):
#         db.session.add(self)
#         db.session.commit()

#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()

#     @staticmethod
#     def get_all():
#         return User.query.all()

#     @staticmethod
#     def get_by_id(id):
#         return User.query.get(id)