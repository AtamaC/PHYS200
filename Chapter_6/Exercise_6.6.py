def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

# print middle('of')
# returns 'f'
# print middle('a')
# returns ''
# print middle('')
# returns ''

def is_palindrome(word):
	if len(word) == 2:
		if first(word) == last(word):
			return True
		else:
			return False
	elif len(word) == 1:
		return True
	else:
		if first(word) == last(word) and is_palindrome(middle(word)):
			return True
		else:
			return False

print is_palindrome('ardvark')	
	
