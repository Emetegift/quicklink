import unittest
from flask import Flask
from flask_jwt_extended import JWTManager

from api import create_app, db
from api.models.links import  Link
from api.models.users import User


class ShortUrlTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

        db.create_all()

        self.jwt = JWTManager(self.app)
        self.jwt.init_app(self.app)

        with self.app.app_context():
            user = User(first_name='testfirst',last_name='testlast',username='testusernsame', email='test@example.com', password='password')
            db.session.add(user)
            db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_valid_url(self):
        original_url = 'https://www.example.com'
        response = self.client.post('/short-urls', json={'original_url': original_url})
        data = response.get_json()
        
        print(response.status_code)
        print(data)

    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn('short_url', data)

    def test_invalid_url(self):
        original_url = 'invalid_url'
        response = self.client.post('/short-urls', json={'original_url': original_url})
        data = response.get_json()
        
        print(response.status_code)
        print(data)

    #     self.assertEqual(response.status_code, 400)
    #     self.assertEqual(data['message'], 'Invalid URL')

    def test_insecure_url(self):
        original_url = 'http://www.example.com'
        response = self.client.post('/short-urls', json={'original_url': original_url})
        data = response.get_json()

        
        print(response.status_code)
        print(data)

        # self.assertEqual(response.status_code, 400)
        # self.assertEqual(data['message'], 'Insecure URL')


if __name__ == '__main__':
    unittest.main()


# # python -m unittest discover -s test -p test_link.py