# filter in python

'''

 filter in Python is a built-in function that allows
 you to filter elements from 
 an iterable (like a list, tuple, or set) based on a specified condition.
 It takes two arguments: a function and an iterable.
 The function is applied to each element of the iterable,
 and only those elements for which the function returns True are included in the result.
'''

'''
    syntex:
        filter(function, iterable)
        function:
            the function to execute for each item.
        iterable:
            A sequence,collection or an iterator object.
'''
print("---------------")
print("filter in python ")
# check age by using filter method
age=[12,16,11,20,21,34,65,78,45,32]
def check_age(x):
    if x<=18:
        return False
    else:
        return True
adult=list(filter(check_age,age))
print(adult)

print("---------------")
print("student data say pass's students filterd ")
data=[
    ('Ali',23,'F'),
    ('ahmad'.title(),54,'E'),
    ('Moize',57,'D'),
    ('Hassan',67,'C'),
    ('qaasim'.title(),78,'B'),
    ('jhon'.title(),27,'F'),
    ('Abbas',99,'A'),
]
print("before filter tha data ")
for x in data:
    print(x)
marks=lambda data:data[1]>=33
pass_student=list(filter(marks,data))
print("before filter tha data ")
for y in pass_student:
    print(y)


