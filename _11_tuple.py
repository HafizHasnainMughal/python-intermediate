#tuple in python 
"""
  1. Immutable (Cannot Be Changed)
  2. Faster Than Lists 
  3. Less Memory Usage
  4. Can Be Used as Dictionary Keys 
  5. Easy Packing and Unpacking
      student = ("Ali", 20)
      name, age = student
      print(name)
      print(age)
  6. Useful for Fixed Data

  tuple bi ik single variable hota hay jis may multiple values store hoti hain
  like list but tuple is immutable means values ko changes nahi kiya ja sakta hay
  Any method to changes values cannot be applied in tuple

  syntex:
      tuple ko create karnay kay liya  this brackets "()" ka use hota hay 
      like num=(2,3,4,5,6,7)
"""

print("------------------")
#create the empty tuple
print("the empty tuple ")
empty=()
print(empty)
print(type(empty))


print("------------------")
#for single value
print("single values in tuple")
single_value=(3,)
print(single_value)
print(type(single_value))
 
print("------------------")
single_int=(3)
print(single_int)
print(type(single_int))

print("------------------")
#create the tuple with some values
print("tuple with some values ")
colour=("red","blue","pink","black")
print(colour)

print("------------------")
#for multiple different values
print("different values in tuple")
data=("hassan",23,"address","sex",5.6,True)
print(data)

print("------------------")
#for index calling
data=("hassan",23,"address","sex",5.6,True)
print(data[4])
print("slicing ",data[0:2+1])
print("negative indexing",data[-2])

print("------------------")
#for print tuple values by using for loop
print("for print tuple values by using for loop")
data=("hassan",23,"address","sex",5.6,True)
for x in data:
    print(x)

print("------------------")
# tuple cannot be changed but if you convert the 
#    tuple --> list
#  changing something  and 
#    again list --> tuple

data=("hassan",23,"address","sex",5.6,True)
print(data)
print("before adding some thing data type",type(data))
data=list(data)
data.append("female")
data.insert(2,"house no.")
print("after converting tuple to list ")
print(data)
print(type(data))
print("again changes into tuple ")
data=tuple(data)
print(data)
print(type(data))

print("------------------")
#some method we used in tuple  

data=("hassan",23,"address","sex",5.6,True)
print("length of the tuple : ",len(data))
print("------------------")

num=(1,2,3,4,5,56,7,8)
print("for finding minimum value ",min(num))
print("for finding maximum value ",max(num))
print("for finding sum values in tuple ",sum(num))