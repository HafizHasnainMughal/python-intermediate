# math function in python
'''
    Python ka math ek built-in module hai jo mathematical calculations 
    ke liye ready-made functions aur constants provide karta hai.

'''
import math
# for taking square root of some value ,use sqrt(number) ,
# it generally give the floating number
print("--------------")
print("finding the square of the function ")
print(math.sqrt(25))

print("--------------")
print("find the power of the number ")
# math.pow(number,power_value)
power=math.pow(2,4)
print(power)

print("--------------")
print("for finding the factorial of any number ")
factoriall=math.factorial(5)
print(factoriall)

print("--------------")
# ceil > Number ko Upar Round Karna
ceill=math.ceil(2.345)
print("ceil :",ceill)

print("--------------")
# floor > Number ko Neeche Round Karna
flor=math.floor(7.5)
print(flor)

print("--------------")
# round() vs ceil() vs floor()
number=4.6
print(f"number {number} ceil  ",math.ceil(number))
print(f"number {number} floor ",math.floor(number))
print(f"number {number} round ",round(number))

print("--------------")
'''
    math.fabs() — Absolute Value
    Absolute value negative sign remove kar deti hai.
'''
absolute=math.fabs(-23)
print('absolute value ',absolute)

print("--------------")
'''
    math.gcd() — Greatest Common Divisor
    GCD = Greatest Common Divisor,
    yani sabse bada number jo dono numbers ko exactly divide kare.
'''

print('gdc :',math.gcd(12, 18))

print("--------------")
# math.lcm() — Least Common Multiple
lcmm=math.lcm(4,6)
print('lcm :',lcmm)

print("--------------")
pi_value=math.pi
print(pi_value)

print("--------------")
print("for finding Area = πr² ")
r=int(input("enter the radius of the circle "))
area=math.pi * r**2
print("the area of that circle is :",area)

print("--------------")
print("Euler's Number",math.e)


# Trigonometric Functions in math 
'''
Python ke math.sin(), math.cos() aur math.tan() angles ko radians mein expect karte hain,
degrees mein nahi.
'''
angle=math.radians(90)
print("degree to radian",angle)
print(math.sin(angle))
print(math.cos(angle))
print(math.tan(angle))

angl = math.pi

print("radian to degree ",math.degrees(angl))