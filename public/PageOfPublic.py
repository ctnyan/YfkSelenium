# -*- coding:utf-8 -*-

"""
@version: 1.0
@author: fky
@file: PageOfPublic.py
"""
from public.logger import Logger
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time,os
from selenium.webdriver.common.action_chains import ActionChains


class PageOfPublic():
    mylogger = Logger(logger='PageOfPublic').getlog()

    def __init__(self,browser = 'chrome'):
        if browser.lower() == "chrome":
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.implicitly_wait(10)

        if browser.lower() == "firefox":
            driver = webdriver.Firefox()
            driver.maximize_window()
            driver.implicitly_wait(10)

        if browser.lower() == "ie":
            driver = webdriver.Ie()
            driver.maximize_window()
            driver.implicitly_wait(10)

        try:
            self.driver = driver
        except Exception:
            raise Exception("Not found %s browser,you can enter chrome,firefox or ie again." %browser)



    def find_element(self,findType,selector):
        if findType.lower() == "id":
            return self.driver.find_element_by_id(selector)

        if findType.lower() == "name":
            return self.driver.find_element_by_name(selector)

        if findType.lower() == "class":
            return self.driver.find_element_by_class_name(selector)

        if findType.lower() == "xpath":
            return self.driver.find_element_by_xpath(selector)

        if findType.lower() == "css":
            return self.driver.find_element_by_css_selector(selector)

        if findType.lower() == "linktext":
            return self.driver.find_element_by_link_text(selector)

        if findType.lower() == "partiallinktext":
            return self.driver.find_element_by_partial_link_text(selector)
        else:
            raise Exception("Not found %s,Please enter a right selector like 'id','xpath','css'." %findType)

    def find_elements(self,findType,selector):
        if findType.lower() == "id":
            return self.driver.find_elements_by_id(selector)

        if findType.lower() == "name":
            return self.driver.find_elements_by_name(selector)

        if findType.lower() == "class":
            return self.driver.find_elements_by_class_name(selector)

        if findType.lower() == "xpath":
            return self.driver.find_elements_by_xpath(selector)

        if findType.lower() == "css":
            return self.driver.find_elements_by_css_selector(selector)

        if findType.lower() == "linktext":
            return self.driver.find_elements_by_link_text(selector)

        if findType.lower() == "partiallinktext":
            return self.driver.find_elements_by_partial_link_text(selector)
        else:
            raise Exception("Not found %s,Please enter a right selector like 'id','xpath','css'." %findType)

    def set_failed(self,e):
        self.screen()
        print(e)



    def open_url(self,url,eleName):
        self.driver.get(url)
        self.mylogger.info("打开"+ eleName)

    def input_text(self,findType,selector,text,eleName):
        PageOfPublic.find_element(self, findType, selector).clear()
        PageOfPublic.find_element(self, findType, selector).send_keys(text)
        self.mylogger.info("在【" + selector + "】中输入" + eleName)

    def click(self,findType,selector,eleName):
        PageOfPublic.find_element(self,findType,selector).click()
        self.mylogger.info("【" + selector + "】点击" + eleName)

    def quit(self,eleName):
        self.driver.quit()
        self.mylogger.info(eleName)

    def sleep(self,sleepTime,eleName):
        time.sleep(sleepTime)
        self.mylogger.info(eleName)

    def web_elements(self,findType,selector,eleName):
        elements = PageOfPublic.find_elements(self,findType,selector)
        self.mylogger.info("【" + selector + "】获取" + eleName)
        return elements

    def get_text(self,findType,selector,eleName):
        text = PageOfPublic.find_element(self,findType,selector).text
        self.mylogger.info("【" + selector + "】得到文本:" + eleName + text)
        return text

    def get_attribute(self,findType,selector,name):
        attribute = PageOfPublic.find_element(self,findType,selector).get_attribute(name)
        self.mylogger.info("根据【" + selector + "】得到" + name + "的属性为" + str(attribute))
        return attribute

    def select_by_value(self,findType,selector,value,eleName):
        Select(PageOfPublic.find_element(self,findType,selector)).select_by_value(value)
        self.mylogger.info("【" + selector + "】选择值" + eleName)

    def screen(self):
        nowTime = time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime(time.time()))
        pic_path = '..\\result\\screen\\'+ nowTime + '.png'
        self.driver.get_screenshot_as_file(pic_path)
        print(pic_path)
        self.mylogger.info("截图")

    def upLoad(self,findType,selector,file,eleName):
        PageOfPublic.find_element(self,findType,selector).send_keys(file)
        self.mylogger.info("上传文件" + eleName)

    def switch_to_frame(self,findType,selector,eleName):
        if findType.lower() == "id":
            self.driver.switch_to.frame(selector)
            self.mylogger.info("根据【" + selector + "】切换到" + eleName)
        if findType.lower() == "name":
            self.driver.switch_to.frame(selector)
            self.mylogger.info("根据【" + selector + "】切换到" + eleName)
        else:
            self.driver.switch_to.frame(PageOfPublic.find_element(self,findType,selector))
            self.mylogger.info("根据【" + selector + "】切换到" + eleName)

    def exit_to_frame(self,eleName):
        self.driver.switch_to.default_content()
        self.mylogger.info("退出" + eleName)


    def execute_my_script(self,js,eleName):
        self.driver.execute_script(js)
        self.mylogger.info(eleName)

    def mouse_over(self,findType,selector,eleName):
        ActionChains(self.driver).move_to_element(PageOfPublic.find_element(self,findType,selector)).perform()
        self.mylogger.info("根据【" + selector + "】鼠标悬浮在" + eleName)

    def keyWord(self,findType,selector,keyWord,eleName):
        PageOfPublic.find_element(self,findType,selector).send_keys(keyWord)
        self.mylogger.info("根据【" + selector + "】执行" + eleName + "键")

    # 该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false
    def isElementExist(self, findType,selector,eleName):
        flag = True
        try:
            PageOfPublic.find_element(self,findType,selector)
            self.mylogger.info("判断["+ selector + "】" + eleName)
            return flag

        except:
            flag = False
            return flag

    def get_title(self,eleName):
        title = self.driver.title
        self.mylogger.info("获取标题：【" + eleName + "】")
        return title


    def scroll_To_Element(self,findType,selector,eleName):
        scroll_add_crowd_button = PageOfPublic.find_element(findType,selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_add_crowd_button)
        self.mylogger.info("滚动到滚动条到" + eleName)




        
        
