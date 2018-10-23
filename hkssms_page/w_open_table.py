# _*_ coding: utf - 8 _*_
from framework.logger import Logger
from framework.base_page import Base_page
import time
from framework.browser_engine import Browser_Engine

logger = Logger(logger='Open_Table').getlogger()

class W_Open_table(Base_page):
    booking_mgt_w = 'xpath=>//*[@id="left-menu"]/a[4]'  # 订舱管理页签组
    booking_by_awb_w = 'xpath=>//*[@id="fbce5b976509432e8f3fc6ce5936a2ef"]/li[1]/a'  # 有运单订舱页签
    def __init__(self, driver):
        self.driver = driver
    def w_open_table(self):
        self.click(self.booking_mgt_w)
        time.sleep(1)
        self.click(self.booking_by_awb_w)
        time.sleep(1)
        # iframe = self.driver.find_elements_by_tag_name("iframe")[1]
        # self.driver.switch_to.frame(iframe)
        self.driver.switch_to.frame(1)
        # self.driver.switch_to.frame(self.driver.find_element_by_xpath('//*[@id="cleverTabPanelItem-1540275308385"]/iframe')[0])
        # self.driver.switch_to.frame('BookingManagement/addBooking.jsp')
        time.sleep(1)