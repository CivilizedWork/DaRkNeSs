##迭代
##更新变量之前，得先初始化
x = 0
x = x + 1
##while语句
def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print('Blastoff!')

def squence(n):
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n / 2
        else:
            n = n*3 + 1

def print_n(s,n):
    while n > 0:
        n = n - 1
        print(s)

##break语句

##平方根# while True:##循环条件为真，所以会一直执行直到碰到break
#     line = input ('> ')
#     if line == 'done':
#         break
#     print(line)
#
# print('Done!')

a = 5
x = 3
while True:
    print(x)
    y = (x +a/x) / 2
    # if y == x:
    #     break
    if abs(y - x) < 0.0000001: ##epsilon是一个很小的数0.0000001
        break
    x = y

## practice7.1
import math
def mysqrt(a,x):
    while True:
        y = (x + a / x) / 2
        # if y == x:
        #     break
        if abs(y - x) < 0.0000001:  ##epsilon是一个很小的数0.0000001
            break
        x = y
    return y
def test_square_root(a):
    print('a',' '*2, 'mysqrt(a)', ' '*3, 'math.sqrt(a)', ' '*2, 'diff')
    print('-', ' ' * 3, '-'*7, ' ' * 4, '-'*7, ' ' * 2, '-'*7)
    while 1<=a<=9:
        a1 = mysqrt(a, 5)
        a2 = math.sqrt(a)
        a3 = abs(a1-a2)
        print(a, ' ' * 3, a1, ' ' * 4, a2, ' ' * 2, a3)
        a = a+1

##practice 7.2
def eval_loop():
    while True:
        a = input('输入数字字符\n')
        if a == 'done':
            print(b)
            break
        else:
            b = eval(a)
            print(b)

## practice 7.3
def factorial (n):
    if not isinstance(n, int):
        print('Factorial is only defined for integers.')
        return None
    elif n < 0:
        print('Factorial is not defined for negative integers.')
        return None
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def estimate_pi(k):
    p1 = 0
    p3 = float(1/math.pi)
    n = 2*2**0.5/9801
    while k <= 100:
        p1 = p1 + factorial(4*k)*(1103+26390*k)/((factorial(k))**4*396**(4*k))
        k = k +1
        if abs(n*p1 - p3) < 10*-15:
            break
        else:
            print(n*p1 - p3)
    print('Exactly')

