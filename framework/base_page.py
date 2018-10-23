# _*_ coding: utf - 8 _*_
import time
import os
from framework.logger import Logger
from selenium.common.exceptions import NoSuchElementException

logger = Logger(logger='').getlogger()

class Base_page(object):
    """
    定义页面基类，让所有页面都继承这个基类，封装常用的页面操作方法
    """
    def __init__(self, driver):
        self.driver = driver
    # 关闭浏览器
    def quit_browser(self):
        self.driver.quit()
        logger.info('quit browser')
    # 浏览器前进操作
    def forward(self):
        self.driver.forward()
        logger.info('click forward on current page')
    # 刷新浏览器操作
    def refresh(self):
        self.driver.refresh()
        logger.info('refresh browser')
     # 浏览器退后操作
    def back(self):
        self.driver.back()
        logger.info('click back on current page')
    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info('wait for %s' % seconds)
    # 关闭窗口
    def close(self):
        try:
            self.driver.close()
            logger.info('closer the browser')
        except Exception as e:
            logger.error('failed to close the browser with %s' % e)
    # 保存图片
    def get_window_img(self):
        """
        将截图文件保存到我们项目根目录的一个文件夹.\screenshots下
        :return:
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        img_name = file_path + rp + '.png'
        try:
            self.driver.get_screen_as_file(img_name)
        except Exception as e:
            logger.error("Failed to take screenshot! %s" % e)
    # 定位元素
    def find_element(self, selector):
        """
        这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
        submit_btn = "id=>su"
        login_lnk = "xpath => //*[@id='u1']/a[7]" #百度首页登录链接定位
        如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return:
        """
        element = ''
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        if selector_by == 'i' or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info("Had find the element \' %s \' seccessful"
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
        elif selector_by == 'n' or selector_by == 'name':
            try:
                element = self.driver.find_element_by_name(selector_value)
                logger.info("Had find the element \' %s \' seccessful"
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
        elif selector_by == 'c' or selector_by == 'class_name':
            try:
                element = self.driver.find_element_by_class_name(selector_value)
                logger.info("Had find the element \' %s \' seccessful"
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
        elif selector_by == 'l' or selector_by == 'link_text':
            try:
                element = self.driver.find_element_by_link_text(selector_value)
                logger.info("Had find the element \' %s \' seccessful"
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
        elif selector_by == 'p' or selector_by == 'partial_link_text':
            try:
                element = self.driver.find_element_by_partial_link_text(selector_value)
                logger.info("Had find the element \' %s \' seccessful"
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
        elif selector_by == 't' or selector_by == 'tag_name':
            try:
                element = self.driver.find_element_by_tag_name(selector_value)
                logger.info("Had find the element \' %s \' seccessful"
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
        elif selector_by == 'x' or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info("Had find the element \' %s \' seccessful"
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementExcept: %s" % e)
        elif selector_by == 's' or selector_by == 'selector_selector':
            try:
                element = self.driver.find_element_by_css_selector(selector_value)
                logger.info("Had find the element \' %s \' seccessful"
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
        else:
            raise NameError("Please enter a valid type of targeting elements.")
        return element
    # 文本输入
    def type(self, selector, text):
        el = self.find_element(selector)
        logger.info('找到元素： %s' % el)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type \' %s \' in inputbox" % text)
        except NameError as e:
            logger.error("Failed to type in inputBox with %s" % e)
    # 清除文本框内容
    def clear(self, selector):
        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("Clear the text in inputBox before typing.")
        except NameError as e:
            logger.error("Failed to clear the inputbox %s" % e)
    # 点击元素
    def click(self, selector):
        el = self.find_element(selector)
        try:
            el.click()
            logger.info("Had click the element \' %s \'" % el.text)
        except NameError as e:
            logger.error("Failed to click the element" % e)
    # 获取网页标题
    def get_page_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title
    # 获取页面上元素的值
    def get_page_num(self, selector):
        num = self.find_element(selector).get_attribute("value")
        return num
    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d second" % seconds)