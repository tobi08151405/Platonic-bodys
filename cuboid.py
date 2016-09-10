__author__ = 'tobias'
import math as m
import cuboid_draw as cd
import rotation_matrix_3D as rm3D

def cuboid():
    print("\n\n****************************************************************************\n\n")
#requesting the variables
    edge_a = float(input("edge a [mm] : "))
    edge_b = float(input("edge b [mm] : "))
    edge_c = float(input("edge c [mm] : "))
    Volume = float(input("volume [mm^3] : "))
    alpha_grad = float(input("angle alpha [°] : "))
    beta_grad = float(input("angle beta [°] : "))
    gamma_grad = float(input("angle gamma [°] : "))
    print("\n\n****************************************************************************\n\n")
#calculation
    if Volume == 0:
        W = edge_a*edge_b*edge_c
        print("Ergebnis: volume = %.5f" % W, "[mm^3]")
        print("\n\n****************************************************************************\n\n")
    elif edge_a == 0:
        d = Volume/edge_b/edge_c
        print("Ergebnis: edge a = %.20f" % d, "[mm]")
        print("\n\n****************************************************************************\n\n")
        edge_a = d
    elif edge_b == 0:
        e = Volume/edge_a/edge_c
        print("Ergebnis: edge b = %.20f" % e, "[mm]")
        print("\n\n****************************************************************************\n\n")
        edge_b = e
    elif edge_c == 0:
        f = Volume/edge_a/edge_b
        print("Ergebnis: edge c = %.20f" % f, "[mm]")
        print("\n\n****************************************************************************\n\n")
        edge_c = f
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
    Ep = [0, edge_c, 0]
    Fp = [edge_b, edge_c, 0]
    Gp = [edge_b, edge_c, -edge_a]
    Hp = [0, edge_c, -edge_a]
    corner_pionts = [Ap, Bp, Cp, Dp, Ep, Fp, Gp, Hp]
#rotate the points
    corner_pionts3 = rm3D.rotation_matrix_3D(alpha, beta, gamma, corner_pionts)
#draw the cuboid
    cd.draw(corner_pionts3)