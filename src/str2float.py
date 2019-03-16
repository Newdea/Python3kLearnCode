from functools import reduce

def str2float(s):
    DIGITS = {'.': '', '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    def char2num(s):
        return DIGITS[s]
    sdot = s.index('.')
    s = s[:sdot] + s[sdot + 1:]
    # for i, v in enumerate(s):
    #     if v == '.':
    #         s = s[:i] + s[i + 1:]
    #         break

    return reduce(lambda x, y: x * 10 + y, map(char2num, s))\
    / pow(10, (len(s) - sdot))  # - sdot
    pass


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')



