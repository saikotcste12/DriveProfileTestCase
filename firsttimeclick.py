import unittest
from selenium import webdriver

class FirstTimeClick(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_first_time_click(self):
        driver = self.driver
        driver.get("http://localhost:8069/")
        driver.maximize_window()
        elem = driver.find_element_by_link_text('First Time')
        elem.click()
        self.assertIn("First Time", driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
