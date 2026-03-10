'''
-- It is atype of inheritance in which the properties will be derived from multiple parent  class to a single child class.
'''

class Parent_1:
    a = 10

class Parent_2:
    b = 20

class Child(Parent_1,Parent_2):
    pass

obj = Child()
print(obj.a, obj.b)