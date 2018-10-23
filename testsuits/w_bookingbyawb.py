# _*_ coding: utf -8 _*_
import time
from framework.browser_engine import Browser_Engine
from framework.logger import Logger
from hkssms_page.w_booking_by_awb import W_Booking_By_Awb
import unittest
from hkssms_page.w_login import W_Login

logger = Logger(logger='').getlogger()

class W_BookingByAwb(unittest.TestCase):
    def setUp(self):
        browser = Browser_Engine(self)
        self.driver = browser.open_browser(self)
        logger.info('open brower')
    def test_bookawb(self):
        w_login = W_Login(self.driver)
        w_login.w_login()
        logger.info('login')
        time.sleep(2)
        bookawb = W_Booking_By_Awb(self.driver)
        bookawb.w_booking_by_awb()
        logger.info('booking by awb')
        time.sleep(2)
    def tearDown(self):
        self.driver.close()
        logger.info('close the browser')
if __name__ == '__main__':
    unittest.main()