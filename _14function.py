# function in python
"""
 what is function:
              'Function code ka ek reusable block hota hai jo kisi 
               specific task ko perform karta hai.'
    function is a block of code which is used to perform a specific task.
"""
'''
  syntex:
  def function_name(parameters):
      statements
  function_name(arguments)
'''
# types of function in python
'''
   1.built-in function
   2.user defined function
'''

# 1. built-in function: Python mein already built-in functions available hoti hay jo
#    kisi specific task ko perform karne ke liye use hoti hay.
print("-----------------")
print("built in functions in python ")
'''
    len()  used for find the length of the string, list, tuple, dictionary etc.
    input() used for taking input from the user
    type()  used for fing the data typs of the variable
    max()   used to find the maximum values in the list, tuple, dictionary etc.
    min()   used to find the minimum values in the list, tuple, dictionary etc.
    sum()   used to find the sum of the values in the list, tuple, dictionary etc.
    sorted() used to sort the values in the list, tuple, dictionary etc.
    abs()   used to find the absolute value of a number
    round() used to round a number to the nearest integer
'''
print("-----------------")
print("user defined function in python")

def hello():
    print("hello world")
hello() #function call

def add():
    a=10
    b=23
    c=a+b
    print(f"the sum of a {a} and b {b} is {c} ")
add()

print("-----------------")

print("function with parameters in python")
def addition(a,b):
    c=a+b
    print(f"the sum of a {a} and b {b} is {c} ")
addition(14,56)

print("-----------------")
print("function with default parameters in python")
def subtraction(a=6,b=5):
    c=a-b
    print(f"the subtraction of a {a} and b {b} is {c} ")
subtraction() #default parameters
subtraction(14,45)



print("-----------------")
print("multiple parameters in function in python")
def data(name,age,city):
    print(f"my name is {name} and my age is {age} and i live in {city}")
data("hassan",23,"okara")


print("-----------------")
print("return statements in function in python")
def sum(num1,num2):
    return num1+num2
print(sum(12,34))

print("-----------------")

print("parameters with user input in function")
num=int(input("enter the some number :"))
def saqure(num):
    return num*num
print(saqure(num))

print("-----------------")
'''
    Arbitrary Arguments (*args)
    If you do not know how many arguments that will be passed into your function,
    add a * before the parameter name in the function definition.
'''
print("args in function in python ")
def numbers(*args):
    print(args)
numbers(10,20,30,40)

print("-----------------")
"""
    Keyword Arbitrary Arguments (**kwargs)
    If you do not know how many keyword arguments that will be passed into your function,
    add two asterisk: ** before the parameter name in the function definition.
"""
print("kwargs in function")
def data(**kwargs):
    print(kwargs)
data(name="ali",age=22,city='london')

print("-----------------")
#local variable wo hota hay jo function kay under define kiya jata 
#   hay or us ka scope siraf function kay under tak hoti hay

print("local variable in function ") 
def local_variable():
    a=12
    print(a)
local_variable()

print("-----------------")
"""
    global variable wo hota hay jo function say bahir define kiya jata hay
    or us ka scope function say bahir bi hota hay.
"""
print("global variable in function ")
x=120
def global_variable():
    print(x)
global_variable()
print(x)


print("-----------------")
print("Recursive Function")
'''
   Recursive Function woh function hota hai jo
     apne aap ko (khud ko) call karta hai jab tak
       ek specific condition (Base Case) puri na ho.
'''
print("factorial of number using recursive function ")
def factorial(n):
    # Base Case
    if n == 0 or n == 1:
        return 1
    # Recursive Case
    return n * factorial(n - 1)
print(factorial(5))

print("Fibonacci Series Using Recursion function ")
def fibonacci(n):
    # Base Cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Recursive Case
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(6))


