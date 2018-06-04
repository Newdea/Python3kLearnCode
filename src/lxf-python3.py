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
