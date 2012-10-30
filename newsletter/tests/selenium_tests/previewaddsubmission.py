from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Previewaddsubmission(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:8000/"
        self.verificationErrors = []
    
    def test_previewaddsubmission(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/")
        driver.find_element_by_link_text("Messages").click()
        self.assertEqual("Select message to change | Django site admin", driver.title)
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Test message"))
        driver.find_element_by_link_text("Test message").click()
        self.assertEqual("Change message | Django site admin", driver.title)
        driver.find_element_by_link_text("Preview").click()
        self.assertEqual("Preview message | Django site admin", driver.title)
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        driver.find_element_by_link_text("Create submission").click()
        self.assertEqual("Change submission | Django site admin", driver.title)
        # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
        self.assertEqual("Select submission to change | Django site admin", driver.title)
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
        driver.find_element_by_link_text("Test message").click()
        self.assertEqual("Change submission | Django site admin", driver.title)
        # ERROR: Caught exception [ERROR: Unsupported command [isTextPresent]]
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()