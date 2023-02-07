# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

#220208905

people_ID = ['Omar', 'Ronaldo', 'Jeff', 'Bucky']

# Simple example for loop
for person in people_ID:
  print(f'Current Person: {person}')

# how to use break in loops
for person in people_ID:
  if person == 'Jeff':
    break
  print(f'Current Person: {person}')

# using continue in a loop
for person in people_ID:
  if person == 'Jeff':
    continue
  print(f'Current Person: {person}')

# how to get the range in a loop
for i in range(len(people_ID)):
  print(people_ID[i])

for i in range(0, 11):
  print(f'Number: {i}')


# While loops execute a set of statements as long as a condition is true.
count_ID = 0
while count_ID < 10:
  print(f'Count: {count_ID}')
  count_ID += 1