# coding:utf-8
from public.PageOfPublic import PageOfPublic
import unittest
from data.baidu import *
from public.logger import Logger

class PageTest1(unittest.TestCase):
    u'''博客园测试'''

    def setUp(self):
        self.mylogger = Logger(logger='PageTest1').getlog()
        driver = PageOfPublic("chrome")
        self.driver = driver


    def tearDown(self):
        self.driver.quit("退出浏览器")

    def test_01(self):
        u"""定位失败截图案例"""
        try:

            self.driver.open_url(baidu_url,"百度网页")
            self.driver.input_text("id","skw",input_text,"搜索内容")
            self.driver.click('id','su',"搜索按钮")
        except Exception as e:
            self.mylogger.info(e)
            self.driver.screen()
            raise

    def test_02(self):
        u'''失败用例'''
        try:
            self.driver.open_url(yoyou_blog,"悠悠博客首页")
            t = self.driver.get_title('上海-悠悠 - 博客园')
            self.assertIn(u"悠s悠",t)
        except Exception as e:
            self.mylogger.info(e)
            self.driver.screen()
            raise

    def test_03(self):
        u'''通过用例'''
        try:
            self.driver.open_url(yoyou_blog,"悠悠博客首页")
            self.assertIn(u"上海-悠悠",self.driver.get_title("上海-悠悠 - 博客园"))
        except Exception as e:
            self.mylogger.info(e)
            self.driver.screen()
            raise

if __name__ == "__main__":
    unittest.main()
