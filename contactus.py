import unittest
from selenium import webdriver


class ContactUs(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_contact_us(self):
        driver = self.driver
        driver.get("http://localhost:8069/")
        driver.maximize_window()

        elem = driver.find_element_by_link_text("Contact us")
        elem.click()

        firstname_elem = driver.find_element_by_id("first_name")
        firstname_elem.send_keys("Md Shakawath")

        lastname_elem = driver.find_element_by_id("last_name")
        lastname_elem.send_keys("Hossain")

        email_elem = driver.find_element_by_id("email")
        email_elem.send_keys("saikot.nstu@gmail.com")

        phone_elem = driver.find_element_by_id("phone")
        phone_elem.send_keys("+4917621553556")

        msg_elem = driver.find_element_by_id("msg")
        msg_elem.send_keys("This is message for contract page for testing purpose")

        firstname_elem.submit()
        driver.quit()

if __name__ == "__main__":
    unittest.main()
