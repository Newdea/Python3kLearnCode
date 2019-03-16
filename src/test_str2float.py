from unittest import TestCase

# todo: how to make a test case.
class TestStr2float(TestCase):
    print('str2float(\'123.456\') =', str2float('123.456'))
    if abs(str2float('123.456') - 123.456) < 0.00001:
        print('测试成功!')
    else:
        print('测试失败!')

    pass
