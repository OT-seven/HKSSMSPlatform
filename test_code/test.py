# _*_ utf - 8 _*_
# The author: seven
import os,sys
# os.chdir('D:\\Program Files (x86)\\Lib\\site-packages\\pytesser_v0.0.1')
sys.path.append('C:\\Users\\songyufang\\PycharmProjects\\HKSSMSPlatform')
sys.path.append('D:\\Program Files (x86)\\Lib\\site-packages')
# os.chdir('D:\\Program Files (x86)\\Lib\\site-packages\\PIL')
from selenium import webdriver
import pytesseract
import time
from PIL import Image, ImageEnhance
from framework.logger import Logger

logger = Logger(logger='Code').getlogger()

class Code():
    def __init__(self,dr):
        self.dr = dr
    @property
    def textcode(self):
        code = self.dr.find_element_by_id('validationCode_img')
        self.dr.execute_script("arguments[0].scrollIntoView();", code)
        self.dr.save_screenshot('E://a.png')  # 截取当前网页需要的验证码
        imgelement = self.dr.find_element_by_xpath('//*[@id="validationCode_img"]')  # 定位验证码
        # imgelement = self.dr.find_element_by_xpath(codeimgelement)  # 定位验证码

        #js = "$('.salary').parent().parent('.listingBox_content').find('input.btn-primary').click()"
        y = "$('#imgSendCaptcha')[0].getBoundingClientRect().top"
        print  (self.dr.execute_script(y))
        print (imgelement)
        x = "$('#imgSendCaptcha')[0].getBoundingClientRect().left"
        print  (self.dr.execute_script(x))
        location = imgelement.location  # 获取验证码x,y轴坐标
        print (location)
        size = imgelement.size  # 获取验证码的长宽
        rangle = (int(location['x']) , int(location['y']) , int(location['x'] + size['width'] ),
                  int(location['y'] + size['height'] ))  # 写成我们需要截取的位置坐标
        i = Image.open("E://a.png")  # 打开截图
        frame5 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
        frame5.save('E://aa.jpg')
        qq = Image.open('E://aa.jpg')
        text = pytesseract.image_to_string(qq)  # .strip() #使用image_to_string识别验证码
        text = text[0:4]
        print (text)
        return text
    def image(self):
        self.dr.save_screenshot('E://Img.png')  #截取当前网页需要的验证码
        imgelement = self.dr.find_element_by_xpath('//*[@id="validationCode_img"]')  #定位验证码
        location = imgelement.location  #获取验证码x,y轴坐标
        size=imgelement.size  #获取验证码的长宽
        rangle=(int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height'])) #写成我们需要截取的位置坐标
        i=Image.open("E://Img.png") #打开截图
        frame5=i.crop(rangle)  #使用Image的crop函数，从截图中再次截取我们需要的区域
        frame5 = frame5.convert('L')  # 图像加强，二值化，PIL中有九种不同模式。分别为1，L，P，RGB，RGBA，CMYK，YCbCr，I，F。L为灰度图像
        sharpness = ImageEnhance.Contrast(frame5)  # 对比度增强
        frame5 = sharpness.enhance(4.0)  # 3.0为图像的饱和度
        frame5.save('E://captchaImg.jpg')  # 保存处理后的图片
        qq=Image.open('E://captchaImg.jpg')  # 打开处理过的图片
        # imgry = qq.convert('L')  # 图像加强，二值化，PIL中有九种不同模式。分别为1，L，P，RGB，RGBA，CMYK，YCbCr，I，F。L为灰度图像
        # sharpness = ImageEnhance.Contrast(imgry)  # 对比度增强
        # i3 = sharpness.enhance(4.0)  # 3.0为图像的饱和度
        # i3.save("E:\\image_code.png")
        # i4 = Image.open("E:\\image_code.png")
        time.sleep(2)
        text=pytesseract.image_to_string(qq).strip()#.strip() #使用image_to_string识别验证码
        # text1=text[0:4]
        print (text)
        logger.info(text)
        return text
    def image1(self):
        qq = Image.open('E://captchaImg.jpg')
        time.sleep(2)
        text = pytesseract.image_to_string(qq).strip()  # .strip() #使用image_to_string识别验证码
        text = text[0:4]
        print (text)
        return text
if __name__=='__main__':
    # driver = WebDriver.GetWebdriver()
    # dr = driver.GetdriverO()
    image=Code('')
    image.image1()
    print(image.image1())