# # # from ..extensions import db
# # # from .import Link

# # # class User(db.Model):
# # #     __tablename__ = 'users'
# # #     id = db.Column(db.Integer, primary_key=True)
# # #     username = db.Column(db.String(50), unique=True, nullable=False)
# # #     first_name = db.Column(db.String(100), nullable=True)
# # #     last_name = db.Column(db.String(100), nullable=True)
# # #     email = db.Column(db.String(200), unique=True, nullable=False)
# # #     password = db.Column(db.Text, nullable=False)
    
    
# # #     # links = db.relationship('Link', backref='user')
    
# # #     # links = db.relationship('Link', backref='user', lazy=True)
    
# # #     # user_links = db.relationship("Link", backref="user", lazy=True)
    
# # #     user_links = db.relationship("Link", backref="user_links", lazy=True)

  
    
    
# # #     def __init__(self, username, password, email, first_name, last_name):
# # #         self.username = username
# # #         self.password = password
# # #         self.email = email
# # #         self.first_name = first_name
# # #         self.last_name = last_name
# # #         self.user_links = []  # Initialize an empty list for user_links

# # #     # def save(self):
# # #     #     db.session.add(self)
# # #     #     db.session.commit()

# # #     def __repr__(self):
# # #         return f'<User {self.username}>'

# # #     def save(self):
# # #         db.session.add(self)
# # #         db.session.commit()

# # #     def delete(self):
# # #         db.session.delete(self)
# # #         db.session.commit()

# # #     # @staticmethod
# # #     # def get_all():
# # #     #     return User.query.all()

# # #     # @staticmethod
# # #     # def get_by_id(id):
# # #     #     return User.query.get(id)
    
    
    
# # #     @staticmethod
# # #     def create_user(username, password, email, first_name, last_name):
# # #         user = User(username, password, email, first_name, last_name)
# # #         db.session.add(user)
# # #         db.session.commit()
# # #         return user


# # from ..extensions import db
# # from .links import Link

# # class User(db.Model):
# #     __tablename__ = 'users'
# #     id = db.Column(db.Integer, primary_key=True)
# #     username = db.Column(db.String(50), unique=True, nullable=False)
# #     first_name = db.Column(db.String(100), nullable=True)
# #     last_name = db.Column(db.String(100), nullable=True)
# #     email = db.Column(db.String(200), unique=True, nullable=False)
# #     password = db.Column(db.Text, nullable=False)
    
# #     user_links = db.relationship("Link", backref="user_links", lazy=True)

# #     def __init__(self, username, password, email, first_name, last_name):
# #         self.username = username
# #         self.password = password
# #         self.email = email
# #         self.first_name = first_name
# #         self.last_name = last_name
# #         self.user_links = []  # Initialize an empty list for user_links

# #     def __repr__(self):
# #         return f'<User {self.username}>'

# #     def save(self):
# #         db.session.add(self)
# #         db.session.commit()

# #     def delete(self):
# #         db.session.delete(self)
# #         db.session.commit()

# #     @staticmethod
# #     def create_user(username, password, email, first_name, last_name):
# #         user = User(username, password, email, first_name, last_name)
# #         db.session.add(user)
# #         db.session.commit()
# #         return user

# #     def update_user_links(self, link_data):
# #         # Clear existing user_links
# #         self.user_links = []

# #         for link in link_data:
# #             # Create Link objects and associate them with the user
# #             link_obj = Link(original_url=link['original_url'], short_url=link['short_url'], user_links=self)
# #             self.user_links.append(link_obj)
# #             db.session.add(link_obj)

# #         db.session.commit()






# from ..extensions import db
# from .links import Link

# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True, nullable=False)
#     first_name = db.Column(db.String(100), nullable=True)
#     last_name = db.Column(db.String(100), nullable=True)
#     email = db.Column(db.String(200), unique=True, nullable=False)
#     password = db.Column(db.Text, nullable=False)
    
#     user_links = db.relationship("Link", backref="user_links", lazy=True)

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
#     def create_user(username, password, email, first_name, last_name):
#         user = User(username, password, email, first_name, last_name)
#         db.session.add(user)
#         db.session.commit()
#         return user

#     def update_user_links(self, link_data):
#         # Clear existing user_links
#         self.user_links = []

#         for link in link_data:
#             # Create Link objects and associate them with the user
#             link_obj = Link(original_url=link['original_url'], short_url=link['short_url'], user=self)
#             self.user_links.append(link_obj)
#             db.session.add(link_obj)

#         db.session.commit()























from ..extensions import db
from .links import Link
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    
    user_links = db.relationship("Link", backref="user_links", lazy=True)

    def __init__(self, username, password, email, first_name, last_name):
        self.username = username
        self.password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f'<User {self.username}>'

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def create_user(username, password, email, first_name, last_name):
        user = User(username, password, email, first_name, last_name)
        db.session.add(user)
        db.session.commit()
        return user

    def update_user_links(self, link_data):
        # Clear existing user_links
        self.user_links = []

        for link in link_data:
            # Create Link objects and associate them with the user
            link_obj = Link(original_url=link['original_url'], short_url=link['short_url'], user=self)
            self.user_links.append(link_obj)
            db.session.add(link_obj)

        db.session.commit()
