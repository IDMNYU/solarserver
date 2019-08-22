#example from https://selenium-python.readthedocs.io/getting-started.html

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class solarServerTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://192.168.1.79/dropdown/dropdown_dynamic.html")
        self.assertIn("Solar", driver.title)
        #elem = driver.find_element_by_id("yesterday")
        #cookieMonster = driver.get_cookies()

        menu = driver.find_element_by_css_selector(".dropbtn")
        hidden_submenu = driver.find_element_by_css_selector(".nav #submenu1")

        actions = ActionChains(driver)
        actions.move_to_element(menu)
        actions.click(hidden_submenu)
        actions.perform()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
