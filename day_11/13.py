##案例研究：数据结构选择

##practice 13.1
import string

fin = open('word.txt')


def output():
    word1 = []
    for words in fin:
        words = words.upper()
        word1.append(words.strip(', \n'))
    delimiter = ' '
    print(delimiter.join(word1))


##随机数
import random  ##提供生成伪随机数的函数

for i in range(10):
    x = random.random()
    print(x)
random.randint(5, 10)  ##返回一个在5~10之间的一个整数

t = [1, 2, 3]
random.choice(t)  ##在t序列中随机挑选一个元素


##random模块提供的函数，
##还可以生成符合高斯、指数、伽马等连续分布的随机值。

def histogram(s):
    d = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
         'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    for c in s:
        d[c] = d.get(c, 1) + 1
    return d


d = histogram('dfwefewfewf')


def choose_from_hist(s):
    return (random.choice(s))


import string


def process_file(filename):
    hist = dict()
    fp = open(filename)
    for line in fp:
        process_line(line, hist)
    return hist


def process_line(line, hist):
    line = line.replace('-', ' ')

    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1


hist = process_file('emma.txt')


##最常用的单词
def most_common(hist):
    t = []
    for key, value in hist.items():
        t.append((value, key))

    t.sort(reverse=True)
    return t


t = most_common(hist)
print('The most common words are:')
for freq, word in t[:10]:
    print(word, freq, sep='\t')


##可选参数
def print_most_common(hist, num=10):  ##num默认值为10
    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[:num]:
        print(word, freq, sep='\t')


##字典差集
def subtract(d1, d2):
    res = dict()
    for key in d1:
        if key not in d2:
            res[key] = None
    return res


words = process_file('words.txt')
diff = subtract(hist, words)

print("Words in the book that aren't in the word list:")
for word in diff.keys():
    print(word, end=' ')
