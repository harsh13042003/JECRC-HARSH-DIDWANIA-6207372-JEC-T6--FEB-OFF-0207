'''
Encapsulation -> 
                1. It is used to provide security to the data(data means variables/propeties and methods present inside the class).

How to provide security to the data ?
    To provide security, we have to use acess specifiers.
        1. public
        2. protected
        3. private

Access Specifier: 
                It described who can acess the class members(properties & methods).

'''

##Example for public acess specifier
# class Temp:
#     a,b,*c,d = 'HELLO'

#     def greeting(self):
#         print('Good Afternoon user :)')

# class C2(Temp):
#     pass

# obj = Temp()
# obj.greeting()

## PROTECTED ACESS SPECIFIER
# class Temp:
#     _a = 10
#     _b = 'I LOVE PYTHON !'

## PRIVATE ACESS SPECIFIER
# class Temp:
#     __a = 10
# #     __b = 'I LOVE PYTHON !'

#     def __status(self):
#         print('class name is temp;')


# obj = Temp()
# print(obj.__a)
# obj.__status()

''' #To access private
1. By Using syntax
2. get & set method
3. by using @property decorater(setter)
'''

### By using syntax
'''
obj_name/class_name._CN__prop_name/__method_name (Acessing)
obj_name/class_name._CN__MemberName = NewValue (Modifying)
'''

# print(obj._Temp__a)
# print(Temp._Temp__a)
# obj._Temp__status()

# obj._Temp__a = 1000
# print(obj._Temp__a)

# class Temp:
#     __a=100

#     def __status(self):
#         print('Class name is Temp')

#     def get(self):
#         print(self.__a)

#     def set(self, new_val):
#         self.__a = new_val

# obj = Temp()
# obj.get()
# obj.set(1)
# obj.get()
# print(obj._Temp__a)

##By using @property decorator
class Temp:
    __a = 10

    @property
    def get(self):
        print(self.__a)

    @get.setter
    def set(self, new_val):
        self.__a = new_val

obj = Temp()
obj.get
obj.set = 1000
obj.get
print(obj._Temp__a)