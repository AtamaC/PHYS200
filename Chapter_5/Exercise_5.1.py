def check_fermat(a,b,c,n):
    LHS = a**n + b**n
    RHS = c**n
    if LHS == RHS and n > 2:
	print 'Holy smokes, Fermat was wrong!'
    else:
	print "No, that doesn't work."

def fermat_prompt():
    print "This program checks Fermat's Theorem by checking if a^n + b^n = c^n"
    a = int(raw_input('Enter an intiger value for a.\n'))
    b = int(raw_input('Enter an intiger value for b.\n'))
    c = int(raw_input('Enter an intiger value for c.\n'))
    n = float(raw_input('Enter a value for n.\n'))
    check_fermat(a,b,c,n)

fermat_prompt()	    
