# Map() function  in python
'''
    Map() applies a function to each item in an iterable (list, tuple, etc)
    syntex:
        map(function,iterable)
        function:
            the function to execute for each item.
        iterable:
            A sequence,collection or an iterator object.
'''
print("---------------")
store=[
    (1,'pen',50),
    (2,'copy',70),
    (3,'pencel',10),
    (4,'jogar',200),
    (5,'t-shirt',200),
    (6,'bag',500)
    ]
print(store)
print("I want to increase the store items price by 10%")
price=lambda item:(item[0],item[1],int(item[2]*1.10))
new_price=list(map(price,store))
print(new_price)

print("---------------")
# list kay number ka square by using map function
print("taking square of list items by using map")
numbers=[1,2,3,4,5,6,7,8,9]
square=lambda x:x*x
print(result:=list(map(square,numbers)))


