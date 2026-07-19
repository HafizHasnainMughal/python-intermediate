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
