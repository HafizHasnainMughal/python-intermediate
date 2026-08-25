# Dictionary comprehension in python
'''
    In which create the dictionary using an  
    expression can replace for loops and lambda function

'''
print("--------------------")
# simple dictionary comprehension
'''
    syntex:
        x={key:expression for (key,value) in iterable.items()}
'''
cities={
    'lahore':45,
    'okara':35,
    'karachi':44
}
updated_cities={key:(value-32/2) for (key,value) in cities.items() }
print(updated_cities)

print("--------------------")
# if condition in dictionary comprehension 
'''
    syntex :
        y={key:expression for (key,values) in iterable,items() if condition}
'''
cities={
    'lahore':45,
    'okara':35,
    'karachi':44
}
updates={key:value for (key,value) in cities.items() if value>=40}
print(updates)

print("--------------------")
# if/else condition in dictionary comprehension 
'''
    syntex :
        y={key:(if/else condition ) for (key,values) in iterable,items()}
        OR
        x={key:function (value) for (key,value) in iterable.items()}
'''
cities={
    'lahore':45,
    'maree':35,
    'karachi':44,
    'multan':50
}
print(new_updates:={key:('hot' if value >=40 else 'cold') for (key,value) in cities.items()})
print("--------------------")
def hello(values):
    if values>=50:
        return "Hot"
    elif values>=49  and values<=30:
        return "Warm"
    else:
        return "Cold"
cities={
    'lahore':45,
    'maree':35,
    'hunza':20,
    'karachi':44,
    'multan':50,
    "thar":60
}
new_updated_dict={key:hello(values) for (key,values) in cities.items()}
print(new_updated_dict)
