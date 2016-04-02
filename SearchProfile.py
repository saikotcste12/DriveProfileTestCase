import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class SearchProfile(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://localhost:8069/"
        self.driver.maximize_window()

    def test_search_profile(self):
        driver = self.driver
        driver.get(self.base_url)
        profilesearchXpath    = "//*[@id='wrapwrap']/div/div[2]/form/div/span/button"
        profiletextfieldXpath = "//input[contains(@placeholder,'Search a Profile')]"
        searchwait = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath(profilesearchXpath))
        textwait   = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath(profiletextfieldXpath))
        profilesearchelement = searchwait
        profiletextelement   = textwait
        profiletextelement.clear()
        profiletextelement.send_keys("test")
        profilesearchelement.click()

    def test_search_result(self):
        driver = self.driver
        driver.get(self.base_url)
        profilesearchXpath    = "//*[@id='wrapwrap']/div/div[2]/form/div/span/button"
        profiletextfieldXpath = "//input[contains(@placeholder,'Search a Profile')]"
        searchwait = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath(profilesearchXpath))
        textwait   = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath(profiletextfieldXpath))
        profilesearchelement = searchwait
        profiletextelement   = textwait
        profiletextelement.clear()
        profiletextelement.send_keys("test")
        profilesearchelement.click()
        profileresultXpath = "//span[contains(.,'TesterEquafy Premium')]"
        profileresultwait = WebDriverWait(driver, 30).until(lambda  driver: driver.find_element_by_xpath(profileresultXpath))
        profileresultelement  = profileresultwait
        profileresultelement.click()

    #def tearDown(self):
       #self.driver.quit()

if __name__ == "__main__":
    unittest.main()
