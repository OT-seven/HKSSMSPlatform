# _*_ coding: utf - 8 _*_
from framework.logger import Logger
from framework.read_config import Read_config
from framework.base_page import Base_page
import time
from selenium.common.exceptions import NoAlertPresentException
from data_create.awb_no import New_AwbNo

logger = Logger(logger='Login').getlogger()

class W_Booking_By_Awb(Base_page):
    # 定位各个元素
    booking_mgt_w = 'xpath=>//*[@id="left-menu"]/a[4]'  # 订舱管理页签组
    booking_by_awb_w = 'xpath=>//*[@id="fbce5b976509432e8f3fc6ce5936a2ef"]/li[1]/a'  # 有运单订舱页签
    awbno_w = 'xpath=>//*[@id="ydh"]'  # 运单号 //*[@id="ydh"]
    dep_w = 'xpath=>//*[@id="qyz"]'  # 起运站
    piece_w = 'xpath=>//*[@id="js"]'  # 件数
    grossweight_w = 'xpath=>//*[@id="zl"]'  # 重量
    chargeableweight_w = 'xpath=>//*[@id="jfzl"]'  # 计费重量
    rate_w = 'xpath=>//*[@id="yj"]'  # 运价
    size_w = 'xpath=>//*[@id="cc"]'  # 尺寸
    volume_w = 'xpath=>//*[@id="tj"]'  # 体积
    origin_w = 'xpath=>//*[@id="hyd"]'  # 货源地
    sono_w = 'xpath=>//*[@id="rcid"]'  # 入仓号
    goods_code_w = 'xpath=>//*[@id="hwpm"]'  # 中文品名
    packingtype_w = 'xpath=>//*[@id="bzlx"]'  # 包装类型
    precision_packaging_w = 'xpath=>//*[@id="bzlx"]/option[3]'  # 精包装
    declaration_type_w = 'xpath=>//*[@id="kjbg"]'  # 报关方式
    general_trade_w = 'xpath=>//*[@id="kjbg"]/option[2]'  # 一般贸易
    memo_w = 'xpath=>//*[@id="bz"]'  # 备注
    ioee_w = 'xpath=>//*[@id="operation"]'  # 经营单位
    awb_save_w = 'xpath=>//*[@id="waybill-btn"]'  # 保存按钮
    iframe = 'BookingManagement/addBooking.jsp'
    def __init__(self, driver):
        self.driver = driver
    def w_booking_by_awb(self):
        self.click(self.booking_mgt_w)
        time.sleep(1)
        self.click(self.booking_by_awb_w)
        time.sleep(1)
        # self.driver.switch_to.frame(self.driver.find_element_by_tag_name('iframe')[0])
        self.driver.switch_to.frame(1)
        logger.info('切换iframe成功')
        time.sleep(1)
        awb_no = New_AwbNo()
        new_awbno = awb_no.new_awbno()
        print(new_awbno)
        time.sleep(2)
        self.type(self.awbno_w, new_awbno)
        time.sleep(1)
        self.type(self.dep_w, 'KMG')
        time.sleep(1)
        self.type(self.piece_w, '100')
        time.sleep(1)
        self.type(self.grossweight_w, '100')
        time.sleep(1)
        self.type(self.chargeableweight_w, '100')
        time.sleep(1)
        self.type(self.rate_w, '10')
        time.sleep(1)
        self.type(self.size_w, '100*100*100*100')
        time.sleep(1)
        self.type(self.origin_w, 'KMG')
        time.sleep(1)
        self.type(self.sono_w, '123456')
        time.sleep(1)
        self.type(self.goods_code_w, '货品')
        time.sleep(1)
        self.click(self.packingtype_w)
        time.sleep(1)
        self.click(self.precision_packaging_w)
        time.sleep(1)
        self.click(self.declaration_type_w)
        time.sleep(1)
        self.click(self.general_trade_w)
        time.sleep(1)
        self.type(self.memo_w, '测试')
        time.sleep(1)
        self.type(self.ioee_w, '友和道通')
        time.sleep(1)
        self.click(self.awb_save_w)
# if __name__ == 'main':
#     book_awb = W_Booking_By_Awb()
#     book_awb.w_booking_by_awb()