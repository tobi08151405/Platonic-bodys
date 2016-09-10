__author__ = 'tobias'
import math as m
import turtle as t
import rotation_matrix_3D as rm3D

def pyramid():
    print("\n\n****************************************************************************\n\n")
#requesting the variables
    edge_a = float(input("edge a [mm] : "))
    edge_b = float(input("edge b [mm] : "))
    height = float(input("height h [mm] : "))
    Volume = float(input("volume [mm^3] : "))
    alpha_grad = float(input("angle alpha [°] : "))
    beta_grad = float(input("angle beta [°] : "))
    gamma_grad = float(input("angle gamma [°] : "))
    print("\n\n****************************************************************************\n\n")
#calculation
    if Volume == 0:
        W = (edge_a*edge_b*height)/6
        print("Ergebnis: volume = %.5f" % W, "[mm^3]")
        print("\n\n****************************************************************************\n\n")
    elif edge_a == 0:
        d = (3*Volume)/edge_b/height
        print("Ergebnis: edge a = %.20f" % d, "[mm]")
        print("\n\n****************************************************************************\n\n")
        edge_a = d
    elif edge_b == 0:
        e = (3*Volume)/edge_a/height
        print("Ergebnis: edge b = %.20f" % e, "[mm]")
        print("\n\n****************************************************************************\n\n")
        edge_b = e
    elif height == 0:
        f = (3*Volume)/edge_a/edge_b
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
    Bp = [edge_b, 0, 0]
    Cp = [edge_b, 0, -edge_a]
    Dp = [0, 0, -edge_a]
    Ep = [edge_b/2, height, -edge_a/2]
    corner_points = [Ap, Bp, Cp, Dp, Ep]
#rotate the points
    corner_points3 = rm3D.rotation_matrix_3D(alpha, beta, gamma, corner_points)
#draw the pyramid
    window = t.Screen()
    t.ht()
    t.speed(2)
    for pointk1 in corner_points3[1:4]:
        t.goto(pointk1[0:2])
    t.goto(corner_points3[0][0:2])
    t.goto(corner_points3[4][0:2])
    t.pu()
    t.goto(corner_points3[1][0:2])
    t.pd()
    t.goto(corner_points3[4][0:2])
    t.pu()
    t.goto(corner_points3[2][0:2])
    t.pd()
    t.goto(corner_points3[4][0:2])
    t.pu()
    t.goto(corner_points3[3][0:2])
    t.pd()
    t.goto(corner_points3[4][0:2])
    window.exitonclick()