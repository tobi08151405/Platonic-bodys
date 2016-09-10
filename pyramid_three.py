__author__ = 'tobias'
import math as m
import turtle as t
import rotation_matrix_3D as rm3D

def pyramid():
    print("\n\n****************************************************************************\n\n")
#requesting the variables
    edge_c = float(input("edge c [mm] : "))
    height_c = float(input("bases height hc [mm] : "))
    height = float(input("height h [mm] : "))
    Volume = float(input("volume [mm^3] : "))
    alpha_grad = float(input("angle alpha [°] : "))
    beta_grad = float(input("angle beta [°] : "))
    gamma_grad = float(input("angle gamma [°] : "))
    print("\n\n****************************************************************************\n\n")
#calculation
    if Volume == 0:
        W = (edge_c*height_c*height)/6
        print("Ergebnis: volume = %.5f" % W, "[mm^3]")
        print("\n\n****************************************************************************\n\n")
    elif edge_c == 0:
        d = (6*Volume)/height_c/height
        print("Ergebnis: edge c = %.20f" % d, "[mm]")
        print("\n\n****************************************************************************\n\n")
        edge_c = d
    elif height_c == 0:
        e = (6*Volume)/edge_c/height
        print("Ergebnis: height hc = %.20f" % e, "[mm]")
        print("\n\n****************************************************************************\n\n")
        height_c = e
    elif height == 0:
        f = (6*Volume)/edge_c/height_c
        print("Ergebnis: height h = %.20f" % f, "[mm]")
        print("\n\n****************************************************************************\n\n")
        height = f
    else:
        print(":-(")
        print("\n\n****************************************************************************\n\n")
#transform from degree to radiant
    alpha = m.radians(alpha_grad)
    beta = m.radians(beta_grad)
    gamma = m.radians(gamma_grad)
#define the points
    Ap = [0, 0, 0]
    Bp = [edge_c, 0, 0]
    Cp = [edge_c/2, 0, -height_c]
    Dp = [edge_c/2, height, -(height_c/2)]
    corner_points = [Ap, Bp, Cp, Dp]
#rotate the points
    corner_points3 = rm3D.rotation_matrix_3D(alpha, beta, gamma, corner_points)
#draw the pyramid
    window = t.Screen()
    t.ht()
    t.speed(2)
    for corner_point1 in corner_points3[1:3]:
        t.goto(corner_point1[0:2])
    t.goto(corner_points3[0][0:2])
    t.goto(corner_points3[3][0:2])
    t.pu()
    t.goto(corner_points3[1][0:2])
    t.pd()
    t.goto(corner_points3[3][0:2])
    t.pu()
    t.goto(corner_points3[2][0:2])
    t.pd()
    t.goto(corner_points3[3][0:2])
    window.exitonclick()