import unittest
from selenium import webdriver

class AssertionsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver') 
        driver = self.driver
        driver.implicitly_wait(30) 
        driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element_by_css_selector("#content > ul > li:nth-child(43) > a").click()

    def test_find_typo(self):
        driver = self.driver

        paragraph_to_check = driver.find_element_by_css_selector("#content > div > p:nth-child(3)")
        text_to_check = paragraph_to_check.text
        print(text_to_check)
        tries = 1
        found = False 
        right_text = "Sometimes you'll see a typo, other times you won't."

        while text_to_check != right_text:
            paragraph_to_check = driver.find_element_by_css_selector("#content > div > p:nth-child(3)")
            text_to_check = paragraph_to_check.text
            driver.refresh()
            tries += 1
        while not found:
            if text_to_check == right_text:
                tries += 1
                driver.refresh()
                found = True 
        self.assertEqual(found, True)
        print(f"It took {tries} tries to find the typo")

    
    def tearDown(self):
        self.driver.quit() 

if __name__ == "__main__":
    unittest.main(verbosity=2)