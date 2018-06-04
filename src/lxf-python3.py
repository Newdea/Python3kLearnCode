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

