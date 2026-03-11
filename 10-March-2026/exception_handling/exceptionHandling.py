'''     Exception - Handling
Exception -->
-Unauthorized event
-Flow of the exception of the program will be stopped
-After that it will never execute the following code

try:
except:
finally:
else:

try: we will put the problem statement.(Block of code due to which we might get error)

else: It is an alternative of try block. if we find out any error inside try block interpeter we will move forward else block

except: We put the actual solution for the error 
    Due to except block we can prevent the unauthorized events (errors)

finally: After getting error or after resoltuion, forcefully if we can execute any particular blcok of code, we use finally block.

Approaches:
        --> Specific Exception Handling
        --> Generic Exception Handling
        --> Default Exception Handling

Specific Exception Handling ->

    --If we are aware of the error or, exception then we go with "specific"

    try:
        problem
        statement
    except ErrorName:
        resolution/
        solution code
-->
'''

# n1, n2 = 21,0
# try:
#     ## Problem Statement
#     result = n1/n2
#     print(result)
# except ZeroDivisionError:
#     ## Solution Code
#     print('Please do not choose 0 as the second number !')

'''
Generic Exception Handling:

-- It is a type of exception handling in which there is no need to pass any particular exception class name. Instead of we can use parent "exception" called "Excpetion"

--Using "generic exception handling". we can't handle keyborad interuption
'''
# try: 
#     a,b, c = 1,2
# except ValueError:
#     print('For performing MVC, no of variables should be equals to no of values!')

# try:
#     print(a,b,c)
# except NameError:
#     print('Identifiers are not there in the memory')

# import time
# try:
#     while True:
#         print(time.time()) # Main drawback of generic
# except Exception:
#     print("loop got stopped")

'''
Default Exception Handling
    -- It is a type of exception handling in which we can handle all types of errors or exceptions excpet "SyntaxErro"
'''

# import time
# try:
#     while True:
#         print(time.time()) # Main drawback of generic
# except:
#     print("loop got stopped")

'''
Exception creation

    `1. Custom Exception, (raise)
    2. User_defined Exception (raise)
    3. Assertion Exception, (assert)

Custome Exception:
    1. We use pre-built Exception classes according to our requirement.

        raise ValueError('message')

        ValueError: message
'''

# num = 17
# if num >= 18:
#     print('you are eligible')
# else:
#     raise ValueError('Your are short in age')

'''
2. user defined exception ->
    it is a type of exception in which we can create our won exception classes based upon our own requirements, we can also provides name to those class acording to user cases

'''
'''
class MyException(Exception):
    pass

n1,n2 = 10,0
if n2 == 0:
    raise MyException('zero')
else:
    print(n1/n2)
'''

'''
    Assertion Exception
    --Assertion exception can be created by using one keyword called "assert.

    assert <condition>, print(ERROR)
    print(output)
'''

s=input('Enter a string')
assert s == s[::-1], print('It isnot a palindromic String!')
print('It is a palindromic string ')
   


