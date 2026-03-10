## It is a type of inheritance in which the properties will be derived from single parent class to multiple child class.

class Parent:
    gold = '2kg'
    silver = '10kg'
    no_of_flats = 12

class SmallestBrother(Parent):
    pass

class ElderBrother(Parent):
    pass

obj = ElderBrother()
print(ElderBrother.gold)
