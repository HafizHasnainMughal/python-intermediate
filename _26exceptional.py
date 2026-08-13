# Exceptional handling in python
'''
    very import concept in python
    Python mein Exception Handling bohat important topic hai,
    especially jab tum real applications banana start karte ho.

    Exception ka matlab hai:
    Program run hote waqt koi unexpected problem/error aa jana.

'''
print("------------------")
# for example
number=int(input("enter the some number "))
print(number)
# if you entered the string value tu phir error aye ga 
'''
    ValueError   : age = int("abc")
    ZeroDivisionError : result = 10 / 0
    TypeError : result = "10" + 5
    IndexError : numbers = [10, 20, 30] ,print(numbers[5])
    KeyError  : student = {"name": "Ali"},print(student["age"])
    FileNotFoundError : file = open("abc.txt")

    basic syntex:
    try:
        # risky code
    except:
        # error handle

'''
try:
    num=int(input("ente the some mumber :"))
    print(num)
except:
    print("you entered the wronge data type ")

print("------------------")
try:
    num1 = int(input("Enter number: "))
except ValueError:
    print("Please enter a valid number.")


print("------------------")
print("use multiple exceptions ")
try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    result = number1 / number2
    print(result)
except ValueError:
    print("Please enter numbers only.")
except ZeroDivisionError:
    print("You cannot divide by zero.")

'''
    try:
        # risky code
    except:
        # error
    else:
        # no error
'''
print("------------------")
try:
    numbers = int(input("Enter number: "))

except ValueError:
    print("Invalid number.")

else:
    print("You entered:", numbers)
