# -*- coding:utf-8 -*-
'''
    作者：zhongan_TestTerm
    创建日期：2017.08.15
    功能：生成QQ号及邮件
'''
__author__ = 'zhongan_TestTerm'
__version__ = '1.0'

import random, time
import string

class qqmail():
    @staticmethod
    def qqnum():
        '''
        生成8位QQ号码
        '''
        qqnum = '%04d%02d%02d' % (random.randint(6000, 8000),
                                  random.randint(10, 99),
                                  random.randint(10, 99))
        print (qqnum)
        return qqnum

    @staticmethod
    def makemail():
        '''
        生成邮件地址信息
        '''
        mailstring = ''.join(random.sample(string.ascii_letters + string.digits, 8))

        mailnum = mailstring + '@126.com'
        print (mailnum)
        return mailnum

if __name__ == "__main__":
    qqmail().qqnum()
    qqmail().makemail()
