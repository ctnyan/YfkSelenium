"""
@author: yfk
@file:readExcel.py
@date: 2020/8/12 10:22
@ide: PyCharm

"""
import xlrd,os
from public.logger import Logger
from public.pageElement import PageElement
from data.caseStatusSetting import CaseStatusSetting

class ReadExcel(object):
    mylogger = Logger(logger='readExcel').getlog()
    def __init__(self):

        # 设置标志位flag，每次执行用例前先检查一下表格数据是否正确，如果有误，则flage=0,并给出对应错误提示
        self.flag = 1

    def read_caseStatusSetting(self,excel_statSetting_path):
        #每次读取caseStausSetting前先跑一下case更新
        CaseStatusSetting().caseStatusSetting_incremental(excel_statSetting_path)

        f = xlrd.open_workbook(excel_statSetting_path)
        table = f.sheet_by_index(0)
        nrows = table.nrows
        case_list =[]
        for row in range(1,nrows):
            row_value = table.row_values(row)
            case_list.append(row_value)
        return case_list

    def getFlag(self,fileName):
        f = xlrd.open_workbook(filename=fileName)
        #h获取excel第一个表格
        table = f.sheets()[0]
        nrows = table.nrows

        for x in range(1,nrows):
            #获取每一行对应的列数据
            ncols = table.row_values(x,end_colx=None)

            #如果表格的列数据位置有增改时这类需要修改索引
            keyword = ncols[0]
            is_excute = ncols[5]
            location_method =  ncols[2]
            location = ncols[3]
            p = PageElement("driver")
            if hasattr(p,keyword):
                pass
            elif ":\\" in keyword:
                #存在文件路径的就递归调用
                self.getFlag(keyword)
            else:
                self.mylogger.info("用例位置："+ fileName + " - Row" + str(x) + "：【" + keyword + "】在系统不存在或为空请仔细检查！")
                #break
                self.flag = 0

            if is_excute == "否" or is_excute == "是":
                pass
            elif is_excute == "":
                self.mylogger.info("用例位置："+ fileName + " - Row" + str(x) + "：【" + is_excute + "】不能为空是必填")
                #break
                self.flag = 0

            else:
                self.mylogger.info("用例位置："+ fileName + " - Row" + str(x) + "：【" + is_excute + "】只能填是或否")
                #break
                self.flag = 0

        return self.flag




    def readExcel(self,fileName,caseName,driver,m=1):
        #内部调用getFlag函数检查表格数据完整性
        flag = ReadExcel().getFlag(fileName)
        count = m
        if flag == 1:
            f = xlrd.open_workbook(filename=fileName)
            # h获取excel第一个表格
            table = f.sheets()[0]
            nrows = table.nrows
            if m == 1:
                self.mylogger.info("数据校验完毕，即将开始执行用例:" + caseName)
            for y in range(1,nrows):
                ncols = table.row_values(y,end_colx=None)
                keyword = ncols[0]
                name = ncols[1]
                location_method = ncols[2]
                location = ncols[3]
                value = ncols[4]
                is_excute = ncols[5]

                #先把为空的清除掉再传参，不然会出问题
                if is_excute == "否":
                    continue
                dict_case = {}
                dict_case["eleName"] = name
                dict_case["findType"] = location_method
                dict_case["selector"] = location
                dict_case["text"] = value


                for key in list(dict_case.keys()):
                    if dict_case[key] == "":
                        dict_case.pop(key)
                #print(keyword)
                if  ':\\' in keyword:
                    m = count + 1
                    self.readExcel(keyword,caseName,driver,m)
                else:
                    try:
                        ob = PageElement(driver)
                        pt = getattr(ob, keyword)
                        pt(**dict_case)
                        if y == nrows - 1:
                            self.mylogger.info("用例执行完毕")
                    except Exception as e:
                        #用例失败时抛出异常以便在用例集里面捕获
                        raise e






if __name__ == "__main__":
    from public.pageElement import InitDriver
    driver = InitDriver().openBrowser()
    fileName = "E:/fukun测试项目/YfkSelenium/excelCase/demo测试用例/功能模块/PR管理/PR查询/嵌套公共业务模块的演示.xlsx"
    ReadExcel().readExcel(fileName,'嵌套公共业务模块的演示.xlsx',driver)


