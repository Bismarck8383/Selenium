import unittest

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert


class base_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test1(self):
        driver = self.driver
        url = "https://testpages.herokuapp.com/styled/javascript-countdown-test.html"
        driver.get(url)

    def tearDown(self):
        driver = self.driver
        time.sleep(5)
        driver.close()


if __name__ == '__main__':
    unittest.main()
