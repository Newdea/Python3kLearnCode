#!/usr/bin/env python3          # 标准注释
# -*- coding:utf-8 -*-          # 表示.py文件本身使用标准UTF-8编码

"""a test hello module"""  # 表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释

__author__ = 'Newdea'  # 变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名


class Student(object):
    count = 0  # 类属性，实例数量
    
    def __init__(self, name, gender='female', score=60):
        self.__name = name  # 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，
        self.__score = score  # 就变成了一个私有变量（private），只有内部可以访问，外部不能访问
        self.__gender = gender
        Student.count += 1
        pass
    
    def get_gender(self):
        return self.__gender
    
    def set_gender(self, gender):
        if gender.lower() == 'male' or 'female':
            self.__gender = gender.lower()
            return self.get_gender()
        else:
            return ValueError('unknow gender')
    
    def get_name(self):
        return self.__name
    
    def get_score(self):
        return self.__score
    
    def print_score(self):
        print('std-%s\'s score :%s...' % (self.__name, self.__score))
        pass
    
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
    
    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'


# 类属性测试

# 测试:
print('类属性测试:')
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')

# get_grade() test
lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.get_name(), lisa.get_grade())
print(bart, bart.get_grade())

# 测试:
print('get_gender() 测试:')
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')


# 把Student的gender属性改造为枚举类型，可以避免使用字符串：

# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')


class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)
#
#  type()函数既可以返回一个对象的类型，又可以创建出新的类型
#
def fn(self, name='world'): # 先定义函数
     print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class

h = Hello()
h.hello()

print(type(Hello))
print(type(h))

# 定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：

# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

# 有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass：
# ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。
# 要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。
class MyList(list, metaclass=ListMetaclass):
    pass

L = MyList()
L.add(1)
L



