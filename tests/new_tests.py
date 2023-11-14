import sys
sys.path.append('..')

from app import app
from unittest import TestCase

class WorkoutTestCase(TestCase):
    # def setUp(self):
    #     # Set up a test user for authentication
    #     with app.test_client() as client:
    #         client.post('/register', data={'username': 'testuser', 'password': 'testpassword'})

    # def tearDown(self):
    #     # Clean up test data after each test
    #     with app.test_client() as client:
    #         client.get('/logout')

    def test_home(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1 class="main-title">Our <span class="bold-you">AI-powered</span> workout generator will create a personalized plan for', html)

    def test_register_user(self):
        with app.test_client() as client:
            # Test successful user registration
            res = client.post('/register', data={'username': 'newuser', 'password': 'newpassword'})
            self.assertEqual(res.status_code, 200)  # Expecting a redirect after successful registration
            self.assertIn('/form', res.headers['Location'])  # Check for redirection to '/form'
            # ... (existing code)

            # Test registration with existing username
            res = client.post('/register', data={'username': 'testuser', 'password': 'testpassword'})
            html = res.get_data(as_text=True)
            self.assertIn('Username already exists.', html)

    # def test_login_user(self):
    #     with app.test_client() as client:
    #         # Test successful user login
    #         res = client.post('/login', data={'username': 'testuser', 'password': 'testpassword'})
    #         self.assertEqual(res.status_code, 302)  # Expecting a redirect after successful login

    #         # Test login with incorrect credentials
    #         res = client.post('/login', data={'username': 'testuser', 'password': 'wrongpassword'})
    #         html = res.get_data(as_text=True)
    #         self.assertIn('Invalid username/password', html)

    # def test_logout_user(self):
    #     with app.test_client() as client:
    #         # Test user logout
    #         res = client.get('/logout')
    #         self.assertEqual(res.status_code, 302)  # Expecting a redirect after logout

    # def test_survey(self):
    #     with app.test_client() as client:
    #         # Assuming a logged-in user
    #         client.post('/login', data={'username': 'testuser', 'password': 'testpassword'})
            
    #         # Test successful form submission
    #         res = client.post('/form', data={'goal': 'Build Muscle', 'days_per_week': 3, 'time_avaliable': 45, 'equipment': 'Dumbbells'})
    #         self.assertEqual(res.status_code, 200)  # Expecting a successful response

    #         # Test form submission without authentication
    #         client.get('/logout')  # Log out the user
    #         res = client.post('/form', data={'goal': 'Build Muscle', 'days_per_week': 3, 'time_avaliable': 45, 'equipment': 'Dumbbells'})
    #         self.assertEqual(res.status_code, 302)  # Expecting a redirect to the login page

    # def test_display_user(self):
    #     with app.test_client() as client:
    #         # Assuming a logged-in user
    #         client.post('/login', data={'username': 'testuser', 'password': 'testpassword'})
            
    #         # Test access to user page
    #         res = client.get('/users/1')  # Assuming user ID 1 exists
    #         self.assertEqual(res.status_code, 200)  # Expecting a successful response

    #         # Test access to another user's page
    #         res = client.get('/users/2')  # Assuming user ID 2 exists
    #         html = res.get_data(as_text=True)
    #         self.assertIn('You do not have access to this user page', html)

    # def test_display_workout(self):
    #     with app.test_client() as client:
    #         # Assuming a logged-in user
    #         client.post('/login', data={'username': 'testuser', 'password': 'testpassword'})
            
    #         # Assuming a workout exists for the logged-in user
    #         res = client.get('/workouts/1')  # Assuming workout ID 1 exists
    #         self.assertEqual(res.status_code, 200)  # Expecting a successful response

    # def test_delete_workout(self):
    #     with app.test_client() as client:
    #         # Assuming a logged-in user
    #         client.post('/login', data={'username': 'testuser', 'password': 'testpassword'})
            
    #         # Assuming a workout exists for the logged-in user
    #         res = client.get('/workouts/1/delete')  # Assuming workout ID 1 exists
    #         self.assertEqual(res.status_code, 302)  # Expecting a redirect after workout deletion
