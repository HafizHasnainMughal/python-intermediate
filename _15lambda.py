# lambda function in python
"""
    Lambda function Python ka ek small,
    anonymous function hota hai jo usually ek
    simple operation ko ek line mein perform karta hai.
     
    syntex:
        lambda parameter : expression
"""
print("-----------------")
print("simple lambda function  in python ")

x= lambda x :x+10
print(x(5))

print("-----------------")
print("square of the number using lambda function in python")
y=lambda x:x*x
print(y(23))

print("-----------------")
print("addition of two numbers using lambda function in python ")
addition=lambda x,y:x+y
print(addition(10,30))

print("-----------------")
print("condition in lambda function in python ")
"""
  for condition in lambda function syntex:
    labda paramter:true_value if condition else false_value
"""
check_age=lambda age:True if age>=18 else False
print(check_age(23))
# OR
check_ag=lambda age:'Adult' if age>=18 else 'Child'
print(check_ag(23))

print("-----------------")
print("lambda function in function in python ")
def my_function(n):
    return lambda a : a * n
lmd=my_function(2)
print(lmd(5))




