# -*- coding:utf-8 -*-

from public.PageOfPublic import PageOfPublic
from data.baidu import *
import unittest
from public.logger import Logger



class PageTest3(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mylogger = Logger(logger='PageTest5').getlog()
        cls.driver = PageOfPublic("chrome")

    @classmethod
    def tearDownClass(cls):
        cls.driver.sleep(5,'延时5秒')
        cls.driver.quit("退出浏览器")

    def test_01(self):
        try:
            self.driver.open_url('file:///C:/Users/13694/Desktop/upLoad.html', '打开测试页面')
            self.driver.upLoad('xpath','//input[@id="file2"]','C:\\Users\\13694\\Desktop\\test1.txt','上传文件')
            self.driver.sleep(5, "延时5秒")
        except Exception as e:
            self.mylogger.info(e)
            self.driver.screen()
            raise



if __name__ == '__main__':
    unittest.main()