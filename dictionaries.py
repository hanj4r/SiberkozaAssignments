# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

#220208905


# creating a dictionary

 personID = {
   'first_name': 'Idrees',
    'last_name': 'Dehistani',
  'age': 30 }

 print(personID)

 # we can also use a constructor
 personID2 = dict(first_name= 'peddy', last_name= 'jeffy')
 print(personID2)
 # get a vlaue from dictionary
 print(personID['first_name'])
 print(personID.get('last_name'))
 # To add a key or a vlue into a dict
 personID['laptop_model'] ='Macbook_pro'
 # to get a dictionariy's keys
 print(personID.keys())
 # to get a dictionary's items
 print(personID.items())
 # copy a dictionary
 personID2 = personID.copy()
 personID2['city'] = 'Izmir' # to add a new value to the copied dictionary
 # to remove a value
 del(personID['age'])
 # to remove a value using pop
personID.pop('laptop_model')
# to clear a dict
personID.clrear
# to get the length
print(len([personID]))
# we can have a list of dictionaries
people = [
    {'name': 'Ed', 'age': 30}
    {'name': 'Rose', 'age': 20}
]
print(people[1]['name'])

