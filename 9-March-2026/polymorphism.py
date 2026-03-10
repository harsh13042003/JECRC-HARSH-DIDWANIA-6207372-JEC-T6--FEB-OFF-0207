##using the same method name or operator to perform two or more differrnt operations.

# class Temp:
#     def sum(self,a,b):
#         print(a+b)

#     def sum(self, a, b, c):
#         print(a+b+c)

# obj = Temp()
# obj.sum(10,20)


## In python, if we want to perform method overloading then it will acts as method overriding
## In other programming languages, based upon no of arguments, the respective mehod block will get executed. But in python, it never happens
## method overloading is a pheneomenon of overiding the prev method's address with the latest one.

class Temp:
    def sum(self,a,b):
        print(a+b)

    add_two_nums = sum ## have prev address of func 

    def sum(self, a, b, c):
        print(a+b+c)

obj = Temp()
obj.sum(10,20,30)
obj.add_two_nums(10,20)