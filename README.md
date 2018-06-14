# YfkSelenium项目说明
## 简介
这是一个基于python 3语言编写的UI自动化测试工具，集成了测试报告，测试日志，错误截图，多线程定时执行任务等相关功能。
## 结构
![Alt text](https://github.com/ctnyan/image/raw/master/picture/1.png)  

- **data目录，存放测试数据；**  
- **logs,存放执行用例的日志；**  
- **public，存放的公共可供调用文件：**    
a. HTMLTestRunner_fky.py为生产测试报告的文件，从网络平台直接copy下了的，带汉化的版本，可以直接使用；  
b. logger.py,集成的用以记录日志的模块；  
c. MultiThread.py,多线程执行任务；  
d. PageOfPublic.py,对Selenium的方法做了二次的封装；  
e. Timing.py,定时执行任务  
- **result,存放测试报告的report目录和错误截屏的screen目录**  
- **runCase,执行测试用例**  
- **testCase,编写用例**  

## 安装介绍
1、安装python 3环境;  
2、安装浏览器驱动,chrome浏览器驱动：chromedriver；firefox驱动：geckodriver，注意和浏览器版本对应，保证兼容性；  
3、安装必要的库文件，可使用pip install packagename安装，如：`pip install selenium`,安装文件如下：    
. selenium   
. threadpool  
. schedule  
## 使用方法 
- **在github上面下载下来整个项目，或者用克隆地址用git下载下来项目；**  
- **使用pycharm或者eclipse打开项目；**  
- **在testCase目录下创建一个PageTest1.py的python文件，写用例代码:**   
    from public.PageOfPublic import PageOfPublic
import unittest
from data.baidu import *
from data.youyouBlog import  *
from public.logger import Logger

class PageTest1(unittest.TestCase):
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
    
    
    


