from TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.001

def koch(t,length):
    if length < 3:
	fd(t,length)
    else:
	koch(t,length/3)
	lt(t,60)
	koch(t,length/3)
	rt(t,120)
	koch(t,length/3)
	lt(t,60)
	koch(t,length/3)

def snowflake(t,length):
    for i in range(3):
	koch(t,length)
	rt(t,120)

l = 243

snowflake(bob,l)

die(bob)
wait_for_user()
