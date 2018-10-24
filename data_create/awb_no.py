# _*_ coding: utf - 8 _*_
import random
from framework.logger import Logger

logger = Logger(logger='New_AwbNo').getlogger()

class New_AwbNo(object):
    def new_awbno1(self):
        awbno7 = random.randint(0,9999999)
        print(awbno7)
        awbno8 = awbno7 % 7
        print(awbno8)
        awbno = int(str(awbno7) + str(awbno8))
        print(awbno)
        return awbno
    def new_awbno(self):
        awbno_7 = random.sample(["0","1","2","3","4","5","6","7","8","9"],7)
        print(awbno_7)
        awbno7 = ''.join(awbno_7)
        print(awbno7)
        awbno8 = int(awbno7) % 7
        print(awbno8)
        awbno = awbno7 + str(awbno8)
        print(awbno)
        return awbno
if __name__ == '__main__':
    newawbno = New_AwbNo()
    newawbno.new_awbno()