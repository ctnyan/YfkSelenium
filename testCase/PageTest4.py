# -*- coding:utf-8 -*-


from public.PageOfPublic import PageOfPublic
import time
import unittest
from public.logger import Logger


class PageTest4(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #cls.mylogger = Logger(logger='test3').getlog()
        cls.driver = PageOfPublic("Chrome")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit("退出浏览器")

    def test_baidu(self):
            self.driver.open_url('https://www.hao123.com/','好123网页')
            #js="var q=document.documentElement.scrollTop=100000"
            js="window.scrollTo(0,document.body.scrollHeight)"
            #js="var q=document.body.scrollTop=100000"
            self.driver.execute_my_script(js,'滚动页面到底部')
            self.driver.sleep(1, '延时1秒')
            self.driver.execute_my_script("window.scrollTo(0,0)",'滚动页面到顶部')
            self.driver.sleep(1, '延时1秒')

    if __name__ == '__main__':
        unittest.main()