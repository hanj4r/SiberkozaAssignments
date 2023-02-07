# If/ Else conditions are used to decide to do something based on something being true or false
#220208905

x = 11
y =  6


# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values


# a simple if statement
if x > y:
    print(f'{x} is greater that {y}')
# a if/else statement
if x > y:
    print(f'{x} is greater that {y}')
else:
    print(f'{y} is greater that {x}  ')

    # else if or also called as elif
    if x > y:
        print(f'{x} is greater that {y}')
    elif x == y:
        print(f'{x} is equal to {y}')
    else:
        print(f'{y} is greater that {x}  ')

# nested if statement
if x >2:
    if x <= 10:
        print(f'{x} is greater than 2 and less or euqal to 10')

# Logical operators (and, or, not) - Used to combine conditional statements

# and statement
if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less or euqal to 10')

# Or statement
if x > 2 or x <= 10:
    print(f'{x} is greater than 2 and less or euqal to 10')

# not statement
if not(x == y ):
    print(f'{x} is not equal to {y}')



# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object
# Using In
numbersID = [1,2,3,4,5,6,7]
if x in numbersID:
    print(x in numbersID)
# using not in
if x is not in numbersID:
    print(x not in numbersID)


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# using is
if x is y:
    print(x is y)

# using is not
if x is not y:
    print(x is not y )