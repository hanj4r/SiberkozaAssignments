# Python has functions for creating, reading, updating, and deleting files.

#220208905
# Opening a new  file
myFile_ID = open('myfile_ID.txt', 'w')

# to get some information from a file
print('Name: ', myFile_ID.name)
print('Is Closed : ', myFile_ID.closed)
print('Opening Mode: ', myFile_ID.mode)

# to write in a file
myFile_ID.write('I enjoy writing Python codes')
myFile_ID.write('and also I like swift')
myFile_ID.close()

# to append into a file
myFile_ID = open('myfile_ID.txt', 'a')
myFile_ID.write('I dont like c++')
myFile_ID.close()

# to read from file
myFile_ID = open('myfile_ID.txt', 'r+')
text_ID = myFile_ID.read(100)
print(text_ID)