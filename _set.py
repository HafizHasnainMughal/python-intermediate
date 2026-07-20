#set in python
"""
  A set is a built-in Python data type used to store multiple unique values 
  in a single variable.
  set may hum multiple unique values store kartay hain .
  it is unordered and mutable means set ka koi order nahi hota or set ko change
  kiya ja sakta hay.

  syntex:
      set={"1items","2items"  }

"""

print("----------------")
print("simple set in python")
fruits = {"Apple", "Banana", "Mango"}
print(fruits)

print("----------------")
print("using set function ")
numbers = set([1, 2, 3, 4])
print(numbers)

print("----------------")
# empty set
print("for making empty set")
empty = set()
print(type(empty))

print("----------------")
#print by using for loop
fruits = {"Apple", "Banana", "Mango"}
for x in fruits:
    print(x)

print("----------------")
#Set Operations
print("Set Operations ")
print("Union Combines two sets.")
A = {1,2,3}
B = {3,4,5}
print(A | B)
# or other method to take unoin of two sets 
print(A.union(B))


print("----------------")
print("Intersection Common elements.")
A = {1,2,3}
B = {2,3,4}
print(A & B)
# or other method to take intersection of two sets 
print(A.intersection(B))


print("----------------")
print("Difference Elements present in A but not in B.")
A = {1,2,3}
B = {2,3,4}
print(A - B)
# or other method to take difference  of two sets 
print(A.difference(B))

