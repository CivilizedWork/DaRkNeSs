##列表
# [10,20,30,40]
# ['crunchy frog','ram bladder','lark vomit']
# ['spam',2.0,5,[10,20]]
cheeses = ['cheddar', 'Edam', 'Gouda']
numbers = [42, 123]
empty = []
print(cheeses, numbers, empty)

##列表式可变的
cheeses[0]
numbers[1] = 5
'Edam' in cheeses
'Brie' in cheeses

##遍历列表
for cheese in cheeses:
    print(cheese)
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
for x in []:  ##不执行循环主体
    print('That is so good')

##列表操作
a = [1, 2, 3]  ##列表的拼接
b = [4, 5, 6]
c = a + b
# [0]*4
# [1,2,3]*4

##列表切片
t = ['a', 'b', 'c', 'd', 'f']
# t[1:3]
# t[:4]
# t[3:]
# t[:]
t[1:3] = ['x', 'y']

##列表方法
t = ['a', 'b', 'c']
t.append('d')
t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
t = ['d', 'c', 'e', 'b', 'a']
t.sort()


##映射、筛选和归并
def add_all(t):
    total = 0
    for x in t:
        total += x
    return total


def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res


##删除元素
t = ['a', 'b', 'c']
x = t.pop()  ##移除并返回最后一个元素
t = ['a', 'b', 'c']
del t[1]
t.remove('c')
t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[2:6]  ##把2~6中间的元素删除

##列表和字符串
s = 'spam'
t = list(s)
s = 'pining for the fjords'
t = s.split()
s = 'spam-spam-spam'
delimiter = '-'
t = s.split(delimiter)
t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
s = delimiter.join(t)

##对象和值
a = 'banana'
b = 'banana'
##指向同一个对象(字符串)
a is b
a = [1, 2, 3]
b = [1, 2, 3]
a is b
##相等(元素相等)不等于相同（对象（列表）相同）
##别名
a = [1, 2, 3]
b = a
b is a


##列表参数
def delete_head(t):
    del t[0]


def bad_delete_head(t):
    t = t[1:]  ##错的


t1 = [1, 2, 3]
t3 = t1 + [4]


def tail(t):
    return t[1:]


letters = ['a', 'b', 'c']
rest = tail(letters)


##practice10.1
def nested_sum(t):
    sum1 = 0
    for i in t:
        sum1 += sum(i)
    return sum1


##practice 10.2
def cumsum(t):
    n = len(t)
    t1 = []
    for i in range(n):
        if i < n - 1:
            t1.append(sum(t[:i + 1]))
            # print(t1)
        else:
            t1.append(sum(t[:]))
            # print(t1)
    return t1


##practice 10.3
def middle(t):
    return t[1:len(t) - 1]


##practice10.4
def chop(t):
    del t[0]
    del t[len(t) - 1]
    return None


##practice 10.5
def is_sort(t):
    t1 = sorted(t)
    print(t1)
    print(t)
    if t1 == t:
        return True
    else:
        return False


##practice 10.6
def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)


##practice 10.7
def has_duplicates(t):
    previous = t[1]
    res = []
    for i in range(len(t)):
        n1 = 0
        n2 = 1 + i
        if i <= len(t) - 2:
            while n2 <= len(t) - 1:
                if t[i] == t[n2]:
                    n1 += 1
                    n2 += 1
            res.append(n1)
            print(res)
    if sum(res) >= 2:
        return True
    else:
        return False


#############参考答案##############
####practice10.8
def has_duplicates(t):
    """Returns True if any element appears more than once in a sequence.

    t: list

    returns: bool
    """
    # make a copy of t to avoid modifying the parameter
    s = t[:]
    s.sort()

    # check for adjacent elements that are equal
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return True
    return False


def random_bdays(n):
    """Returns a list of integers between 1 and 365, with length n.

    n: int

    returns: list of int
    """
    t = []
    for i in range(n):
        bday = random.randint(1, 365)
        t.append(bday)
    return t


def count_matches(num_students, num_simulations):
    """Generates a sample of birthdays and counts duplicates.

    num_students: how many students in the group
    num_samples: how many groups to simulate

    returns: int
    """
    count = 0
    for i in range(num_simulations):
        t = random_bdays(num_students)
        if has_duplicates(t):
            count += 1
    return count


def main():
    """Runs the birthday simulation and prints the number of matches."""
    num_students = 23
    num_simulations = 1000
    count = count_matches(num_students, num_simulations)

    print('After %d simulations' % num_simulations)
    print('with %d students' % num_students)
    print('there were %d simulations with at least one match' % count)


##practice10.9
import time


def make_word_list1():
    """Reads lines from a file and builds a list using append."""
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t.append(word)
    return t


def make_word_list2():
    """Reads lines from a file and builds a list using list +."""
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t = t + [word]
    return t


start_time = time.time()
t = make_word_list1()
elapsed_time = time.time() - start_time

print(len(t))
print(t[:10])
print(elapsed_time, 'seconds')

start_time = time.time()
t = make_word_list2()
elapsed_time = time.time() - start_time

print(len(t))
print(t[:10])
print(elapsed_time, 'seconds')


##practice10.10
def make_word_list():
    import bisect
    """Reads lines from a file and builds a list using append.

    returns: list of strings
    """
    word_list = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list


def in_bisect(word_list, word):
    """Checks whether a word is in a list using bisection search.

    Precondition: the words in the list are sorted

    word_list: list of strings
    word: string

    returns: True if the word is in the list; False otherwise
    """
    if len(word_list) == 0:
        return False

    i = len(word_list) // 2
    if word_list[i] == word:
        return True

    if word_list[i] > word:
        # search the first half
        return in_bisect(word_list[:i], word)
    else:
        # search the second half
        return in_bisect(word_list[i + 1:], word)


def in_bisect_cheat(word_list, word):
    """Checks whether a word is in a list using bisection search.

    Precondition: the words in the list are sorted

    word_list: list of strings
    word: string
    """
    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False

    return word_list[i] == word


if __name__ == '__main__':
    word_list = make_word_list()

    for word in ['aa', 'alien', 'allen', 'zymurgy']:
        print(word, 'in list', in_bisect(word_list, word))

    for word in ['aa', 'alien', 'allen', 'zymurgy']:
        print(word, 'in list', in_bisect_cheat(word_list, word))


##pracrice10.11

def reverse_pair(word_list, word):
    """Checks whether a reversed word appears in word_list.

    word_list: list of strings
    word: string
    """
    rev_word = word[::-1]
    return in_bisect(word_list, rev_word)


if __name__ == '__main__':
    word_list = make_word_list()

    for word in word_list:
        if reverse_pair(word_list, word):
            print(word, word[::-1])


##practice10.12
def interlock(word_list, word):
    """Checks whether a word contains two interleaved words.

    word_list: list of strings
    word: string
    """
    evens = word[::2]
    odds = word[1::2]
    return in_bisect(word_list, evens) and in_bisect(word_list, odds)


def interlock_general(word_list, word, n=3):
    """Checks whether a word contains n interleaved words.

    word_list: list of strings
    word: string
    n: number of interleaved words
    """
    for i in range(n):
        inter = word[i::n]
        if not in_bisect(word_list, inter):
            return False
    return True


if __name__ == '__main__':
    word_list = make_word_list()

    for word in word_list:
        if interlock(word_list, word):
            print(word, word[::2], word[1::2])

    for word in word_list:
        if interlock_general(word_list, word, 3):
            print(word, word[0::3], word[1::3], word[2::3])
