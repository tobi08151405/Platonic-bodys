__author__ = 'tobias'
import math as m
import cuboid_draw as cd
import rotation_matrix_3D as rm3D

def cube():
    print("\n\n****************************************************************************\n\n")
#requesting the variables
    edge_a = float(input("edge a [mm] : "))
    Volume = float(input("volume [mm^3] : "))
    alpha_grad = float(input("angle alpha [°] : "))
    beta_grad = float(input("angle beta [°] : "))
    gamma_grad = float(input("angle gamma [°] : "))
    print("\n\n****************************************************************************\n\n")
#calculation
    if Volume == 0:
        W = edge_a**3
        print("Ergebnis: volume = %.5f" % W, "[mm^3]")
        print("\n\n****************************************************************************\n\n")
    elif edge_a == 0:
        b = Volume**(1/3)
        print("Ergebnis: edge a = %.20f" % b, "[mm]")
        print("\n\n****************************************************************************\n\n")
        edge_a = b
    else:
        print(":-(")
        print("\n\n****************************************************************************\n\n")
#transform from degree to radiant
    alpha = m.radians(alpha_grad)
    beta = m.radians(beta_grad)
    gamma = m.radians(gamma_grad)
#define the points
    Ap = [0, 0, 0]
    Bp = [edge_a, 0, 0]
    Cp = [edge_a, 0, -edge_a]
    Dp = [0, 0, -edge_a]
    Ep = [0, edge_a, 0]
    Fp = [edge_a, edge_a, 0]
    Gp = [edge_a, edge_a, -edge_a]
    Hp = [0, edge_a, -edge_a]
    corner_points = [Ap, Bp, Cp, Dp, Ep, Fp, Gp, Hp]
#rotate the points
    corner_points3 = rm3D.rotation_matrix_3D(alpha, beta, gamma, corner_points)
#draw the cube
    cd.draw(corner_points3)