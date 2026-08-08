# Reduce in python
'''
    Reduce() function apply a function to an iterable and reduce it to 
    a single commulative value,performs function on first two elements and repeats process
    until one value is remainning. 
    
    syntex:
        import functools
        functool.reduce(function,iterable)
        function:
            A function to be run for each item in the iterable
        iterable:
            the iterable to be reduced.
'''
print("----------------")
print("simple reduce function ")
import functools
numbers=[1,2,3,4,5,6,7,8,9]
red=lambda x,y:x+y
sum_up=functools.reduce(red,numbers)
print(sum_up)


print("----------------")
print("multiply the list items is same tha finding factorial ")
num=[1,2,3,4,5,6]
print(mul:=functools.reduce(lambda x,y:x*y,num))

