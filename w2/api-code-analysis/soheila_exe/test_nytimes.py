"""unit test for nytimes"""
import unittest
import nytimes

class TestNytimes(unittest.TestCase):
    """unit test class"""
    def test_success(self):
       """test happy path"""
       url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q=Apollo 11&api-key=ecmEGhTeFYvTGEAWcYZ6KJGmW6jrOjy0"
       self.assertEqual(nytimes.get_information(url),"success")
    def test_unauthorized(self):
       """invalid key"""
       url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q=Apollo 11&api-key=test"
       self.assertEqual(nytimes.get_information(url),"unauthorized, invalid api keys")
    def test_notfound(self):
        """invalid url"""
        url = "https://api.nytimes.com/svc/search/v2/articlesearch.jsonq=Apollo 11&api-key=ecmEGhTeFYvTGEAWcYZ6KJGmW6jrOjy0"
        self.assertEqual(nytimes.get_information(url),"invalid url")
if __name__== "__main__":
    unittest.main()