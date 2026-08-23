# modules in python 
'''
    Python module ek .py file hoti hai jisme Python code,
    functions, classes, ya variables hote hain, 
    jise hum doosri Python file mein reuse kar sakte hain.

    There are three types of modules in python
    1.Built-in / Standard Library Modules
        wo modules ya libraries jo python povide karta hay
        like >>math, random, os, datetime, statistics, json, re etc
    2.User-defined Modules
        Jo module hum khud banate hain.
        like calulator.py
    3. Third-party Modules
        Jo Python ke saath default nahi aate aur usually pip se install kiye jate hain.
        like pandas, numpy, matplotlib etc 

'''
print("-----------------------")
from calculator import addition,subtract,multiply

reult=addition(10, 5)
print(reult)
print(subtract(10, 5))
print(multiply(10, 5))

print("-----------------------")
import student

student.student_info(
    "hassan".title(),
    21,
    "Computer Science"
)
marks = [80, 75, 90, 65, 85]
average = student.calculate_average(marks)
print("Average:", average)
result = student.check_result(average)
print("Result:", result)