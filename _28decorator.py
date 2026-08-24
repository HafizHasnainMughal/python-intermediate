# Decorator in python
'''
    Decorator ek function hota hai jo kisi doosre function ke behavior ko 
    modify ya enhance karta hai, bina original function
    ka code directly change kiye.
    
    Original Function
       ↓
    Decorator
       ↓
    Enhanced Function


'''
'''
    Decorato ko samjhnay say phalay hum functios kay kuch 
    important concepts smjhna hoin gay
'''
# first function is also object
# second hum functions ko kisi bi varible may store kar skty hain 
print('-----------------------')
def hello():
    print('kya baaat hay ')
x=hello
x()

# third function ko dosray function kay argument kay taur per pass kar saktay hain 
print('-----------------------')
def first():
    print("hello to kasay hain ap looog! ")
def second(function):
    function()
second(first)

# fourth function kay under function
print('-----------------------')
def outer():
    def inner():
        print('this is the inner function')
    inner()
    print("this is the outer function")
outer()

# fifth function ko return bi kiya ja sakta hay 
print('-----------------------')
def oouter():
    print("this is the outer function ")
    def iinner():
        print('this is the inner function')
    return iinner()
y=oouter
y()

# Decorator in python
print('-----------------------')
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper
@my_decorator  
def hello():
    print("Hello World")
hello()



