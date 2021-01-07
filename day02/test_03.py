'''
测试前置：类级别和方法级别
'''

class Test001: # 测试类以Test开头
    def setup_class(self):
        print("测试前置:类级别，类开始前执行")

    def teardown_class(self):
        print("测试后置:类级别，类结束后执行")

    def setup_method(self):
        print("测试前置:方法级别，方法开始前执行")

    def teardown_method(self):
        print("测试后置:方法级别，方法结束后执行")

    def test_case001(self):
        print("测试用例1")

    def test_case002(self):
        print("测试用例2")

    def test_case003(self):
        print("测试用例3")
