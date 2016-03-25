import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class FirstTimeClick(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def test_first_time_click(self):
        driver = self.driver
        driver.get("http://localhost:8069/")
        driver.maximize_window()
        elem = driver.find_element_by_xpath("//*[@id='top_menu']/li[1]/a/span")
        elem.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
