# _*_ coding: utf - 8 _*_
import os
import configparser

class Read_config(object):
    config = configparser.ConfigParser()
    congif_paht = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
    config.read(congif_paht)
    def read_url(URL):
        url = Read_config.config.get('TestServer', URL)
        return url
    def read_account(account_name):
        account = Read_config.config.get('Account', account_name)
        return account
    def read_password(pwd):
        password = Read_config.config.get('Password', pwd)
        return password
    def read_browser(browsername):
        browser = Read_config.config.get('Browser', browsername)
        return browser