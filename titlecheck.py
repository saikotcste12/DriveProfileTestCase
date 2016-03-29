import unittest
from selenium import webdriver


class TitleCheck(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_drive_profile_title(self):
        driver = self.driver
        driver.get("http://localhost:8069/")
        driver.maximize_window()
        elem = driver.find_element_by_link_text("Home")
        elem.clik()
        self.assertIn("Homepage", driver.title)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
