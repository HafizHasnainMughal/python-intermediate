#set in python
"""
  A set is a built-in Python data type used to store multiple unique values 
  in a single variable.
  set may hum multiple unique values store kartay hain .
  it is unordered and mutable means set ka koi order nahi hota or set ko change
  kiya ja sakta hay.
  unordered :
          means set ki indexing nahi ho sakti hay is ka output har bar different ata hay 

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
#for add item in set
print("for add item in set ")
num={1,2,3,4,5}
num.add(10)
print(num)

print("----------------")
# for add multiple items in sets
print("add multiple items in set ")
multiple={2,4,6,8}
multiple.update([10,20,30])
print(multiple)

print("----------------")
# for removing item in set
print("remove item in set ")
remov={1,2,3,4,4,5}
remov.remove(3)
print(remov)



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


print("----------------")
# for copt of the set
print("copy of  the set ")
orig={1,3,5,7,9}
cpy=orig.copy()
print(cpy)
cpy.update([11,13,15,17])
print("orginal set ",orig)
print("copy set", cpy)

print("----------------")
# for making set into immutable 
print("set convert it into the immutable ")
immu=frozenset({10,20,30,40,50,60,70,80})
print("frozen set ",immu)

# immu.add(3)   it will genreate the error
# print(immu)




