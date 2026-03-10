'''
lambda(Anonymous Function):
        1. Lambda is a keyword, which is used to create a anonymous function.
'''

## lambda args: <exp>
# result = lambda a,b: a+b
# print(result)
# print(result(1,2))

# (lambda a,b: print(a+b))(int(input('First Num: ')), int(input('Sec Num: ')))

## WAP to find the square of a number if it is even
# num = int(input('Enter a number : '))
#     if num % 2 == 0:
#         print(num**2) 


result = lambda num: print(num ** 2) if num % 2 == 0 else None
result(10)




