#220208905 Muhammethanjar Nepesov
perssonalId = ['Sepehr', 'Dovlet', 'Hanjar', 'Omer']
for person in perssonalId:
  print(f'Current Person: {person}')
for person in perssonalId:
  if person == 'Sepehr':
    break
  print(f'Current Person: {person}')
for person in perssonalId:
  if person == 'Hanjar':
    continue
  print(f'Current Person: {person}')
for i in range(len(perssonalId)):
  print(perssonalId[i])
for i in range(0, 11):
  print(f'Number: {i}')
count_ID = 0
while count_ID < 10:
  print(f'Count: {count_ID}')
  count_ID += 1