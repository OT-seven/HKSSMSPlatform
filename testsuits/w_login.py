# _*_ coding: utf - 8 _*_
from hkssms_page.login import Login
import unittest
from framework.browser_engine import Browser_Engine
from framework.logger import Logger
import time

logger = Logger(logger='w_login').getlogger()

class w_login(unittest.TestCase):
    def setUp(self):
        browser = Browser_Engine(self)
        self.driver = browser.open_browser(self)
        logger.info('open browser')
    def test_w_login(self):
        w_login = Login(self.driver)
        w_login.login()
        logger.info('login')
        time.sleep(10)
    def tearDown(self):
        self.driver.close()
        logger.info('close browser')
if __name__ == '__main__':
    unittest.main()