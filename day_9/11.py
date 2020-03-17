#########字典#########
enf2sp = dict()
enf2sp = {'one': 1, 'two': 2, 'three': 3}
vals = enf2sp.values()
1 in vals


############字典作为计数集合############
def histogram(s):
    d = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
         'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    for c in s:
        d[c] = d.get(c, 1) + 1
    return d


#####循环和字典
def print_hist(h):  ###无需打印
    for c in h:
        print(c, h[c])


def order_print_hist(h):  ###有序打印
    for key in sorted(h):
        print(key, h[key])


#########逆向查找###########
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError('value does not appear in the dictionary')  ## raise 语句 能触发异常，这里它触发了 ValueError，这是一个表示查找操作失败的内建异常。


##字典和列表
##倒转字典
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


##注意;列表可以作为字典中的值，但是不能是键
##键必须是可哈希的

##备忘录
known = {0: 0, 1: 1}


def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n - 1) + fibonacci(n - 2)
    known[n] = res
    return res


##全局变量
verbose = True


def example():
    if verbose:
        print('Running example')


been_called = False


def example2():
    global been_called
    been_called = True


known = {0: 0, 1: 1}


def example4():
    known[2] = 1


def example5():
    global known
    known = dict()


##pracrtice 11.1
d = dict()


def input1():
    global d
    fin = open('words.txt')
    d = dict()
    for word in fin:
        d[word] = 1
    return d
    # if word1 in d:
    #     return True


##practice 11.2
def invert_dict(d):
    inverse = {}
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse


if __name__ == '__main__':
    d = dict(a=1, b=2, c=3, z=1)
    inverse = invert_dict(d)
    for val in inverse:
        keys = inverse[val]
        print(val, keys)


##practice 11.3
def ackermann(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return ackermann(m - 1, 1)

    if (m, n) in cache:
        return cache[m, n]
    else:
        cache[m, n] = ackermann(m - 1, ackermann(m, n - 1))
        return cache[m, n]


print(ackermann(3, 4))
print(ackermann(3, 6))


##practice11.4
def has_duplicates(t):
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False


def has_duplicates2(t):
    return len(set(t)) < len(t)


if __name__ == '__main__':
    t = [1, 2, 3]
    print(has_duplicates(t))
    t.append(1)
    print(has_duplicates(t))

    t = [1, 2, 3]
    print(has_duplicates2(t))
    t.append(1)
    print(has_duplicates2(t))


##practice11.5
def make_word_dict():
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = None

    return d


def rotate_pairs(word, word_dict):
    for i in range(1, 14):
        rotated = rotate_word(word, i)
        if rotated in word_dict:
            print(word, i, rotated)


if __name__ == '__main__':
    word_dict = make_word_dict()

    for word in word_dict:
        rotate_pairs(word, word_dict)
