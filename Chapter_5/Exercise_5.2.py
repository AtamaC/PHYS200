def is_triangle(a,b,c):
    if c > a + b or b > a + c or a > b + c:
	print 'No'
    else:
	print 'Yes'

def triangle_prompt():
    print 'This program checks 3 lengths to see if they can form a closed triangle.\n'
    a = float(raw_input('Enter a length.\n'))
    b = float(raw_input('Enter another length.\n'))
    c = float(raw_input('Enter a third length.\n'))
    is_triangle(a,b,c)

triangle_prompt()
