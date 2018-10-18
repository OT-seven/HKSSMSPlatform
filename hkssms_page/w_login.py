# _*_ coding: utf - 8 _*_
from framework.logger import Logger
from framework.read_config import Read_config
from framework.base_page import Base_page
import time
from selenium.common.exceptions import NoAlertPresentException
logger = Logger(logger='Login').getlogger()

class Login(Base_page):
    accountname_w = 'xpath=>//*[@id="uname"]'  # 用户名输入框
    password_w = 'xpath=>//*[@id="passwd"]'    # 密码输入框
    vct_code_w = 'xpath=>//*[@id="validationCode"]'  # 图形验证码输入框
    login_btn_w = 'xpath=>//*[@id="login"]'  # 登录按钮
    def __init__(self, driver):
        self.driver = driver
    def login(self):
        accountname = Read_config.read_account('accountname')
        self.type(self.accountname_w, accountname)
        password = Read_config.read_password('pwd')
        self.type(self.password_w, password)
        time.sleep(10)
        self.click(self.login_btn_w)
        logger.info('click login btn')
        time.sleep(2)
        try:
            alert = self.driver.switch_to.alert
            if  alert:
                print(alert.text)
                logger.info(alert.text)
                time.sleep(2)
            else:
                logger.info('没有获取到错误信息')
            alert.accept()
            logger.info('点击确定')
        except NoAlertPresentException:
            return False
