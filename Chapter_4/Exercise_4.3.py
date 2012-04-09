from TurtleWorld import *
import math

def triangle(t,base,angle):
    rad_angle = math.pi * angle/180
    side = base * math.sin((math.pi - rad_angle)/2)/math.sin(rad_angle)
    fd(t,base)
    lt(t,90 + angle/2)
    fd(t, side)
    lt(t,180 - angle)
    fd(t, side)
    lt(t,90 + angle/2)

def pie(t,n,length):
    angle = 360.0/n
    for i in range(n):
	triangle(t,length,angle)
	fd(t,length)
	lt(t,angle)
    

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

pu(bob)
fd(bob,-150)
pd(bob)

rt(bob,54)
pie(bob,5,60)

pu(bob)
lt(bob,54)
fd(bob,120)
lt(bob,90)
fd(bob,25)
lt(bob,180)
pd(bob)
pie(bob,6,50)

pu(bob)
lt(bob,180)
fd(bob,-25)
rt(bob,90)
fd(bob,110)
rt(bob,450/7)
pd(bob)
pie(bob,7,40)


die(bob)

wait_for_user()
