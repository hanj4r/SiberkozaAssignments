# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
#220208905
name = 'Ahmet'
age = 22
# to insert a varibale into a string
print ('Hello my name is'+ name + 'and I am ' + str(age)) #In order to print an int we need to wrap it in a string first

# String Formatting
# we can aslo do this in another way called 'Arguements by position
print ('Hello, my name is {name} and I am {age}'.format(name=name, age=age)) #the curly brackets act like a place holder for the variable
# we can also do this by using F-STRINGS
print(f'Hello, my name is {name}, and I am {age}')

# String Methods
# These are basic functions that are built in python to use for their reasons 
s = 'Hello everyone'
# to capitalize the letters
print(s.capitalize())
# To make all the letters uppercase
print(s.upper())
#to make all the letters lowercase
print(s.lower())
#to swap case
print(s.swapcase())
# to get the length
print(len(s))
# to replace something
print (s.replace('everyone','world'))
# to count
sub = 'e'
print(s.count(sub))
# starts with
print(s.startswith('hello'))
# ends with
print(s.endswith('e'))
# split it into a list
print(s.split())
# Find the postion of a charecter
print(s.find('y'))
# is it all alphanumeric
print(s.isalnum())
# is it all alphabetic
print(s.isalpha())
# is it all nummeric
print(s.isnumeric())