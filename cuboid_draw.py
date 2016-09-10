__author__ = 'tobias'
import turtle as t

def draw(corner_points3):
    window = t.Screen()
    t.ht()
    t.speed(2)
    for corner_point1 in corner_points3[1:4]:
        t.goto(corner_point1[0:2])
    t.goto(corner_points3[0][0:2])
    for corner_point2 in corner_points3[4:8]:
        t.goto(corner_point2[0:2])
    t.goto(corner_points3[4][0:2])
    t.pu()
    t.goto(corner_points3[1][0:2])
    t.pd()
    t.goto(corner_points3[5][0:2])
    t.pu()
    t.goto(corner_points3[2][0:2])
    t.pd()
    t.goto(corner_points3[6][0:2])
    t.pu()
    t.goto(corner_points3[3][0:2])
    t.pd()
    t.goto(corner_points3[7][0:2])
    window.exitonclick()