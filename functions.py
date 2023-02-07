# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

#220208905

#creating a function
def sayHello():
    print(f'Hello {name}')
    sayHello('peddy jeffery')

# a function to return a value
def getSumID(number1, number2):
    total = number1 + number2
    return total


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSumeID = lambda number1, number2: number1 + number2
print (getSumeID(11, 2))
