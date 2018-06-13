# -*- coding:utf-8 -*-
from public.PageOfPublic import PageOfPublic
from data.baidu import *
import unittest
from public.logger import Logger



class PageTest2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mylogger = Logger(logger='PageTest2').getlog()
        cls.driver = PageOfPublic("Chrome")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit("退出浏览器")


    def test_baidu_01(self):
        try:
            self.driver.open_url(baidu_url, '百度首页')
            self.driver.input_text("xpath",'//*[@id="kw"]',input_text,'输入内容')
            self.driver.click('xpath','//*[@id="su"]','点击搜索按钮')
            text = self.driver.get_text('xpath','//*[@id="4"]/h3/a','test百度百科')
            print(text)
            self.driver.sleep(5,"延时5秒")
        except Exception as e:
            self.mylogger.info(e)
            self.driver.screen()
            raise

if __name__ == "__main__":
    unittest.main()


