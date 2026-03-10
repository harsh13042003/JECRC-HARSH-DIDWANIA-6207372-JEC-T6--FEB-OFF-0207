'''
-- Operator Overloading: It is a phenomenon of making the operators to work on user-defined data types by invoking respective magice methods.
-- Magic Method/DUndar: It is a special type of methods in which double underscore will be there at the starting & ending of the method's name.

--Example:
    1.__add__
    2.__sub__
    3.__mul__
    4.__floordiv__
    5.__truediv__
    6.__mod__

    -- if we dont use operator overloading then what will happen
    For using the operators inside user-defined data types we have to operator overloading.

    --syntax:
    class className:
        def __init__(self,val):
            self.val= val

        def __add__(self, ano_obj):
            return self.val + ano_obj.val

obj1 = className(val1)
obj2 = className(val2)
print(obj1 + obj2) ##obj1.__add__(obj2)
'''

class MyDt:
    def __init__(self,val):
        self.val = val
        # print(self.val)

    # def __add__(self, ano_obj):
    #     # print(self.val)
    #     return self.val+ ano_obj.val

    def __str__(self):
        return str(self.val)

    # def __add__(self,ano_obj):
    #     return self.val + ano_obj.val

    def __add__(self,*ano_obj):
        sum = self.val
        for i in ano_obj:
            sum+=i.val
        
        return MyDt(sum)

    # def add(self,*args):
    #     sum= self.val
    #     for i in args:
    #         sum+=i.val
    #     return sum

    def __sub__(self,ano_obj):
        return self.val - ano_obj.val

    def __mul__(self,ano_obj):
        return self.val * ano_obj.val

    def __floordiv__(self,ano_obj):
        return self.val // ano_obj.val

    def __truediv__(self,ano_obj):
        return self.val / ano_obj.val

    def __mod__(self,ano_obj):
        return self.val % ano_obj.val

print(MyDt(10)+MyDt(20))
print(MyDt(20) - MyDt(5))
print(MyDt(2)*MyDt(2))
print(MyDt(11)//MyDt(2))
print(MyDt(11)/MyDt(2))
print(MyDt(11)%MyDt(2))
# print(MyDt.add(MyDt(100),MyDt(200),MyDt(300)))
print(MyDt(10)+MyDt(20)+MyDt(1000))
