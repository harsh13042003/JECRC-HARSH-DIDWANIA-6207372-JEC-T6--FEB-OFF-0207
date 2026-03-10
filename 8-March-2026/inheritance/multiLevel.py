'''
-- It is a type of inheritance in which the properties will be derived from one to another class by considering more than one level.
'''

class Class_1:
    a = 'Class_1'

class Class_2(Class_1):
    b = 'Class_2'

class Class_3(Class_2):
    c = 'Class_3'

class Class_4(Class_3):
    d= 'Class_4'

class Class_5(Class_4):
    e= 'Class_5'

obj = Class_5()
print(obj.a)