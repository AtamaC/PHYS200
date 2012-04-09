import math


# Start with a basic outline

def hypotenuse(l1,l2):
    return 0.0

# Add intermediate calculations

def hypotenuse(l1,l2):
    l1_squared = l1**2
    print l1_squared
    l2_squared = l2**2
    print l2_squared
    return 0.0

# Add more calculations

def hypotenuse(l1,l2):
    l1_squared = l1**2
    l2_squared = l2**2
    squared = l1_squared + l2_squared
    print squared
    return 0.0

# Add final calculations

def hypotenuse(l1,l2):
    l1_squared = l1**2
    l2_squared = l2**2
    squared = l1_squared + l2_squared
    hyp = math.sqrt(squared)
    return hyp

# Condense code

def hypotenuse(l1,l2):
    squared = l1**2 + l2**2
    return math.sqrt(squared)

hyp = hypotenuse(3,4)
print hyp

