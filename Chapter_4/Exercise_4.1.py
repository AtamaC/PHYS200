from TurtleWorld import *
import math

def square(t, length):
    """Use the Turtle (t) to draw a square with sides of
    the given length.  Returns the Turtle to the starting
    position and location.
    """
    for i in range(4):
        fd(t, length)
        lt(t)

def polyline(t, n, length, angle):
    """Draw n line segments with the given length and
    angle (in degrees) between them.
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def polygon(t, n, length):
    """Draw a closed polygon with n sides with the given length"""
    angle = 360.0/n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    """Draw an arc segment of radius r over the angle given in
    degrees"""
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before the polyline reduces
    # the error caused by the linear approximation of the arc
    lt(t, step_angle/2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle/2)

def circle(t, r):
    """Draws a circle of radius r"""
    arc(t, r, 360)

# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':
    world = TurtleWorld()    

    bob = Turtle()
    bob.delay = 0.001

    # draw a circle centered on the origin
    radius = 100
    pu(bob)
    fd(bob, radius)
    lt(bob)
    pd(bob)
    circle(bob, radius)

    wait_for_user()

# stack diagram:
# __main__  : bob ----> Turtle
#           : radius ----> 100
#           : world ----> TurtleWorld
#
# circle    : t ----> Turtle
#           : r ----> 100
#
# arc       : t ----> Turtle
#           : r ----> 100
#           : angle ----> 360

