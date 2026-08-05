# dictionary in python
"""
    Dictionary Python ka built-in data type hai 
      jo Key : Value pair ki form mein data store karta hai.
    key:
          key unique hoti hay or key immutable hoti hay.
    value:
          value mutable hoti hay or value kisi bhi data type ki ho sakti hay.
    key:value = items 

"""
# syntex: dict_name = {"key1": "value1", "key2": "value2"}
print("-----------------")
print("simple dictionary in python")

data={
    "name":"hafiz hasnain",
    "age":23,
    "city":'lahore',
    "country":"pakistan"
}

print("only the keys in dictionary ",data.keys())
print("only the values in dictionary ",data.values())

# Dictionary ki Properties
'''
  1.mutable
  2.ordered
  3.duplicate keys are not allowed
  4.but duplicate values are allowed
  5.you can use any kind of data type in dictionary
'''
# 1.mutable: Dictionary mutable hoti hay or is mein 
#    items ko add, remove or update kiya ja sakta hay.
print("-----------------")
print("update item in dictionary ")
student={
    "name":"hafiz hasnain",
    "age":23
}
student["age"]=24
print("updated age in dictionary ",student)

print("-----------------")
print("use different data types in dictionary")
data1 = {
    "name":"Ali",
    "age":20,
    "marks":90.5,
    "pass":True,
    "subjects":["Math","Physics"],
    "address":{
        "city":"Lahore",
        "country":"Pakistan"
    }
}
# accessing items in dictionary
# 1. Method : by using key name
print(data1["name"])
print(data1['address'])
print(data1['subjects'])

# 2. Method : by using get() method ,
# get use karnay say ya hota hay kay agar key exist nahi karti
#  tu error nahi aye ga or none return kare ga .
print(data1.get("name"))
print(data1.get("cast")) #ya key exist nahi karti is waja say none retrn karay ga