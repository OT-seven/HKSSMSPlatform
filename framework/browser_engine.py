# _*_ coding: utf - 8 _*_
import os
from selenium import webdriver
from framework.logger import Logger
from framework.read_config import Read_config

logger = Logger(logger='Browser_Engine').getlogger()

class Browser_Engine(object):
    dir = os.path.dirname(os.path.abspath('.'))
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    firefox_driver_path = dir + '/tools/gockodriver.exe'
    ie_driver_paht = dir + '/tools/IEDriverServer.exe'
    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, driver):
        browser = Read_config.read_browser('browsername')
        url = Read_config.read_url('URL')
        if browser == "chrome":
            driver = webdriver.Chrome()
            logger.info("you had select %s" % browser)
        elif browser == "firefox":
            driver = webdriver.Firefox()
            logger.info("you had select %s" % browser)
        elif browser == "ie":
            driver = webdriver.Ie()
            logger.info("you had select %s" % browser)
        else:
            logger.info("select browser error")
        driver.get(url)
        logger.info("browser open %s" % url)
        driver.maximize_window()
        driver.implicitly_wait(1)
        return driver
    def handle(self):
        handles = self.driver.window_handles
        for handle in handles:
            if handle != self.driver.current_window_handle:
                self.driver.close()
                self.driver.swith_to.window(handle)
                logger.info('switch to second window', handle)
    def iframe(self, iframeid):
        self.driver.swith_to.frame(iframeid)