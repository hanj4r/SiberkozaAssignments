# A List is a collection which is ordered and changeable. Allows duplicate members.
#220208905
# A list is the same as an array
# create a list
oddNumbers = {1, 3, 5,7}
#we can also create a list using a constructor
evenNumbers = list((2, 4, 6,8))
print (oddNumbers, evenNumbers)

fruitsID = ['apple', 'oranges', 'grapes', 'pears']
# to get a value from a list
print (fruitsID[1]) # if you print this you might think why did it print orange and not apple, it is because a list starts from zero not one.
# to get the length of a list
print(len(fruitsID))
# to append into a list or add a new member
fruitsID.append('Bananas')
# to remove something form a list
fruitsID.remove('grapes')
# to insert a member into a special place
fruitsID.insert(3,'berry')
# remove an item from a special place using pop
fruitsID.pop(2)
# you can also reverse the list
fruitsID.reverse()
# you can sort the list
fruitsID.sort()
# you can also reverse sort
fruitsID.sort(reverse=True)


print(fruitsID)