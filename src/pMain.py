what_he_does = 'plays '
his_instrument = 'guitar '
his_name = 'Robert Johnson '
artist_intro = his_name + what_he_does + his_instrument

print(artist_intro)

num = 1
string = '1'
num2 = int(string)
print(num + num2)

# 字符串相乘
words = 'worrrrrd' * 3
print(words)

word = 'a looooooooooooooooooong word '
num = 12
string = 'Bang'
total = string * (len(word) - num)  # 等价于'Bang' * x
print(total)

# string slice 分片
name = 'My name is Mike'
print(name[0])
'M'
print(name[-4])
'M'
print(name[11:14])  # from 11th to 14th, 14th one is excluded
'Mik'
print(name[11:15])  # from 11th to 15th, 15th one is excluded
'Mike'
print(name[5:])
'me is Mike'
print(name[:5])
'My na'

# 找出朋友中的魔鬼
word = 'friends'
find_ths_evil_in_friends = word[0] + word[2:4] + word[-3:-1]
print(find_ths_evil_in_friends)

url = 'http://ww1.site.cn/14d2e8ejw1exjogbxdxhj20ci0kuwex.jpg'
file_name = url[-10:]
print(file_name)

# 方法
phone_num = '130-2778-1777'
hiding_num = phone_num.replace(phone_num[:9], '*' * 9)
print(hiding_num)

# 号码联想功能
search = '168'
num_a = '1386-168-0006'
num_b = '1681-222-0006'

print(search + ' is at ' + str(num_a.find(search) + 1) + ' to\
' + str(num_a.find(search) + len(search)) + ' of num_a')
print(search + ' is at ' + str(num_b.find(search) + 1) + ' to\
' + str(num_b.find(search) + len(search)) + ' of num_b')

# 格式化
print('{} a word she can get what she {} for.'.format('With', 'came'))
print('{preposition} a word she can get what she {verb} for'.format(preposition='With', verb='came'))
print('{0} a word she can get what she {1} for.'.format('With', 'came'))

city = input("write down the name of city:")
url = "http://apistore.baidu.com/microservice/weather?citypinyin={}".format(city)


# converte Celsius to Fahrenheit
# positional argeument
# keywoord argument

def fCtoF(C):
    return str(C * 9 / 5 + 32) + '°F'


# 默认参数可以不用在调用时设置，只需在定义时设置
def trapezoid_area(up=1, down=2, h=3):
    return 0.5 * (up + down) * h


trapezoid_area(h=3, down=2, up=1)  # RIGHT!
# trapezoid_area(h=3, down=2, 1) #  WRONG!
# trapezoid_area(up=1, down=2, 3) #  WRONG!
trapezoid_area(1, 2, h=3)  # RIGHT!
trapezoid_area(1, 2)  # RIGHT!


# open函数
# window:   \\


def text_create(name, msg):
    desktop_path = 'D:\\o\\'
    full_path = desktop_path + name + '.txt'
    file = open(full_path, 'w')
    file.write(msg)
    file.close()
    print('Done')


text_create('hello', 'hello worldhello Phython World')  # 调用


def text_filter(word, censored_word='lame', changed_word='Awesome'):
    return word.replace(censored_word, changed_word)


text_filter('Python is lame!')

#  运算符//取整除
#  浮点和整数可以比较
# 成员in
# 身份is

album = ['Black Star', 'David Bowie', 25, True]
album.append("hslesong")

'blask' in album

#  None 空值

password_list = ['*#*#', '12345']


def faccount_login():
    vpCounter = 3
    while vpCounter > 0:
        vpassWord = input('password:')
        bpswdCorrect = vpassWord == password_list[-1]
        bpswdReset = vpassWord == password_list[0]
        if bpswdReset:
            vNewpswd = input('Plesae input New password:')
            password_list.append(vNewpswd)
            print('Reset password success! Please save it carefully')
            faccount_login()
        elif bpswdCorrect:
            print('Login success!')
        else:
            print('Wrong assword or invalid input')
            vpCounter -= 1
    else:
        print('Your Account has been Locked!!!')


faccount_login()

for num in range(1, 11):
    print(str(num) + ' + 1 =', num + 1)

for i in range(1, 10):
    for j in range(i, 10):
        print('{}*{}={}'.format(i, j, i * j))

count = 0
while True:
    print('Repeat this line !')
    count += 1
    if count == 5:
        break

#  列表
fruit = ['pineapple', 'pear']
fruit.insert(1, 'grape')
fruit[1:3] = ['apple']  # 在相信相应位置插入
fruit.remove('orange')
del fruit[0:1]
print(fruit)
fruit.extend(['abc', 'fdg', 'akdf'])
# 排序
print(sorted(fruit, reverse=True))
# 同时使用两个列表
num_list = [6, 2, 7, 4, 1, 3, 5]
for a, b in zip(num_list, fruit):
    print(b, 'is', a)

# 列表解析式
b = [i for i in range(1, 500, 20)]

#  dictionary
a = {'key': '123', 'key': 456}
a.update({'FB': 'facebook', 'G': 'google'})
print(a)
del a['FB']

#  元组Tuple
#   不能增删改，可查
tu = ('a', '1', 'f')
tu[2]

# set
# 无序，不重复
a_set = {1, 2, 3, 4}
a_set.add(7)
a_set.remove(4)
a_set.discard(3)
print(a_set)

import string

path = 'D:\\o\\ttt.txt'
with open(path, 'r') as text:
    raw_words = text.read().split()
    words = [raw_word.strip(string.punctuation).lower() for raw_word in raw_words]
    words_index = set(words)
    count_dict = {index: words.count(index) for index in words_index}

for word in sorted(words_index, key=lambda x: count_dict[x], reverse=True):
    print('{}---{} times'.format(word, count_dict[word]))


# Class 类
class Cocacola:
    colories = 140
    formula = ['caffeine', 'suga', 'water', 'soda']
    
    def __init__(self, logo_name='可口可乐'):
        self.Local_logo = logo_name
        for element in self.formula:
            print('Coke has {}!'.format(element))
    
    def drink(self, how_much='a sip'):
        if how_much == 'a sip':
            print('Cool~')
        elif how_much == 'a bottle':
            print('Headache')
        else:
            print('Energy!')


coke = Cocacola()
print(coke.Local_logo)


# class inheritance 类的继承
class CaffeineFree(Cocacola):
    colories = 100  # override 重载
    formula = ['suga', 'water', 'soda']


coke_a = CaffeineFree('Cocacola-FREE')
coke_a.drink()

coke_a.colories = 200
print(coke_a.colories)
print(CaffeineFree.__dict__)
print(coke_a.__dict__)
print(type(coke_a))

# 扩展了解
from bs4 import Beautifulsoup

soup = Beautifulsoup
print((type(soup)))

from src import FakeUser

user_a = FakeUser()
user_b = SnsUser()
user_a.fake_name()
user_b.get_follwers()

import sys

print(sys.path[3])
