__author__ = 'tobias'
import cube_for as cf
import cuboid as c
import pyramid_three as pt
import pyramid_four as pf
import pentagon as p
import octagon as o

print("\n\n****************************************************************************\n\n")
print("\n****************************************************************************\n")
print("\n\nIf you don't know one measurement, please write down 0!\n")
print("The program needs two measurements to do the calculation!\n\n")
print("\n****************************************************************************\n")
while 1:
    frame_type = str(input("Bodytype a=cube, b=cuboid, c=triangular pyramid, d=quadrangular pyramid, e=pentagonal prism, f=octagonal prism, q=quit : "))
    if frame_type in ['q']:
        break
    elif frame_type in ['a']:
        cf.cube()
    elif frame_type in ['b']:
        c.cuboid()
    elif frame_type in ['c']:
        pt.pyramid()
    elif frame_type in ['d']:
        pf.pyramid()
    elif frame_type in ['e']:
        p.pentagon()
    elif frame_type in ['f']:
        o.octagon()
    else:
        print(":-(")