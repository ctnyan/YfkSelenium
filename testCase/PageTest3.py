# -*- coding:utf-8 -*-

from public.PageOfPublic import PageOfPublic
from data.baidu import *
import unittest
from public.logger import Logger


class PageTest3(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mylogger = Logger(logger='PageTest2').getlog()
        cls.driver = PageOfPublic("Chrome")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit("退出浏览器")

    #错误用例
    def test_01(self):
        try:
            self.driver.open_url(baidu_url, '打开百度')
            self.driver.input_text("xpath",'//*[@id="kw"]',input_text,'输入内容')
            self.driver.click('xpath','//*[@id="s3u"]','点击搜索按钮')
            self.driver.sleep(1,"延时1秒")
        except Exception as e:
            self.mylogger.info(e)
            self.driver.screen()
            raise

    #正确用例
    def test_02(self):
        try:
            self.driver.open_url(baidu_url, '打开百度')
            self.driver.input_text("xpath",'//*[@id="kw"]',input_text,'输入内容')
            self.driver.click('xpath','//*[@id="su"]','点击搜索按钮')
            self.driver.sleep(1,"延时1秒")
        except Exception as e:
            self.mylogger.info(e)
            self.driver.screen()
            raise

            

if __name__ == '__main__':
    unittest.main()