import unittest
from app import app

# https://docs.python.org/3/library/unittest.html

class TestURLShortenerAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_root(self):
        # since there is no '/' route defined, testing if the error is in fact 404
        response = self.app.post('/')
        self.assertEqual(response.status_code, 404)

    def test_shorten_url(self):
        # testing if the shorten url route works properly 
        response = self.app.post('/shorten', json={"url": "https://example.com"})
        data = response.get_json()
        self.assertEqual(response.status_code, 201)
        self.assertTrue("shortcode" in data)

    def test_custom_shortcode(self):
        # if the website and shortcode is provided, testing whether or not it returns the shortcode (assuming that the shortcode is valid)
        response = self.app.post('/shorten', json={"url": "https://abc.com", "shortcode": "ab_123"})
        data = response.get_json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data["shortcode"], "ab_123")



if __name__ == '__main__':
    unittest.main()