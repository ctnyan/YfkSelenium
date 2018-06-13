# -*- coding:utf-8 -*-

"""
@version: 1.0
@author: fky
@file: Timing.py
"""

import schedule
import time

class Timing():

    #按秒循环定时执行任务
    def doEverySecond(self,seconds,job_func):
        try:
            schedule.every(seconds).seconds.do(job_func)
            while True:
                schedule.run_pending()

        except Exception as e:
            raise e

    # 按分钟循环定时执行任务
    def doEveryMinutes(self,minutes,job_func):
        try:
            schedule.every(minutes).minutes.do(job_func)
            while True:
                schedule.run_pending()

        except Exception as e:
            raise e

    # 按小时循环定时执行任务
    def doEveryHours(self,Hours,job_func):
        try:
            schedule.every(Hours).minutes.do(job_func)
            while True:
                schedule.run_pending()

        except Exception as e:
            raise e


    #按天数在某个时刻定时执行任务
    def doEveryDay(self,time,job_func,days=1):
        try:
            schedule.every(days).days.at(time).do(job_func)
            while True:
                schedule.run_pending()
        except Exception as e:
            raise e


    #设置在每天的多个时刻定时执行任务,这个方法在实际工作中比较常用到
    def doEveryTime(self,time_str,job_func,days=1):
        '''

        :param time_str:
        :param job_func:
        :param days:
        :return: None
        example:time_str="10:30","10:45","11:00"
        '''

        try:
            list_time = time_str.split(",")
            for time in list_time:
                schedule.every(days).days.at(time).do(job_func)
            while True:
                schedule.run_pending()
        except Exception as e:
            raise e

    #自定义时间，dateTimes格式为："2018-06-08 16:55,2018-06-08 16:56"
    def doJustTime(self,datestr,job_func):
        try:
            date_list = datestr.split(",")
            print(date_list)
            for i in date_list:
                #转换为unix时间戳格式
                timeArray = time.strptime(i, "%Y-%m-%d %H:%M")
                timestamp = time.mktime(timeArray)
                while True:
                    now_time = round(time.time(),0)
                    if timestamp == now_time:
                        job_func()
                        break
                    else:
                        time.sleep(1)

        except Exception as e:
            raise  e


if __name__ == "__main__":
    def print1():
        print("ok")
    Timing().doJustTime('2018-06-08 17:53,2018-06-08 17:54',print1)
