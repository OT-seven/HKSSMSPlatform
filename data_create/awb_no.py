# _*_ coding: utf - 8 _*_
import random

class New_AwbNo(object):
    def new_awbno(self):
        awbno7 = '%07d' % (random.randint(0,9999999))
        awbno8 = int(awbno7) % 7
        awbno = int(str(awbno7) + str(awbno8))
        print(awbno)
        return awbno
if __name__ == '__main__':
    newawbno = New_AwbNo()
    newawbno.new_awbno()