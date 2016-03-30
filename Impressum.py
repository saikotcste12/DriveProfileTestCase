import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class Impressum(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_impressum_click(self):
        driver = self.driver
        driver.get("http://localhost:8069/")
        driver.maximize_window()
        elem = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_link_text("Impressum"))
        elem.click()
        self.assertIn("Impressum", driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()