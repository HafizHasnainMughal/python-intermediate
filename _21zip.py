# Zip() function in python
'''
    zip() function is used to connrct two or more iterable(list,tuple,set etc)
    together ,paring the elements as tuples,for each elements
'''

print("-------------------")
name=['hassan','ahmad','jhon','michale','A.d']
marks=(23,45,67,83,95)
lst=list(zip(name,marks))
print(f"for in list type {lst}")
dic=dict(zip(name,marks))
print(f"for in dictionary type ")

for key,values in dic.items():
    print(key,":",values)