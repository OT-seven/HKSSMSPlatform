#-*- coding:utf-8 -*-
'''
    功能：生成身份证号码
'''
__author__ = 'zhongan_TestTerm'
__version__ = '1.0'

import random,time
import time


class idcard():

    @staticmethod
    def makeNew():
        u'''
        随机生成新的18位身份证号码
        '''
        ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
        LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')

        t = time.localtime()[0]
        # print t
        x = '440524%04d%02d%02d%03d' % (random.randint(t - 40, t - 30),  # 年份项
                                        random.randint(1, 12),
                                        random.randint(1, 28),
                                        random.randint(1, 999))
        y = 0
        for i in range(17):
            y += int(x[i]) * ARR[i]
        global cardnum
        cardnum='%s%s' % (x, LAST[y % 11])
        print (cardnum)
        return cardnum


    def makeidcard(self):
        return cardnum

if __name__ == "__main__":
    idcard().makeNew()