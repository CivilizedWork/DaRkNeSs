##条件和递归
##多数语法与C语言一致
##practice调用制指定的函数n次
def do_n(f,n):
    if n<=0:
        print('end!')
    else:
        f()
        do_n(f,n-1)
def printf():
    print('good job')

##无限递归
# def recurse():
#     recurse()

##键盘的输入
name  = input ('What\'s your name ?\n')

##调试
##会出现空格错误
# x = 5
#  y = 6 ##前有一缩进空格

##数学错误
# import math
# signal_power = 9
# noise_power = 10
# ratio = signal_power // noise_power ##使用了地板除，值为零，可是真数不能为零，无意义，产生错误，所以应该改为/
# decibels = 10*math.log10(ratio)
# print(decibels)

##practice 5.1
import time
def time_transfer():
    t = time.time()
    day = int(t/24/3600)
    hour = int(t/3600)
    minutes = int(t/60)
    print(day,hour,minutes,t)
##practice 5.2
def check_fermat(a,b,c,n):
    if (n>2 and int(a)**n + int(b)**n == int(c)**n):
        print('Holy smokes, Fermat was wrong')
    else:
        print('No, that doesn’t work.')

##practrice 5.3
def is_triangle(a,b,c):
    if  a>0 and b>0 and c>0:
        if a+b>c and a+c>b and b+c>a:
            print('Yes')
        else:
            print('No')
    else:
        print('Fault')

##practice5.4
def recurse(n, s):
    print(n,s)
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

##practice 5.5
import turtle
# def draw(t, length, n, n1):
#     if n1==1:
#         bob = t()
#         n1=n1-1
#     if n == 0:
#         return
#     angle = 50
#     bob.fd(length*n)
#     bob.lt(angle)
#     draw(t, length, n-1,n1)
#     bob.rt(2*angle)
#     draw(t, length, n-1,n1)
#     bob.lt(angle)
#     bob.bk(length*n)
def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    turtle.Turtle.fd(t, length*n)
    turtle.Turtle.lt(t, angle)
    draw(t, length, n-1)
    turtle.Turtle.rt(t, 2*angle)
    draw(t, length, n-1)
    turtle.Turtle.lt(t, angle)
    turtle.Turtle.bk(t, length*n)
##像一朵雪花

##practice 5.6
def kele():
    bob = turtle.Turtle()
    bob.fd(100)
    bob.lt(60)
    bob.fd(100)
    bob.rt(120)
    bob.fd(100)
    bob.lt(60)
    bob.fd(100)
    turtle.mainloop()
##答案
def koch(t, n):
    """Draws a koch curve with length n."""
    if n<3:
        turtle.Turtle.fd(t, n)
        return
    m = n/3.0
    koch(t, m)
    turtle.Turtle.lt(t, 60)
    koch(t, m)
    turtle.Turtle.rt(t, 120)
    koch(t, m)
    turtle.Turtle.lt(t, 60)
    koch(t, m)


def snowflake(t, n):
    """Draws a snowflake (a triangle with a Koch curve for each side)."""
    for i in range(3):
        koch(t, n)
        turtle.Turtle.rt(t, 120)


world = turtle.World()
bob = turtle.Turtle()
bob.delay = 0
bob.x = -150
bob.y = 90
bob.redraw()

snowflake(bob, 300)

world.mainloop()