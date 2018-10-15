# _*_ coding: utf - 8 _*_
from framework.logger import Logger
from framework.read_config import Read_config
from framework.base_page import Base_page
import time

logger = Logger(logger='Login').getlogger()

class Login(Base_page):
    accountname_w = 'xpath=>//*[@id="uname"]'  # 用户名输入框
    password_w = 'xpath=>//*[@id="passwd"]'    # 密码输入框
    vct_code_w = 'xpath=>//*[@id="validationCode"]'  # 图形验证码输入框
    login_btn_w = 'xpath=>//*[@id="login"]'  # 登录按钮
    def __init__(self, driver):
        self.driver = driver
    def login(self):
        date = Read_config()
        accountname = date.read_account('accountname')
        password = date.read_password('pwd')
        self.type(self.accountname_w, accountname)
        self.type(self.password_w, password)

        time.sleep(5)
        self.click(self.login_btn_w)
