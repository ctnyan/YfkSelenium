

"""
@author: yfk
@file:testCase_PR查询
@date: 2020/08/17 18:05
@ide: PyCharm
""" 
from public.pageElement import PageElement,InitDriver
from data.baidu import *
import unittest
from public.logger import Logger
from public.readExcel import ReadExcel
import os,sys


class TestCase_PR查询(unittest.TestCase):
    #path = os.getcwd()
    #gen_path = os.path.abspath(os.path.dirname(path))
    #data_path = gen_path + '\excelCase\demo测试用例\\功能模块\\PR管理\\PR查询'
    data_path = 'E:/fukun测试项目/YfkSelenium/excelCase/demo测试用例/功能模块/PR管理/PR查询/'
    mylogger = Logger(logger='testCase_PR查询.py').getlog()
    
    def setUp(self):
        self.driver = InitDriver().openBrowser()

    def tearDown(self):
        pass

    def test_PR查询(self):
        caseName = 'PR查询.xlsx'
        file_name = os.path.join(self.data_path,caseName )
        try:
            ReadExcel().readExcel(file_name,caseName,self.driver)
        except Exception as e:
            #执行异常抛异常，用于反映在测试报告
            self.mylogger.info('用例 "{}"执行失败'.format(caseName))
            PageElement(self.driver).screen()
            raise
            
            