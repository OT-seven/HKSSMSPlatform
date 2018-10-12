# _*_ coding: utf - 8 _*_
from framework.logger import Logger
from framework.base_page import Base_page
from framework.read_config import Read_config
from framework.browser_engine import Browser_Engine
from selenium import webdriver
from testsuits.test import Code

logger = Logger(logger='Test').getlogger()


d = webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(1)
d.get('http://10.1.2.194:4029/hkssms/login.jsp')
code = Code(d)
# code.textcode()
# code.textcode('//*[@id="validationCode_img"]')
code.imege()