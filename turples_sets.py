# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.


#220208905
# creating a tuple
fruitsID = ('apple', 'orange', 'grape')
            #creating a tuple using a constructor
fruitsID2 = tuple(('apple', 'orange', 'grape'))
print (fruitsID, fruitsID2)
# a single tuple value needs a trailing comma. if you don't put the comma it will think it is a string
# you cant change a tuple item like you can in list
#delete tuple
       #del fruitsID
# to get the length
print(len(fruitsID))


# A Set is a collection which is unordered and unindexed. No duplicate members.
# to create a set
fruitsID_set = {'cherry', 'berry', 'banana'}
# to check if an item is in a set
print('berry' in fruitsID_set)
# to add an element to a set
fruitsID_set.add('apple')
#removing an element from a set
fruitsID_set.remove('banana')
# to clear a set
     #fruitsID_set.clear()
# to delete a set
      #del fruitsID_set

print(fruitsID_set)