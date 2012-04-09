from TurtleWorld import *
from polygon import *

def leaf(t, r, angle):
    for i in range(2):
	arc(t, r, angle)
	lt(t, 180 - angle)

def flower(t, r, angle, n):
    for i in range(n):
	leaf(t, r, angle)
	lt(t, 360.0/n)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

pu(bob)
fd(bob, -100)
pd(bob)

flower(bob, 60.0, 60.0, 7)

pu(bob)
fd(bob, 100)
pd(bob)

flower(bob, 40.0, 80.0, 10)

pu(bob)
fd(bob,100)
pd(bob)

flower(bob, 140.0, 20.0, 20)

die(bob)

wait_for_user()


