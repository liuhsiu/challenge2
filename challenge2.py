import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()
        print('in tear down method')

    def test_challenge2(self):
        self.driver.get("https://www.copart.com")
        searchfield = self.driver.find_element(By.ID, "input-search")
        searchfield.send_keys("exotic" + Keys.ENTER)
        table = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"serverSideDataTable\"]//tbody")))
        time.sleep(3)
        html = table.get_attribute("innerHTML")
        print(html)
        self.assertIn("PORSCHE", html)


if __name__ == '__main__':
    unittest.main()