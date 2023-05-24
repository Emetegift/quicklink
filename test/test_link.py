import unittest
from api import create_app
from api.config.config import config_dict
from api. extensions import db
from api.models.users import Link
from werkzeug.security import generate_password_hash

class  UserTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config=config_dict['test'])
        
        self.appctx = self.app.app_context()
        
        self.appctx.push()
        
        self.client = self.app.test_client()
        
        db.create_all()
        
        #tearDown help to reset an app before creating another table
    def tearDown(self):
        
        db.drop_all()
        
        self.appctx.pop()
        
        self.app=None
        
        self.client=None