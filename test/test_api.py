import unittest
from api import create_app
from api.config.config import TestConfig
from api. extensions import db

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        
        self.clent =self.app.test_client(self)
        
        with self.app.app_context():
            db.init_app(self.app)
            
            db.create_all()
            
    def test_register(self):
        register_response = self.client.post('/register',
            json={"username":"testusername", "first_name":"testfirstname", "last_name":"testlastname",
                  "email":"testemail", "password":"testpassword", "confirmpassword":"testpassword"}                                     
        )        
            
        status_code =register_response.status_code
        
        self.assertEqual(status_code, 201)
            
    def tearDown(self):
        with self.app.app_context():
                db.session.remove()
                db.drop_all()


# Test runner
if __name__ =="__main__":
    unittest.main()

        