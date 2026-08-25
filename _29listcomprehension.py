# List comprehension in python
'''
    1 >List comprehension ek concise way hai jis se hum
    existing iterable ke elements par operation karke ek new list create kar sakte hain.
    2 >A way to create a new list with less syntex can minimum certain 
    lambda function and easier to read 

'''
print("----------------------")
print("for normal code to chech one letter to fruit name ")
fruits=['mango','banana','peach','cherry']
new_list=[]
for x in fruits:
    if 'b' in x :
        new_list.append(x)
print(new_list)

print("----------------------")
print("In list comprehension way code ")
'''
    syntex:
        list=[expression for  item in iterable]
'''
square=[i*i for i in range(1,10+1)]
print(square)

print("----------------------")
# list comprehension with if condition 
'''
    syntex:
        list=[expression for item in iterabel if condition ]
'''
student_marks=[23,45,65,32,54,21,54,87]
pass_student=[j for j in student_marks if j>=33]
print(pass_student)

print("----------------------")
# list comprehension with if-else condition 
'''
    syntex:
        list=[expression if / else for item in iterabel ]
'''
student_marks=[23,45,65,32,54,21,54,87]
after_filter=[z if z>=33  else 'fail' for z in student_marks]
print(after_filter)




