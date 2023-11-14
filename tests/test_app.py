import sys
sys.path.append('..')

from app import app
from flask import session
from unittest import TestCase

app.config['WTF_CSRF_ENABLED'] = False

class WorkoutTestCase(TestCase):
    def test_home(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1 class="main-title">Our <span class="bold-you">AI-powered</span> workout generator will create a personalized plan for', html)
            self.assertIn('<div class="card-background">', html)
    
    def test_register_form_get(self):
        with app.test_client() as client:
            res = client.get('/register')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<p class="lead">Register below to save your workout routine!</p>', html)
            self.assertIn('<button class="button-submit" type="submit">Register</button>', html)
            
    def test_register_form_post(self):
        with app.test_client() as client:
            res = client.post('/register', data={'username': 'test_username', 'password': 'test_password'})
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<div class="background-img_login"></div>', html)
    
    def test_session_login(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['user_id'] = 100
                change_session['username'] = 'test_username'
            
            res = client.get('/')

            self.assertEqual(res.status_code, 200)
            self.assertEqual(session['user_id'], 100)
            self.assertEqual(session['username'], 'test_username')