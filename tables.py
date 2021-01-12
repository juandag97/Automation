import unittest
from selenium import webdriver
from time import sleep
class AssertionsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver') 
        driver = self.driver
        driver.implicitly_wait(30) 
        driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element_by_css_selector("#content > ul > li:nth-child(41) > a").click()

    def test_sort_tables(self):
        driver = self.driver
        table_data = [[] for i in range(5)]
        print(table_data)

        for i in range(5):
            header = driver.find_element_by_xpath(f'//*[@id="table1"]/thead/tr/th[{i + 1}]/span')
            table_data[i].append(header.text)

            for j in range(4):
                row_data = driver.find_element_by_xpath(f'//*[@id="table1"]/tbody/tr[{j + 1}]/td[{j+1}]')
                table_data[i].append(row_data.text)

        print(table_data)
    def tearDown(self):
        self.driver.quit() 

if __name__ == "__main__":
    unittest.main(verbosity=2)