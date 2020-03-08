#第三章函数

#数学函数
import math
x = math.log10(11);
int(x);
y = math.sin(math.pi/2);
z = math.sqrt(2)/2.0;
a = math.cos(45/360*2*math.pi);
x = math.exp(math.log(x+1))
## hours*60 = minutes 非法（左侧一定为变量名，右侧一定为表达式）

#新建函数
def 打印函数():    ##函数名第一个字不能用数字
    print('你好')  ##括号内单双引号都可以

def repeat():
    打印函数()
    printf()
    打印函数()
def printf():
    print('hello!')

#形参与实参

def print_twice(void):
    print(void);
    print(void);
def print_triple(void):
    print(void);
    print(void);
    # print(a);
    print(void);
print_triple('Spam '*4);
print_triple(math.cos(math.pi));

#变量和形参都是局部的
def cat_twice(part1,part2):
    cat = part1 + part2
    print_triple(cat)

line1 = 'hello'
line2 = ' world!'
cat_twice(line1,line2)

#堆栈图
#函数列表被称作回溯

#有返回值函数和无返回值函数
result = print_triple('bing')
#print(result) 返回值为None

## practice 3.1
def right_justify(s):
    print(' '*69,s)

def do_twice(f1,v):
    f1(v)
    f1(v)
def do_four(f1,v):
    do_twice(f1, v)
    do_twice(f1, v)
do_twice(print,'spam')
do_four(print,'spam')
def grid():
    print('+', '-'*4, '+', '-'*4, '+')
    # do_four(f1, v)
    print('|', ' '*4,'|', ' '*4, '|')
    print('|', ' ' * 4, '|', ' ' * 4, '|')
    print('|', ' ' * 4, '|', ' ' * 4, '|')
    print('|', ' ' * 4, '|', ' ' * 4, '|')
    print('+', '-'*4, '+', '-'*4, '+')
    # do_four(f1, v)
    print('|', ' ' * 4, '|', ' ' * 4, '|')
    print('|', ' ' * 4, '|', ' ' * 4, '|')
    print('|', ' ' * 4, '|', ' ' * 4, '|')
    print('|', ' ' * 4, '|', ' ' * 4, '|')
    print('+', '-' * 4, '+', '-' * 4, '+')

def grid_four():
    print('|', '——', '|', '——', '|', '——', '|', '——', '|')
    print('|', '——', '|', '——', '|', '——', '|', '——', '|')
    print('|', '——', '|', '——', '|', '——', '|', '——', '|')
    print('|', '——', '|', '——', '|', '——', '|', '——', '|')
    print('|', '——', '|', '——', '|', '——', '|', '——', '|')
