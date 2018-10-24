# _*_ coding: utf - 8 _*_
from framework.logger import Logger
from framework.base_page import Base_page
import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from data_create.awb_no import New_AwbNo
from hkssms_page.w_open_table import W_Open_table

logger = Logger(logger='W_Booking_By_Awb').getlogger()

class W_Booking_By_Awb(Base_page):
    # 定位各个元素
    booking_mgt_w = 'xpath=>//*[@id="left-menu"]/a[4]'  # 订舱管理页签组
    booking_by_awb_w = 'xpath=>//*[@id="fbce5b976509432e8f3fc6ce5936a2ef"]/li[1]/a'  # 有运单订舱页签
    awbno_w = 'xpath=>//*[@id="ydh"]'  # 运单号 //*[@id="ydh"]  //*[@id="ydh"]
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
    general_trade_w = 'xpath=>//*[@id="kjbg"]/option[2]'  # 一般贸易  //*[@id="kjbg"]/option[2]  //*[@id="kjbg"]/option[2]
    memo_w = 'xpath=>//*[@id="bz"]'  # 备注
    ioee_w = 'xpath=>//*[@id="operation"]'  # 经营单位
    awb_save_w = 'xpath=>//*[@id="waybill-btn"]'  # 保存按钮
    new_awb = 'xpath=>//*[@id="empty-btn"]'
    iframe = 'BookingManagement/addBooking.jsp'
    close1 = 'xpath=>//*[@id="cleverTabHeaderItem-1540274976351"]/a[2]/span'
    def __init__(self, driver):
        self.driver = driver

    def w_booking_by_awb(self):
        table = W_Open_table(self.driver)
        table.w_open_table()
        self.click(self.booking_mgt_w)
        time.sleep(1)
        self.click(self.booking_by_awb_w)
        time.sleep(1)
        self.driver.switch_to.frame(0)
        self.click(self.close1)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name('iframe')[0])
        self.driver.switch_to.frame(1)
        logger.info('切换iframe成功')
        time.sleep(1)
        awb_no = New_AwbNo()
        new_awbno1 = awb_no.new_awbno()
        time.sleep(1)
        # self.driver.find_element_by_xpath('//*[@id="ydh"]').send_keys(new_awbno1)
        self.type(self.awbno_w, new_awbno1)
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
        # 点击包装类型
        # # self.click(self.precision_packaging_w)
        # self.driver.find_element_by_xpath('//*[@id="bzlx"]')
        # logger.info('点击包装类型输入框')
        # # ab = self.driver.find_element_by_id('bzlx')
        # # ab.find_element_by_xpath('//option[@value="bzlx_002"]').click()
        # self.driver.find_element_by_id("cardType").select_by_value('bzlx_002')
        # # self.driver.find_element_by_xpath('//option[@value="bzlx_002"]').click()
        # s = Select(self.driver.find_element_by_id("bzlx"))
        # logger.info('定位select框架')
        # s.select_by_visible_text('精包装')
        # logger.info('定位下拉框内容')


        js = "$('.精包装').parent('.listingBox_content').find('select.bzlx_002').click()"  # 使用js查找元素  选择产品
        self.driver.implicitly_wait(5)
        self.driver.execute_script(js)

        # s.select_by_value("bzlx_002")
        time.sleep(1)
        self.click(self.declaration_type_w)
        time.sleep(1)
        # self.click(self.general_trade_w)
        self.driver.find_element_by_xpath('//*[@id="kjbg"]')
        # ac = self.driver.find_element_by_id('kjbg')
        # ac.find_element_by_xpath('//option[@value="KJBG002"]').click()
        self.driver.find_element_by_xpath('//option[@value="KJBG002"]').click()
        time.sleep(1)
        self.type(self.memo_w, '测试')
        time.sleep(1)
        self.type(self.ioee_w, '友和道通')
        time.sleep(1)
        self.click(self.awb_save_w)
        time.sleep(1)
        # self.click(self.new_awb)
        # time.sleep(2)
# if __name__ == 'main':
#     book_awb = W_Booking_By_Awb()
#     book_awb.w_booking_by_awb()