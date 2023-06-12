import unittest
from api import create_app
from api.config.config import config_dict
from api. extensions import db
from api.models.users import User
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
        
        
    def test_user_register(self):
        
        data = {
            "username":"moon",
            "first_name": "john",
            "last_name": "Doe",
            "email":"ani@gmail.com",
            "password":"password",
            "confirm_password": "password"
        }
        
        
        register_response = self.client.post('/signup', json=data)
        
        user = User.query.filter_by(email='ani@gmail.com').first()
         
        assert user.username == "moon"
        
        assert register_response.status_code == 201
        
    def test_user_login(self):
        
        data = {
            "username":"moon",
            "first_name": "john",
            "last_name": "Doe",
            "email":"ani@gmail.com",
            "password":"password",
            "confirm_password": "password"
        }
        
        register_response = self.client.post('/signup', json=data)
        
        data = {
            "email":"ani@gmail.com",
            "password":"password"
        }
        login_response = self.client.post('/login', json=data)
        
        status_code = login_response.status_code
        
        # json=login_response.json
        # print(json)
        
        
        self.assertEqual(status_code, 200)
        
        
        
        
        
        
# Test runner
if __name__ =="__main__":
    unittest.main()
        
      
 # command line to run test_user.py       
# python -m unittest discover -s test -p test_user.py
