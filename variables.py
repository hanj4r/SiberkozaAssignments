# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""




#220208905

# we can create variables one by one
x = 4             # This is an int
y = 4.5           #This is a float (It is a decimal value)
name = 'Harry'    # This is a string
is_funny = True    #This is a bolean which can be either true or false
print (x, y, name,is_funny)
# or we can do something much easier to give vaiables values.
a, b, surname, is_rude = (2, 3.3, 'Linda', True)
print(a,b,surname,is_rude)
#we can also do basic math
M = a + x
print(M)
# we can also change the type of a variable or as it is called in the video CASTING
x = str(x)
y = int(y)
z = float(y)
print (type(z), z)