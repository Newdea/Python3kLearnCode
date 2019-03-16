from functools import reduce


# reduce() and map()


def prod(L):
    pass
    return reduce(lambda x, y: x * y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# --------------------------------------------------------#
def str2float(s):
    DIGITS = {'.': '', '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    sdot = 0

    def char2num(s):
        return DIGITS[s]

    for i, v in enumerate(s):
        if v == '.':
            sdot = i
            s = s[:i] + s[i + 1:]
            break

    return reduce(lambda x, y: x * 10 + y, map(char2num, s)) / pow(10, (len(s) - sdot))  # - sdot
    pass


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


# --------------------------------------------------------------
# filter()
def is_palindrome(n):
    sn = str(n)
    for i, v in enumerate(sn):
        if v != sn[-i - 1]:
            return False
    return True
    pass


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
                                                  111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

# -----------------------------
# sorted()
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0].lower()
    pass


L2 = sorted(L, key=by_name)
print(L2)


def by_score(t):
    return -t[1]
    pass


L2 = sorted(L, key=by_score)
print(L2)


# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
# -*- coding: utf-8 -*-

def createCounter():
    ci = 0
    
    def counter():
        nonlocal ci
        ci = ci + 1
        
        def f(i):
            return i
        
        return f(ci)
    
    # fs = []
    # for i in range(1, 4):
    #     counter(i)
    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


def is_odd(n):
    return n % 2 == 1


# L = list(filter(is_odd, range(1, 20)))
L = list(filter(lambda n: n % 2 == 1, range(1, 20)))

print(L)


# decorator


def log(func):
    def wrapper(*args, **kw):
        print('call %s' % func.__name__)  # 先打印日志
        return func(*args, **kw)  # 再紧接着调用原始函数
    
    return wrapper


# 要借助Python的@语法，把decorator置于函数的定义处
# @log放到now()函数的定义处，相当于执行了语句：now = log(now)
@log
def now():
    print('2015-3-25')


now()

import functools


def log(text):
    def decorator(func):
        # 需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
        # 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s 33%s():' % (text, func.__name__))
            return func(*args, **kw)
        
        # print('%s22 %s():' % (text, func.__name__))
        return wrapper
    
    # print('%s11 %s():' % (text,'11'))
    return decorator


@log('excute')
def now():
    print('2015-3-25')


print('a')
now()

# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
# -*- coding: utf-8 -*-
import time, functools


def logger(text='excute'):
    @functools.wraps(text)
    def metric(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            print('begin call %s:' % (fn.__name__))
            t = time.time()
            result = fn(*args, **kwargs)
            t = time.time() - t
            print('%s %s in %s ms' % (fn.__name__, text, t * 1000))
            print('end call %s.' % (fn.__name__))
            return result
        
        return wrapper
    
    return metric


# 测试
# @metric
@logger('run')
def fast(x, y):
    time.sleep(0.0012)
    return x + y


# @metric
# @logger
@logger('run')
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


# 偏函数
def int2(x, base=2):
    return int(x, base)


int2('1010101')

# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2
# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
int2 = functools.partial(int, base=2)

# 仅仅是把base参数重新设定默认值为2，但也可以在函数调用时传入其他值：
int2('1000000', base=10)


# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
# -*- coding: utf-8 -*-


class Screen(object):
    __slots__ = ('_width', '_height')  # 用tuple定义允许绑定的属性名称

    def __str__(self):  # 返回用戶看到的字符串
        return 'Screen'

    __repr__ = __str__  # 返回開發者看到的字符串

    def __getattr__(self, item):
        raise AttributeError('%s has no attribute %s' % (self.__dict__, item))
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, w):
        self._width = w
    
    # 可读写属性
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, h):
        self._height = h
    
    @property  # 只读属性
    def resolution(self):
        return self._height * self._width
    
    pass


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')


class Animal(object):
    pass


# 大类:
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


# 各种动物:

class Ostrich(Bird):
    pass


# 现在，我们要给动物再加上Runnable和Flyable的功能，只需要先定义好Runnable和Flyable的类：


class Runnable(object):
    def run(self):
        print('Running...')


# 对于需要Runnable功能的动物，就多继承一个Runnable，例如Dog：


class Dog(Mammal, Runnable):
    pass


# 判斷對象是否可以調用
callable(Dog())


# 如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。
# 利用完全动态的__getattr__，我们可以写出一个链式调用：
class Chain(object):
    
    def __init__(self, path=''):
        self._path = path
    
    def __getattr__(self, path):
        return Chain('%s//%s' % (self._path, path))  # 1-%s/[]  self._path,
    
    def __str__(self):
        return self._path
    
    __repr__ = __str__


# 測試
print(Chain().status.user.timeline.list)


# '/status/user/timeline/list'

# Git
class ChainGit(object):
    
    def __init__(self, name='/user'):
        self._name = name
    
    def __getattr__(self, name):
        if name == 'user':
            return ChainGit(self._name)
        return ChainGit('%s/%s' % (self._name, name))  # 1-%s/[]  self._name,
    
    def __call__(self, *args, **kwargs):
        return ChainGit('%s/%s' % (self._name, args[0]))
        # print('My name is %s:%s.' % (self._name, args[-1]))
    
    def __str__(self):
        return self._name
    
    __repr__ = __str__


# 測試
print(ChainGit().user('micheal').repos)  #
# GET /user/micheal/repos
