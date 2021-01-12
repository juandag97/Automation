import unittest
from selenium import webdriver
from time import sleep
class TestingMercadoLibre(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver') 
        driver = self.driver
        driver.get('https:www.mercadolibre.com')
        driver.implicitly_wait(30) 
        driver.maximize_window()
    
    def test_search_mazda3(self):
        driver = self.driver 

        country = driver.find_element_by_id('CO')
        country.click()

        search_field = driver.find_element_by_name('as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys('mazda 3')
        search_field.submit()
        sleep(3)

        location = driver.find_element_by_partial_link_text('Bogotá D.C')
        location.click()
        sleep(3)

        condition = driver.find_element_by_css_selector('#root-app > div > div > aside > section.ui-search-filter-groups > dl:nth-child(7) > dd:nth-child(2) > a > span.ui-search-filter-name')
        #condition.click()
        driver.execute_script("arguments[0].click();", condition)
        sleep(3)

        order_menu = driver.find_element_by_css_selector('#root-app > div > div > aside > section.ui-search-view-options > div.ui-search-view-options__group > div.ui-search-sort-filter > div > div > button')
        order_menu.click()
        lower_price = driver.find_element_by_css_selector('#root-app > div > div > aside > section.ui-search-view-options > div.ui-search-view-options__group > div.ui-search-sort-filter > div > div > div > ul > li:nth-child(2)')
        lower_price.click()
        sleep(3)

        articles, prices = [], []
        for i in range(3):
            #article_name = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol[1]/li[{i + 1}]/div/div/a/div/div[3]/h2').text
            article_name = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol[1]/li[{i + 1}]/div/div/a/div/div[3]/h2').text
            articles.append(article_name)
            article_price = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol[1]/li[{i + 1}]/div/div/a/div/div[1]/div/div/span/span[2]').text 
            prices.append(article_price)

        print(articles, prices)
    def tearDown(self):
        self.driver.quit() 

if __name__ == "__main__":
    unittest.main(verbosity=2)