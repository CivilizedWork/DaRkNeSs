##案例研究: 接口设计
import turtle
import math
# # bob = turtle.Turtle()
# # print(bob)
# ##画正方形
# # bob.fd(100)
# # bob.lt(90)
# # bob.fd(100)
# # bob.lt(90)
# # bob.fd(100)
# # bob.lt(90)
# # bob.fd(100)
# # turtle.mainloop()
#
# ##简单的重复
# # for i in range(4):
# #     print('Hello!')
# # for i in range(4):
# #     bob.fd(100)
# #     bob.lt(90)
# ##practice
# # def square(t,length):
# #     bob = t()
# #     print(bob)
# #     for i in range(4):
# #         bob.fd(length)
# #         bob.lt(90)
# ###################################
# def polygon(t,length,n,angle):
#     bob = t()
#     print(bob)
#     for i in range(n):
#         bob.fd(length)
#         bob.lt(angle/n)
# #####################################
# def circle (t,r):
#     polygon(t,2*math.pi*r/100,100)
# ##答案
# # def circle(t, r):
# #     circumference = 2 * math.pi * r
# #     n = 50
# #     length = circumference / n
# #     polygon(t, n, length)
# # def circle(t, r):
# #     circumference = 2 * math.pi * r
# #     n = int(circumference / 3) + 1 ##？？？
# #     length = circumference / n
# #     polygon(t, n, length)
# ########################################
# def arc (t,r,angle):
#     polygon(t, 2 * math.pi * r * angle / 360/100, 100,angle)
# ##答案
# # def arc(t, r, angle):
# #     arc_length = 2 * math.pi * r * angle / 360
# #     n = int(arc_length / 3) + 1
# #     step_length = arc_length / n
# #     step_angle = angle / n
# #
# #     for i in range(n):
# #         t.fd(step_length)
# #         t.lt(step_angle)
# #调用时可以使用关键字形参如：polygon(bob, n=7, length=70)
# ##重构
# def polyline(t, n, length, angle):
#     for i in range(n):
#         t.fd(length)
#         t.lt(angle)
#
# def arc(t, r, angle):
#     arc_length = 2 * math.pi * r * angle / 360
#     n = int(arc_length / 3) + 1
#     step_length = arc_length / n
#     step_angle = float(angle) / n
#     polyline(t, n, step_length, step_angle)
# def circle(t, r):
#     arc(t, r, 360)
#
# #文档字符串
# def polyline(t, n, length, angle):
#     '''Draws n line segments with the given length and
#     angle (in degrees) between them.  t is a turtle.
#     '''
#     for i in range(n):
#         t.fd(length)
#         t.lt(angle)
#
# ##practice 4.1
# ##答案
# def arc(t, r, angle):
#     arc_length = 2 * math.pi * r * abs(angle) / 360
#     n = int(arc_length / 4) + 3
#     step_length = arc_length / n
#     step_angle = float(angle) / n
#
#     t.lt(step_angle/2)
#     polyline(t, n, step_length, step_angle)
#     t.rt(step_angle/2)
# ##4.2
# ###参见答案
# # def petal(t, r, angle):
# #     """Draws a petal using two arcs.
# #
# #     t: Turtle
# #     r: radius of the arcs
# #     angle: angle (degrees) that subtends the arcs
# #     """
# #     for i in range(2):
# #         arc(t, r, angle)
# #         t.lt(180-angle)
# #
# #
# # def flower(t, n, r, angle):
# #     """Draws a flower with n petals.
# #
# #     t: Turtle
# #     n: number of petals
# #     r: radius of the arcs
# #     angle: angle (degrees) that subtends the arcs
# #     """
# #     for i in range(n):
# #         petal(t, r, angle)
# #         t.lt(360.0/n)
# #
# #
# # def move(t, length):
# #     """Move Turtle (t) forward (length) units without leaving a trail.
# #     Leaves the pen down.
# #     """
# #     t.pu()
# #     t.fd(length)
# #     t.pd()
# #
# #
# # bob = turtle.Turtle()
# #
# # # draw a sequence of three flowers, as shown in the book.
# # move(bob, -100)
# # flower(bob, 7, 60.0, 60.0)
# #
# # move(bob, 100)
# # flower(bob, 10, 40.0, 80.0)
# #
# # move(bob, 100)
# # flower(bob, 20, 140.0, 20.0)
# #
# # bob.hideturtle()
# # turtle.mainloop()
##4.3
# def polygon(t,length,n,angle):
#     bob = t()
#     print(bob)
#     bob.lt(90+180/n)
#     bob.fd(length/2/math.cos(90-180/n))
#
#     for i in range(n-1):
#         bob.lt(180-360/n)
#         bob.fd(length/2/math.cos(90-180/n))
#         bob.bk(length/2/math.cos(90-180/n))
#     bob.lt(180-360 / n)
#     bob.fd(length / 2 / math.cos(90-180 / n))
#     bob.lt(90-180/n)
#     for i in range(n):
#         bob.fd(length)
#         bob.lt(angle/n)
#     ##def draw_pie(t, n, r):
#     """Draws a pie, then moves into position to the right.
#
#     t: Turtle
#     n: number of segments
#     r: length of the radial spokes
#     """
#     polypie(t, n, r)
#     t.pu()
#     t.fd(r*2 + 10)
#     t.pd()
#
#
# def polypie(t, n, r):
#     """Draws a pie divided into radial segments.
#
#     t: Turtle
#     n: number of segments
#     r: length of the radial spokes
#     """
#     angle = 360.0 / n
#     for i in range(n):
#         isosceles(t, r, angle/2)
#         t.lt(angle)
#
#
# def isosceles(t, r, angle):
#     """Draws an icosceles triangle.
#
#     The turtle starts and ends at the peak, facing the middle of the base.
#
#     t: Turtle
#     r: length of the equal legs
#     angle: half peak angle in degrees
#     """
#     y = r * math.sin(angle * math.pi / 180)
#
#     t.rt(angle)
#     t.fd(r)
#     t.lt(90+angle)
#     t.fd(2*y)
#     t.lt(90+angle)
#     t.fd(r)
#     t.lt(180-angle)
#
#
# bob = turtle.Turtle()
#
# bob.pu()
# bob.bk(130)
# bob.pd()
#
# # draw polypies with various number of sides
# size = 40
# draw_pie(bob, 5, size)
# draw_pie(bob, 6, size)
# draw_pie(bob, 7, size)
# draw_pie(bob, 8, size)
#
# bob.hideturtle()
# turtle.mainloop()
##4.4参考答案

##4.5参考答案
# def drawl(t, n, length, a=, b=):
#
#     theta = 0
#
#     for i in range(n):
#         t.fd(length)
#         dtheta = 1 / (a + b * theta)
#
#         t.lt(dtheta)
#         theta += dtheta
# bob = turtle.Turtle()
# draw(bob, 100)
# turtle.mainloop()