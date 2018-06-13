# -*- coding:utf-8 -*-

"""
@version: 1.0
@author: fky
@file: RunTestCase.py
"""

import unittest
import os,time
from public.HTMLTestRunner_fky import HTMLTestRunner


if __name__ == '__main__':
    testDir = os.path.join(os.getcwd(), '..\\testCase')
    discover = unittest.defaultTestLoader.discover(testDir, pattern="PageTest4.py")
    runner = unittest.TextTestRunner()

    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_path = "..\\result\\report\\" + current_time + '.html'  # 生成测试报告的路径
    fp = open(report_path, "wb")
    runner = HTMLTestRunner(stream=fp, title=u"自动化测试报告", description=u'自动化测试演示报告',verbosity=2)
    runner.run(discover)
    fp.close()


    