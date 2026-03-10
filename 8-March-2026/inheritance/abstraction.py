'''
Abstraction: Hiding the internal implementation and showing only functionality to the end user.

Abstract method:
    if a method/function consists of only declarartion not definition then it will be called as "Abstract method"

Abstract Class:
    If a class consists of at least one abstract method, it will be called as "Abstract Class"

Concret Class:
    It consists of zero(0) abstract method.

abc: Module
ABC: Abstract Base Class
'''

from abc import ABC, abstractmethod
class ATM(ABC):
    @abstractmethod
    def generate_pin(self):
        pass

    @abstractmethod
    def forget_pin(self):
        pass

    @abstractmethod
    def check_bal(self):
        pass

class SBI_ATM(ATM):
    def generate_pin(self):
        print('It is used to generate ATM pin!')

    def forget_pin(self):
        print('It is used to forget pin')

    def check_bal(self):
        print('Balance')

obj = SBI_ATM()
obj.generate_pin()
