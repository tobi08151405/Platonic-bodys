__author__ = 'tobias'
import math as m
import numpy as np

def rotation_matrix(axis, theta):
    """
    Return the rotation matrix associated with counterclockwise rotation about
    the given axis by theta radians.
    """
    axis = np.asarray(axis)
    theta = np.asarray(theta)
    axis = axis/m.sqrt(np.dot(axis, axis))
    a = m.cos(theta/2)
    b, c, d = -axis*m.sin(theta/2)
    aa, bb, cc, dd = a*a, b*b, c*c, d*d
    bc, ad, ac, ab, bd, cd = b*c, a*d, a*c, a*b, b*d, c*d
    return np.array([[aa+bb-cc-dd, 2*(bc+ad), 2*(bd-ac)],
                     [2*(bc-ad), aa+cc-bb-dd, 2*(cd+ab)],
                     [2*(bd+ac), 2*(cd-ab), aa+dd-bb-cc]])

def rotation_matrix_3D(alpha, beta, gamma, corner_points):
    corner_points1 = []
    corner_points2 = []
    corner_points3 = []
    axis = [1, 0, 0]
    theta = alpha
    for corner_point in corner_points:
        corner_points1.append(np.dot(rotation_matrix(axis,theta), corner_point))
    axis = [0, 1, 0]
    theta = beta
    for corner_point1 in corner_points1:
        corner_points2.append(np.dot(rotation_matrix(axis,theta), corner_point1))
    axis = [0, 0, 1]
    theta = gamma
    for corner_point2 in corner_points2:
        corner_points3.append(np.dot(rotation_matrix(axis,theta), corner_point2))
    return corner_points3