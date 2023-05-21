import os
import re
from decouple import config
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

## Configuration for production
# uri = config('DATABASE_URL') # or any other relevant config variable.
# if uri.startswith('postgres://'):
#     uri = uri.replace('postgres://', 'postgresql://', 1)
# This configuration will be used by the application
class Config:
    # The secret key for the application
    SECRET_KEY = config("SECRET_KEY", "secretkey")
    # Expiration minutes for the jwt access token
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
    # Expiration days for the jwt refresh token
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    # The secret key for the jwt
    JWT_SECRET_KEY = config("JWT_SECRET_KEY", "secret")

    CACHE_TYPE = 'SimpleCache'
    CACHE_DEFAULT_TIMEOUT = 300

    # the api title
    API_TITLE = 'Url Shortener API'
    API_VERSION = 'v1'
    OPENAPI_VERSION = '3.0.2'
    OPENAPI_URL_PREFIX = '/'
    OPENAPI_JSON_PATH = 'openapi.json'
    OPENAPI_REDOC_PATH = '/redoc'
    OPENAPI_SWAGGER_UI_PATH = '/'
    OPENAPI_SWAGGER_UI_URL = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'
    OPENAPI_SWAGGER_UI_VERSION = '3.23.11'
    OPENAPI_SWAGGER_UI_JSONEDITOR = True
    PROPAGATE_EXCEPTIONS = True
    # the swagger ui configuration for authorization
    # API_SPEC_OPTIONS = {
    #     'security': [{"bearerAuth": []}],
    #     'components': {
    #         "securitySchemes":
    #             {
    #                 "bearerAuth": {
    #                     "type": "http",
    #                     "scheme": "bearer",
    #                     "bearerFormat": "JWT"
    #                 }
    #             }
    #     }
    # }

    
    
    
# class Config:
#     SECRET_KEY = config('SECRET_KEY', 'secret')
#     JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
#     JWT_REFRESH_TOKEN_EXPIRES = timedelta(minutes=30)
#     JWT_SECRET_KEY = config('JWT_SECRET_KEY')
    
    
class DevConfig(Config):
    DEBUG =True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO=True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(BASE_DIR, 'db.sqlite3')
    SQLALCHEMY_ECHO=True
    
class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO=True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db' # This will simply use a memory database instaed of creating a new one for the testing



class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = uri
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # DEBUG = config('DEBUG', False, cast=bool)
 # SQLALCHEMY_ECHO=True
     pass

#create a dictionary for easy use of the classes
config_dict={
    "dev":DevConfig,
    "prod":ProdConfig,
    "test":TestConfig
}