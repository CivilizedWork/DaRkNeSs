##字符串

##小练习
def printf(s):
    index = 0
    while index > -1*len(s):
        letter = s[index-1]
        print(letter)
        index = index - 1

################################

##小练习
prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter == 'O' or letter == 'Q':
       print(letter + 'u' + suffix)
    else:
       print(letter + suffix)

######################################
fruit = 'banana'
fruit[:]##打出所有字母
##字符串不可变
greeting = 'Hello， world!'
new_greeting = 'J' + greeting[1:]

##搜索
def find(word,letter):##搜索字母在某单词中的位置(索引)
    index = 0
    count = 0
    while index < len(word):
        if word[index] == letter:
            a = index
            count += 1
        index = index + 1
    return count

##循环和计数
#3计算字母a在字符串中出现的次数
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

def count(word,letter):
    print(find(word, letter))

##字符串方法、
word = 'banana'
new_word = word.upper()##小写变大写

##in运算符
def in_both(word1,word2):
    for letter in word1:
        if letter in word2:
            print(letter)

if word < 'banana':
    print('Your word， ' + word + '， comes before banana.')
elif word > 'banana':
    print('Your word， ' + word + '， comes after banana.')
else:
    print('All right， bananas.')

## practice 8.2
def count(word,letter):
    count = 0
    for letter1 in word:
        if letter1 == letter:
            count = count + 1
    print(count)

##practice 8.3
##编写一个叫 is_palindrome 的函数，接受一个字符串作为实参。
# 如果是回文词，就返回 True ，反之则返回 False。
# 记住，你可以使用内建函数 len 来检查字符串的长度。
def is_palindrome(word):
    n = 0
    n1 = -1
    n2 = 0
    while n <= int(len(word)/2):
        if word[n] == word[n1]:
            n += 1
            n1 -= 1
        else:
            n += 1
            n1 -= 1
            n2 += 1
    if n2 == 0:
        return True
    else:
        return False

##practice 8.5
def rotate_word(word,num,a):
    n = 0
    letter1 ='答案：\n'
    for letter in word:
        if a == 1:
            letter1 += chr(ord(letter)+num)
        else:
            letter1 += chr(ord(letter) - num)
    print(letter1)
