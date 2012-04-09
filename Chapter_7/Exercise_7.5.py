import math

def factorial(n):
	if n == 0:
		return 1
	else:
		recurse = factorial(n-1)
		result = recurse * n		
		return result

def estimate_pie():
	k = 0
	term = 1
	summation = 0
	factor = (2*math.sqrt(2)/9801)
	while abs(term) >= 1e-15:
		numerator = factorial(4*k)*(1103+26390*k)
		denominator = (factorial(k)**4)*396**(4*k)
		term = numerator/denominator * factor
		summation = summation + term
		k = k + 1
	pi = (summation)**-1
	return pi

pi = estimate_pie()
print math.pi
print pi
print abs(pi - math.pi)


