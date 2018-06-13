# -*- coding:utf-8 -*-

"""
@version: 1.0
@author: fky
@file: RunThreadsOnTime.py
"""
import unittest
import os,time
from public.HTMLTestRunner_fky import HTMLTestRunner
import threadpool
from public.MultiThread import MultiThread
from public.Timing import Timing


if __name__ == '__main__':
    testDir = os.path.join(os.getcwd(), '..\\testCase')
    discovers = unittest.defaultTestLoader.discover(testDir, pattern="PageOf*.py")
    runner = unittest.TextTestRunner()

    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_path = "..\\result\\report\\" + current_time + '.html'  # 生成测试报告的路径
    fp = open(report_path, "wb")
    runner = HTMLTestRunner(stream=fp, title=u"自动化测试报告", description=u'自动化测试演示报告',verbosity=2)

    #计算用例个数count
    count = 0
    for x in discovers:
        count = count +1
    print(count)


    #调用多线程执行用例
    def runCase(discovers):
        for i in discovers:
            runner.run(i)
    def MultiThreadRun():
        MultiThread(runCase,count,discovers).pool()

    #定时任务
    Timing().doJustTime("2018-06-09 17:04,2018-06-09 17:06",MultiThreadRun)

    fp.close()