##Inheritance

'''
    1. Single level
    2. Multi-level
    3. Multiple
    4. Hierarachical
    5. Hybrid

'''

##Single Level
## we will have a single parent & child class. Also the properties will be derieved only one time.

##Parent Class or, Super class
## The class from which we are going to derieve the properties, is known as Parent class.
class Parent:
    bank_balance = '54L'
    def __init__(self, members):
        self.members=members
    def desc(self):
        print('I am parent class')


## Child class or sub class
## The class in which we are going to derieve the properties, is known as Child class.
class Child(Parent):
    # pass

    def __init__(self,child_name, *args):
        self.child_name=child_name
        super().__init__(args)

    def display(self):
        super().desc()

# obj = Child()
# print(obj.bank_balance)
# obj.desc()

##Constructor Chaining: Calling Parent's class constructor from inside child class's constructor

obj = Child('Child','Mom','Dad')
print(obj.members)
print(obj.child_name)
obj.display()