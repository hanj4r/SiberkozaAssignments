#220208905 Muhammethanjar Nepesov
name = 'Hanjar'
age = 22
print ('Hello my name is'+ name + 'and I am ' + str(age)) 
print ('Hello, my name is {name} and I am {age}'.format(name=name, age=age)) 
print(f'Hello, my name is {name}, and I am {age}')
s = 'Hello everyone'
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.swapcase())
print(len(s))
print (s.replace('everyone','world'))
sub = 'e'
print(s.count(sub))
print(s.startswith('hello'))
print(s.endswith('e'))
print(s.split())
print(s.find('y'))
print(s.isalnum())
print(s.isalpha())
print(s.isnumeric())