def is_power(a,b):
	if a%b == 0 and is_power(a/b,b):
		return True
	else:
		if a == b:
			return True
		else:
			return False

