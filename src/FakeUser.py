import random

#  练习-
fn = []  # 姓
ln1 = []  # 单名
ln2 = []  # 双各

path = 'D:\\o\\ttt.txt'
with open(path, 'r') as f:
    for line in f.readlines():
        fn.append(line.split('\n')[0])  # 只获取每行以'\n' 分割的第1个数据（其他数据还有单词，换行符等）
print(fn)

with open(path, 'r') as f:
    for line in f.readlines():
        if len(line.split('\n')[0]) <= 5:
            ln1.append(line.split('\n')[0])  # 只获取每行以'\n' 分割的第1个数据（其他数据还有单词，换行符等）
        else:
            ln2.append(line.split('\n')[0])

print(ln1)
print('=' * 50)
print(ln2)
# 要把打印出的数据复制到元组中，这样更节省内存也不必每次都重新读取

fn = ('赵', '钱', '孙')
ln1 = ('Ann', '玉')
ln2 = ('安宁', '宝贵')


class FakeUser:
    def __init__(self, amount=1):
        self.amount = amount
    
    def fake_name(self, one_word=False, two_words=False):
        n = 0
        while n < self.amount:
            if one_word:
                full_name = random.choice(fn) + random.choice(ln1)
            elif two_words:
                full_name = random.choice(fn) + random.choice(ln2)
            else:
                full_name = random.choice(fn) + random.choice(ln1 + ln2)
            yield full_name  # 生成器 generator
            n += 1
        
        # print(full_name)
    
    def fake_gender(self):
        n = 0
        while n < self.amount:
            gender = random.choice('Male', 'Famale', 'Unknow')
            yield gender
            n += 1
        
        # print(gender)


# 定义子类
class SnsUser(FakeUser):
    def get_follwers(self, few=True, a_lot=False):
        n = 0
        while n < self.amount:
            if few:
                followers = random.randrange(1, 50)
            elif a_lot:
                followers = random.randrange(400, 10000)
            yield followers
            n += 1
        # print(followers)


user_a = FakeUser()
user_b = SnsUser()
user_a.fake_name()
user_b.get_follwers()
