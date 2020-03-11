##有返回值的函数
##例子1
import math
def area(radius):
    a = math.pi *radius**2
    return a
##等价
##der area(radius):
##      return math.pi * radius**2
def absolute_value(x):
    if x <= 0:
        return -x
    else:
        return x
##只有一个return语句会被执行
##出现在return之后的语句不再被执行

##小练习

def contrast(x,y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

##增量式开发
def distance(x1,y1,x2,y2):
    dx = x1 - x2
    dy = y1 - y2
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

def hypotenuse(a,b):
    a1 = a**2
    b1 = b**2
    dsquared = a1 + b1
    result = math.sqrt(dsquared)
    return result

##组合
# radius = distance(xc,yc,xp,yp)
# result = area(radius)
def circle_area(xc,yc,xp,yp):
    radius = distance(xc,yc,xp,yp)
    result = area(radius)
    return result
##合并
def circle_area(xc,yc,xp,yp):
    return area(distance(xc,yc,xp,yp))

##bool函数
def is_divisible(x,y):
    if x % y == 0:
        return True
    else:
        return False
##简化
def is_divisible(x,y):
    return x % y == 0

##条件语句
if is_divisible(1,1) == True:
    print('x is divisible by y')

##小练习
def is_between(x,y,z):
    if x <= y <= z:
        return True
    else:
        return False

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n*recurse
        return result

##斐波那契数列
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

##检测是否有小数或者有负数
def factorial(n):
    if not isinstance(n,int):
        print('Factorial is only defined for integers.')
        return None
    elif n < 0:
        print('Factorial is not defined for negative integers.')
        return None
    elif n == 0:
        return 1
    else:
        return n*factorial(n-1)

def factorial(n):
    space = ' ' * (4 * n)
    print(space, 'factorial', n)
    if n == 0:
        print(space, 'returning 1')
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        print(space, 'returning', result)
        return result

##practice 6.1
def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

x = 1
y = x + 1
print(c(x, y+3, x+y))
##已画堆栈图

##practice 6.2
def ack(m,n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m-1,1)
    elif m > 0 and n > 0:
        return ack(m-1,ack(m,n-1))

##practice 6.3
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

##回文函数
def is_palindorme(string):

    if len(string) == 1:
        return True
    elif len(string) == 0:
        return True
    elif len(string) == 2:
        if string[1] == string[-1]:
            return True
    elif len(string) > 2:
        if first(string) == last(string):
            return True
        else:
            return False
        return is_palindorme(middle(string))

##practice 6.4
def is_power(a,b):
    if a % b == 0 and a != 0 and a / b !=1:
        return is_power(a/b,b)
    if a / b == 1:
        return True

##practice 6.5

def max(a,b,n1):
    global b1
    if n1 == 1:
        b1=b
    if a % b == 0 and b1 % b == 0 and b > 1:
        return b
    elif b <= 1:
        return False
    else:
        return max(a,b-1,2)