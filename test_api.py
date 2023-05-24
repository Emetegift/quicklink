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
            
            
            
    def tearDown(self):
        with self.app.app_context():
                db.session.remove()
                db.drop_all()


# Test runner
if __name__ =="__main__":
    unittest.main()

        