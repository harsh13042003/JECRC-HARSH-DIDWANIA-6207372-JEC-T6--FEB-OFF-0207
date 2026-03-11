file = open('temp.txt','r')
'''
1. read(): Display the file content as it is.
2. readline(): Display single line of data at a time.
3. readlines()
'''

## to make the python interpeter to point a specific index, we use seek(index)
file.seek(0)
print(file.read())
# print(file.readline())
# print(file.readlines())
file.close()