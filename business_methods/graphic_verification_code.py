# _*_ coding: utf - 8 _*_
# The author: seven
import os, sys
# os.chdir('D:\\Program Files (x86)\\Lib\\site-packages\\pytesser_v0.0.1')
sys.path.append('C:\\Users\\songyufang\\PycharmProjects\\HKSSMSPlatform')
sys.path.append('D:\\Program Files (x86)\\Lib\\site-packages')
# os.chdir('D:\\Program Files (x86)\\Lib\\site-packages\\PIL')
import pytesseract
import time
from PIL import Image, ImageEnhance
from framework.logger import Logger

logger = Logger(logger='Code').getlogger()

class Code():
    def __init__(self, driver):
        self.driver = driver

    def img_code(self, imgelement):
        self.driver.save_screenshot('E://Img.png')  # 截取当前网页需要的验证码
        img_element = self.driver.find_element_by_xpath(imgelement)  # 定位验证码
        location = img_element.location  # 获取验证码x,y轴坐标
        size = img_element.size   # 获取验证码的长宽
        rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']), int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
        i = Image.open('E://Img.png')  # 打开截图
        frame = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
        frame = frame.convert('RGB')  # 图像加强，二值化，PIL中有九种不同模式。分别为1，L，P，RGB，RGBA，CMYK，YCbCr，I，F。L为灰度图像
        frame.save('E://captchaImg.jpg') # 保存处理后的图片
        qq = Image.open('E://captchaImg.jpg')  # 打开处理过的图片
        imgry= qq.convert('L')