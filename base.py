import unittest
from selenium import webdriver

class AssertionsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver') 
        driver = self.driver
        driver.implicitly_wait(30) 
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def tearDown(self):
        self.driver.quit() 

if __name__ == "__main__":
    unittest.main(verbosity=2)