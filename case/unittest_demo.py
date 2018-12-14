# Author:
# Data:
# Status

import unittest, HTMLTestRunner
from base.Run_main import RunMain
from base.demo_mock import mock_test


class UnittestDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # 比如所有用例都需要登陆一次
        # cls.run_main=RunMain()
        print(">>>>>>>>>>>>类执行之前的方法\n")

    def setUp(self):  # 执行用例前把类实例化放这里
        self.run = RunMain()
        print(">>>>>>>>>>>>方法执行之前，每次会执行它\n")

    def tearDown(self):
        print(">>>>>>>>>>>>方法执行之后，每次会执行它\n")

    @classmethod
    def tearDownClass(cls):  # 比如所有用例执行完成之后的环境清理
        print(">>>>>>>>>>>>类执行之后的方法\n")

    def test_0001(self):  # 方法必须以test开头，且按顺序执行
        params2 = {
            'typeId': '888888888888888888888888888',
            'pageNo': '1',
            'pageSize': '5',
        }
        url2 = 'http://api.yishengyue.cn/api/v1/topic'
        res = self.run.run_main('GET', url2, params2)  # 这里返回的已经是
        print(type(res), '\n', res)
        print(">>>>>>>>>>>>这是第一个测试方法\n")
        self.assertEqual(res['code'], 0, '接口返回状态吗不正确')  # 注意这里是按字符来处理的
        globals()['varr1'] = 0

    def test_0002(self):
        print('打印已生效全局变量global_var1：')
        params2 = {
            'typeId': '888888888888888888888888888',
            'pageNo': '1',
            'pageSize': '5',
        }
        url2 = 'http://api.yishengyue.cn/api/v1/topic'
        res = mock_test(self.run.run_main, 'POST', url2, params2, params2)
        self.assertEqual(res['pageNo'], 1, '接口返回状态吗不正确')  # 注意这里是按字符来处理的
        print(">>>>>>>>>>>>这是第二个测试方法\n")

    @unittest.skip('test_0003')
    def test_0003(self):
        print(">>>>>>>>>>>>这是第三个测试方法")


if __name__ == '__main__':
    # 第一种执行方式，执行所有
    # unittest.main()             #特殊执行方式
    # 第二种，执行制定名字开头的用例
    # suite = unittest.TestSuite()
    # suite.addTest(UnittestDemo('test_00*'))
    # unittest.TextTestRunner().run(suite)
    # 第三种，结合html执行
    file_path = r'D:\Job\pythonStudy\django_requests\report\htmlreport.html'  # 注意这里是全路径，且r代表转义内容
    with open(file_path, 'wb') as fp:  # 对html文件进行读写
        suite = unittest.TestSuite()
        suite.addTest(UnittestDemo('test_0001'))
        suite.addTest(UnittestDemo('test_0002'))
        suite.addTest(UnittestDemo('test_0003'))
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="Alwin's first report!")
        runner.run(suite)
