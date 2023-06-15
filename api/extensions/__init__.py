from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_smorest import Api
# from flask_cors import CORS
from flask_caching import Cache

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
api = Api()
# cors = CORS()
cache = Cache()