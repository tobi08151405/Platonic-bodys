__author__ = 'tobias'
import math as m
import turtle as t
import rotation_matrix_3D as rm3D

def pentagon():
    print("\n\n****************************************************************************\n\n")
#requesting the variables
    radius = float(input("prisms radius [mm] : "))
    height = float(input("height h [mm] : "))
    Volume = float(input("volume [mm^3] : "))
    alpha_grad = float(input("angle alpha [°] : "))
    beta_grad = float(input("angle beta [°] : "))
    gamma_grad = float(input("angle gamma [°] : "))
    print("\n\n****************************************************************************\n\n")
#calculation
    if Volume == 0:
        W = ((((m.sin((m.pi * 2) / 5) * radius) ** 2 + (radius - (m.cos((m.pi * 2) / 5) * radius)) ** 2) ** 0.5) / 2 * ((radius ** 2 - ((((m.sin((m.pi * 2) / 5) * radius) ** 2 + (radius - (m.cos((m.pi * 2) / 5) * radius)) ** 2) ** 0.5) / 2) ** 2) ** 0.5) * 5) * height
        print("Ergebnis: volume = %.5f" % W, "[mm^3]")
        print("\n\n****************************************************************************\n\n")
    elif height == 0:
        a = Volume / ((((m.sin((m.pi * 2) / 5) * radius) ** 2 + (radius - (m.cos((m.pi * 2) / 5) * radius)) ** 2) ** 0.5) / 2 * ((radius ** 2 - ((((m.sin((m.pi * 2) / 5) * radius) ** 2 + (radius - (m.cos((m.pi * 2) / 5) * radius)) ** 2) ** 0.5) / 2) ** 2) ** 0.5) * 5)
        print("Ergebnis: height h = %.%f" % a, "[mm]")
        height = a
#transform from degree to radiant
    alpha = m.radians(alpha_grad)
    beta = m.radians(beta_grad)
    gamma = m.radians(gamma_grad)
#define the points
    Ap, Bp, Cp, Dp, Ep, Fp, Gp, Hp, Ip, Jp = [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]
    points_calculat = [Ap, Bp, Cp, Dp, Ep, Fp, Gp, Hp, Ip, Jp]
    corner_pionts = []
    k = 0
    for point in points_calculat:
        if k > 4:
            z = height
        else:
            z = 0
        corner_pionts.append([(radius * m.sin(m.pi * 2 / 5 * k)), (radius * m.cos(m.pi * 2 / 5 * k)), z])
        k = k + 1
#rotate the points
    corner_pionts3 = rm3D.rotation_matrix_3D(alpha, beta, gamma, corner_pionts)
#draw the prism
    window = t.Screen()
    t.ht()
    t.speed(2)
    t.up()
    t.goto(corner_pionts3[0][0:2])
    t.pd()
    for pointk1 in corner_pionts3[1:5]:
        t.goto(pointk1[0:2])
    t.goto(corner_pionts3[0][0:2])
    for pointk2 in corner_pionts3[5:10]:
        t.goto(pointk2[0:2])
    t.goto(corner_pionts3[5][0:2])
    t.pu()
    t.goto(corner_pionts3[1][0:2])
    t.pd()
    t.goto(corner_pionts3[6][0:2])
    t.pu()
    t.goto(corner_pionts3[2][0:2])
    t.pd()
    t.goto(corner_pionts3[7][0:2])
    t.pu()
    t.goto(corner_pionts3[3][0:2])
    t.pd()
    t.goto(corner_pionts3[8][0:2])
    t.pu()
    t.goto(corner_pionts3[4][0:2])
    t.pd()
    t.goto(corner_pionts3[9][0:2])
    window.exitonclick()