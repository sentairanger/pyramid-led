import unittest

from pyramid import testing

class TutorialFunctionalTests(unittest.TestCase):
    def setUp(self):
        from tutorial import main
        app = main({})
        from webtest import TestApp

        self.testapp = TestApp(app)

    def test_home(self):
        res = self.testapp.get('/', status=200)
        self.assertIn(b'', res.body)
    
    def test_ledon(self):
        res = self.testapp.get('/ledon', status=200)
        self.assertIn(b'', res.body)
        
    def test_ledoff(self):
        res = self.testapp.get('/ledoff', status=200)
        self.assertIn(b'', res.body)
