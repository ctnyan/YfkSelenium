"""
@author: yfk
@file:caseStatusSetting.py
@date: 2020/8/14 19:07
@ide: PyCharm


"""
import os
import pandas as pd
from pandas import DataFrame
import configparser

class CaseStatusSetting(object):

    def __init__(self):

        # 读取配置文件数据config.ini
        config = configparser.ConfigParser()
        demoCase_path = os.path.join(os.path.dirname(os.getcwd()), 'data\\config.ini')
        config.read(demoCase_path, encoding='utf-8')
        self.proj_value = config.get(u'项目路径', 'demoCase_path')
        #print(self.proj_value)

    def getCaseFile(self):
        '''
        该方法用于读取项目中的用例文件名
        :return:
        '''
        pt = 'excelCase\\' + self.proj_value
        project_directPath = os.path.join(os.path.dirname(os.getcwd()), pt)
        list = []
        for root, dirs, files in os.walk(project_directPath):
            for file in files:
                file = os.path.join(root + "\\" + file)
                list.append(file)
        return list

    def caseStatusSetting_all(self):
        path_lists = CaseStatusSetting().getCaseFile()

        #全量更新
        dict = {"用例名称":path_lists,"是否执行":"是"}
        df = pd.DataFrame(dict)
        df.to_excel('caseStatusSetting.xlsx',index=0)


    def caseStatusSetting_incremental(self,fileName):
        path_lists = CaseStatusSetting().getCaseFile()
        #excel_path = os.path.join(os.getcwd(),'caseStatusSetting.xlsx')
        df = pd.read_excel(fileName)
        data = pd.DataFrame(df)

        #增量更新数据，不会去对原有的用例状态（是/否）进行更改，需要测试人员自己去维护
        list_va = data.values.tolist()
        #print(list_va)

        #sum(1 for _ in list_va这个是统计列表长度，这里如果用len()会有个警告提示，所以先把他就当成是一个iterator来处理了
        for x in range(sum(1 for _ in list_va)):
            if list_va[x][0]  not in path_lists:
                #删除表格中多余的用例数据（行删除）
                data = data.drop([x],axis=0,inplace = False)

        for y in range(len(path_lists)):
            #读取项目目录，如果没有的用例会加进来，默认执行状态是“是”
            if path_lists[y] not in data['用例名称'].values.tolist():
                data.loc[y] = [path_lists[y],"是"]


        DataFrame(data).to_excel(fileName, index=0, header=True)






if __name__ == "__main__":
    # li = CaseStatusSetting().getCaseFile()
    # print(li)

    #调用此方法来更新表格中的测试用例清单
    excel_path = os.path.join(os.getcwd(), 'caseStatusSetting.xlsx')
    CaseStatusSetting().caseStatusSetting_all()
    #CaseStatusSetting().caseStatusSetting_incremental(excel_path)

