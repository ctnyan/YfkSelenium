"""
@author: yfk
@file:autoCase.py
@date: 2020/8/14 9:55
@ide: PyCharm


"""
import xlrd
import sys
import os
import re,time
from public.readExcel import ReadExcel


def autoCase(excel_statSetting_path):
    case_path = os.path.join(os.path.dirname(os.getcwd()),'testCase')

    #先删掉testCase目录下的用例
    case_list =[]
    for root, dirs, files in os.walk(case_path):
        for file in files:
            file = os.path.join(root + "\\" + file)
            case_list.append(file)
    for case in case_list:
        os.remove(case)

    #读read_caseStatusSetting.xlsx的用例状态
    #excel_statSetting_path = os.path.join(os.path.dirname(os.getcwd()), 'data\\caseStatusSetting.xlsx')
    case_statusList = ReadExcel().read_caseStatusSetting(excel_statSetting_path)

    flag = 1
    for index in range(len(case_statusList)):
        #不可执行的用例从表中删除
         if case_statusList[index][1] == "否":
            case_statusList.pop(index)
         elif case_statusList[index][1] == "是":
            pass
         else:
             flag = 0
             print("执行状态:" + case_statusList[index][1] + "须填【是/否】z状态")
    if flag == 1:
        case_list = []
        for x in case_statusList:
            #去掉表中的执行状态
            x.pop(1)
            m = ''.join(i for i in x)
            case_list.append(m)
        for i in case_list:
            #excel_name = str2 = i.split('\\')[len(i.split('\\'))-1].strip('.xlsx')
            #把用例名提取出来去掉".**"后缀名
            str2 = i.split('\\')[len(i.split('\\')) - 1]    #带后缀的用例名
            str3 = re.findall(r'\.\w+', str2)
            excel_name = str2.strip(str3[len(str3) - 1])
            case_name =os.path.join(case_path,"testCase_{0}.py".format(excel_name))

            #获得每个用例的绝对路径
            m_path = ''.join(x for x in re.findall(r'\w+.\w+$', i))
            direct_path = i.strip(m_path).replace('\\','/')
            sy_time = time.strftime("%Y/%m/%d %H:%M", time.localtime())
            with open(case_name,'w',encoding='utf-8') as out:
                out.write('''

"""
@author: yfk
@file:testCase_{0}
@date: {3}
@ide: PyCharm
""" 
from public.pageElement import PageElement,InitDriver
from data.baidu import *
import unittest
from public.logger import Logger
from public.readExcel import ReadExcel
import os,sys


class TestCase_{0}(unittest.TestCase):
    #path = os.getcwd()
    #gen_path = os.path.abspath(os.path.dirname(path))
    #data_path = gen_path + '\\excelCase\\demo测试用例\\\功能模块\\\PR管理\\\PR查询'
    data_path = '{1}'
    mylogger = Logger(logger='testCase_{0}.py').getlog()
    
    def setUp(self):
        self.driver = InitDriver().openBrowser()

    def tearDown(self):
        pass

    def test_{0}(self):
        caseName = '{2}'
        file_name = os.path.join(self.data_path,caseName )
        try:
            ReadExcel().readExcel(file_name,caseName,self.driver)
        except Exception as e:
            #执行异常抛异常，用于反映在测试报告
            self.mylogger.info('用例 "{{}}"执行失败'.format(caseName))
            PageElement(self.driver).screen()
            raise
            
            '''.format(excel_name,direct_path,str2,sy_time) )



autoCase(os.path.join(os.path.dirname(os.getcwd()), 'data\\caseStatusSetting.xlsx'))