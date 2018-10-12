# _*_ coding: utf - 8 _*_
from framework.logger import Logger
from framework.read_config import Read_config
from framework.base_page import Base_page

logger = Logger(logger='Login').getlogger()

class Login(Base_page):
    accountname_w = 'xpath=>//*[@id="uname"]'
    password_w = 'xpath=>//*[@id="passwd"]'
