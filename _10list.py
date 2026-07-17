#list in python

"""
    list is ordered collection of items which can be of any data type.
    list is mutable which means we can change the items in the list.
"""

#list may hum kisi bi data type ko store kar sakte hain 
# like string, integer, float, boolean, etc.
# to storing multiple items in a single variable we use list in python 
# list creating in python is done by using square brackets [] and 
# separating the items with commas.

name=["hassan", "ali", "ahmed", "hussain"]
print("listof name")
print(name)
print(type(name))

#for indexing the list we use index number which starts from 0
print("indexing the list")
print(name[0])  # prints "hassan"   
print(name[1])  # prints "ali"
print(name[2])  # prints "ahmed"

#for mutating the list we can change the value of the list by using index number
print("mutating the list")
name[0]="saqib"  #in which adding the new value in the list by using index number
print(name)

#for slicing the list we use slice operator which is [start:stop:step]
print("slicing the list")
print(name[0:2])  # prints ["hassan", "ali"]
print(name[1:3])  # prints ["ali", "ahmed"]
print(name[0:4:2])  # prints ["hassan", "ahmed"]


print("reverse the list")
print(name[::-1])


#also store the different data types in the list like string, integer, float, boolean, etc.
data=["hassan", 20, 3.14, True]
print("list of different data types")
print(data)


#list methods in python
"""
  for adding the new item in the list we use append() method  like name.append("new item")
  for removing the item from the list we use remove() method like name.remove("item to be removed")
  for popping the item from the list we use pop() method like name.pop() or name.pop(index)
  for sorting the list we use sort() method  like name.sort() or name.sort(reverse=True)
  for reversing the list we use reverse() method  like name.sort(reverse=True) or name.reverse()
  for copying the list we use copy() method like name.copy()
  for finding the length of the list we use len() function 
  for finding the index of an item in the list we use index() method
  for extending the list we use extend() method
  for inserting an item in the list we use insert() method
  for clearing the list we use clear() method
  for checking if an item is in the list we use in operator
  for checking if an item is not in the list we use not in operator   

"""


#for adding the new item in the list we use append() method
ages=[20, 21, 22, 23]
print(ages)
ages.append("40")
print(ages)

#for removing the item from the list we use remove() method
ages.remove(21)
print(ages)

#for popping the item from the list we use pop() method
ages.pop()  # removes the last item from the list
print(ages)

#for sorting the list we use sort() method
ages.sort() #for ascending order
print(ages)

ages.sort(reverse=True) #for descending order
print(ages) 


#for copying the list we use copy() method
"""
   copy wala method hum tab use kartay hain jab orignal list ko change nahi karna 
   hota aur uska copy banana hota hay. 
   Or phir hum copy wali list per different methods apply kartay hain .
  
"""
ages_copy=ages.copy()
print(ages_copy)


#for length finding of the list  items use len()
print(len(ages))

#for  extend the list  in which we join the two lists

list1=[1,2,3,4,5,6]
list2=[7,8,9]
list1.extend(list2)
print(list1)

#for inserting the items in existing list insert(index, item) method use hota hay

inst=["hassan", "ali", "ahmed", "hussain"]
inst.insert(2, "saqib")  #inserting the new item in the list at index 2
print(inst) 


#for del() delete the item from the list by using index number
del(inst[2])  #deleting the item from the list at index 2
print(inst)
