import unittest
from selenium import webdriver
from google_page import GooglePage

class GoogleTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver') 
        
    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search('Facebook')

        self.assertEqual('Facebook', google.keyword)

    @classmethod
    def tearDown(self):
        self.driver.quit() 

if __name__ == "__main__":
    unittest.main(verbosity=2)