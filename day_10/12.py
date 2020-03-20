##############元组###########
t = 'a',
t = tuple()
t = tuple('apple')

##t[] 方括号运算符将索引一个元素与列表索引一致

##t[1:3]切片法与列表一样

##t[0] = 'g' 元组中的元素是不可变的

##可以用其他的元组中低端元素替代
t = ('A',) + t[1:]

##关系运算符适用于元组和其他序列
(0, 1, 2) < (1, 2, 3)
(0, 1, 2000000) < (0, 3, 4)
##Python 会首先比较序列中的第一个元素，
##如果他们相等，就继续比较下一组元素，
##直到比值不同，其后的元素也不会参与比较、

##元组赋值
# temp = a
# a = b
# b = temp##比较繁琐
##简化版
# a,b = b,a
addr = 'monty@python.org'  ##右侧可以为任意类型
uname, domain = addr.split('@')

##元组作为返回值
# divmod()##此函数接受两个实参，返回两个值的元组：商和余数
t = divmod(5, 2)
quot, rem = divmod(6, 4)


def min_max(t):
    return min(t), max(t)


##可变长度参数元组
def printall(*args):  ##此形参为汇集形参，可以接受可变数量的参数
    print(*args)


##与汇集相对的是分散
# t = (6,4)
# divmod(t)##不行的
divmod(*t)  ##可行，因为参数被分散了

##许多内建函数使用了可变长度参数元组。例如：max,min\
max(1, 2, 3)


##但是sum不行
def small(t):
    sum1 = 0
    for i in t:
        sum1 += i
    return sum1


##列表和元组
s = 'abc'
t = [0, 1, 2]
zip(s, t)
for pair in zip(s, t):
    print(pair)
list(zip(s, t))
list(zip('anne', 'elk'))  ##如果用于创建的序列长度不一，返回对象的长度
##以最短序列的长度为准
t = [('a', 0), ('b', 1), ('c', 2)]
for letter, number in t:
    print(number, letter)


def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False


for index, element in enumerate('abc'):  ##enumerate()返回一个枚举对象，
    ##每个对象包括了索引和对应元素
    print(index, element)

##字典和元组
# items()##返回多个元组组成的序列，其中每个元组是一个键值对
d = {'a': 0, 'b': 1, 'c': 2}
t = d.items()  ##由序列（字典）变成元组
dict_items = d.items()
for key, value in d.items():
    print(key, value)

t = [('a', 0), ('c', 2), ('b', 1)]  ##由元组变成字典
d = dict(t)

d = dict(zip('abc', range(3)))
directory = dict()
directory['w', 'p'] = 123456
for last, first in directory:
    print(first, last, directory['w', 'p'])
