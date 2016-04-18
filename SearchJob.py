import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class SearchJob(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://localhost:8069/"
        self.driver.maximize_window()

    def base_case(self):
        driver = self.driver
        driver.get(self.base_url)
        jobsearchXpath = "//*[@id='wrapwrap']/div/div[3]/form/div/span/button"
        jobtextfieldXpath = "//input[contains(@placeholder,'Search a Job')]"
        searchwait = WebDriverWait(self.driver, 30).until(lambda driver: driver.find_element_by_xpath(jobsearchXpath))
        textwait = WebDriverWait(self.driver, 30).until(lambda driver: driver.find_element_by_xpath(jobtextfieldXpath))
        jobsearchelement = searchwait
        jobtextelement = textwait
        jobtextelement.clear()
        jobtextelement.send_keys("Test")
        jobsearchelement.click()

    def test_search_job_what(self):
        self.base_case()

    def test_search_job_where(self):
        self.base_case()
        jobwheresearchXpath = ".//*[@id='wrap']/div/div[1]/form/div[2]/span/button"
        jobtextfieldXpath = "//input[contains(@placeholder,'Where')]"
        jobwheresearchwait = WebDriverWait(self.driver, 30).until(lambda driver: driver.find_element_by_xpath(jobwheresearchXpath))
        jobwheretextwait = WebDriverWait(self.driver, 30).until(lambda driver: driver.find_element_by_xpath(jobtextfieldXpath))
        jobwheresearchelement = jobwheresearchwait
        jobwheretextelement = jobwheretextwait
        jobwheretextelement.clear()
        jobwheretextelement.send_keys("Berlin")
        jobwheresearchelement.click()

    def base_case_two(self):
        jobwheresearchXpath = ".//*[@id='wrap']/div/div[1]/form/div[2]/span/button"
        jobtextfieldXpath = "//input[contains(@placeholder,'Where')]"
        jobwheresearchwait = WebDriverWait(self.driver, 30).until(lambda driver: driver.find_element_by_xpath(jobwheresearchXpath))
        jobwheretextwait = WebDriverWait(self.driver, 30).until(lambda driver: driver.find_element_by_xpath(jobtextfieldXpath))
        jobwheresearchelement = jobwheresearchwait
        jobwheretextelement = jobwheretextwait
        jobwheretextelement.clear()
        jobwheretextelement.send_keys("Berlin")
        jobwheresearchelement.click()

    def test_search_job_result(self):
        self.base_case()
        self.base_case_two()
        jobresultXpath = "//td[contains(.,'Software Development Engineers in Test (SDET), remotely')]"
        jobresultwait = WebDriverWait(self.driver, 30).until(lambda driver: driver.find_element_by_xpath(jobresultXpath))
        jobresultelement = jobresultwait
        jobresultelement.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
