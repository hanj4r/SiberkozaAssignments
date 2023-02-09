#220208905 Muhammethanjar Nepesov


 personalId = {
   'firstName': 'Muhammethanjar',
    'lastName': 'Nepesov',
  'age': 22 }

 print(personalId)

 personalId2 = dict(firstName= 'Vladik', lastName= 'Ramos')
 print(personalId2)
 print(personalId['firstName'])
 print(personalId.get('lastName'))
 personalId['model'] ='Lenovo'
 print(personalId.keys())
 print(personalId.items())
 personalId2 = personalId.copy()
 personalId2['city'] = 'Ankara' 
 del(personalId['age'])
personalId.pop('model')
personalId.clrear
print(len([personalId]))
people = [
    {'name': 'Hanjar', 'age': 22}
    {'name': 'Vladik', 'age': 22}
]
print(people[1]['name'])

