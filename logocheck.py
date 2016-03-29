import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class LogoCheck(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_logo_check_img(self):
        driver = self.driver
        driver.get("http://localhost:8069/")
        driver.maximize_window()
        elem = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//*[@id='wrapwrap']/div/nav/a/img"))
        elem.click()
        self.assertIn("Homepage", driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()