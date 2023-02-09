#220208905 Muhammethanjar Nepesov
nameId = ('Hanjar', 'Seper', 'Dovlet')
nameId2 = tuple(('Hanjar', 'Seper', 'Dovlet'))
print (nameId, nameId2)
print(len(nameId))
nameId_set = {'Hanjar', 'Seper', 'Dovlet'}
print('Hanjar' in nameId_set)
nameId_set.add('sepehr')
nameId_set.remove('dovlet')
print(nameId_set)