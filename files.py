#220208905 Muhammethanjar Nepesov
personalId = open('personalId.txt', 'w')
print('Name: ', personalId.name)
print('Is Closed : ', personalId.closed)
print('Opening Mode: ', personalId.mode)
personalId.write('Js the best')
personalId.write('Mern App')
personalId.close()
personalId = open('personalId.txt', 'a')
personalId.write('I dont like python')
personalId.close()
personalId = open('personalId.txt', 'r+')
text_ID = personalId.read(100)
print(text_ID)