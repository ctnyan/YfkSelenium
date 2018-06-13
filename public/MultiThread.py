# -*- coding:utf-8 -*-

"""
@version: 1.0
@author: fky
@file: RunThreads.py
"""

import threadpool

class MultiThread():
    def __init__(self,func,count=1,data=None):
        self.count = count
        self.func = func
        self.data = data

    def pool(self):

        #创建线程池
        pool = threadpool.ThreadPool(self.count)

        # 生成线程池要执行的东西，makeRequests,传入数量，自动找出每个线程要执行的数据
        reqs = threadpool.makeRequests(self.func, self.data)

        # 创建多个任务put到线程池中
        for req in reqs:
            pool.putRequest(req)
        pool.wait()