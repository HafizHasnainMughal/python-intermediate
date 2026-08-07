# Walrus Operator in python 
'''
    walrus operator assigns values to variable as part oof a large expression.

'''
print("-----------------")
print("before the walrus operator in python ")

name=input("enter your name : ")
print(name)

print("-----------------")
print("After the walrus operator in python ")
print(name:=input("enter your name "))

print("-----------------")
print("additing items in list ")
food=list()
while(name:=input("enter your liked food items name at the end print(no) : "))!='no'.lower():
    food.append(name)
print(f"your liked food list are  {food} ")


'''
    Note:
        Walrus operator  using opposite sign in this statement Normaly used =='no'
        but  walrus  operator !='no'

'''
