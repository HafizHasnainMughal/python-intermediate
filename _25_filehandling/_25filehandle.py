# File Handling in Python
'''
    File handling ka matlab hai Python program ke through kisi file ko:

        create karna
        open karna
        read karna
        write karna
        existing data update karna
        append karna
        delete karna

    Basic workflow of file handling:

        Open File
            ↓
        Perform Operation
            ↓
        Close File
'''

print('----------------------')
print("Read the text file")

file_read = open("_25fileread.txt", "r")
data = file_read.read()
print(data)
file_read.close()


print('----------------------')
print("Write method in file handling")

# "w" ka matlab write hai.
# Agar file already exist karti hai to purana data overwrite ho jayega.

file_write = open("_25filewrite.txt", "w")
file_write.write("Imam Mula Ali A.S")
file_write.close()

'''
    Important Note:

    w Mode
    w existing file ke old content ko overwrite kar deta hai.

    w = Write + Old Data Replace
'''


print('----------------------')
print("Write multiple lines")

file_write = open("_25filewrite.txt", "w")

file_write.write("Imam Mula Ali A.S\n")
file_write.write("Imam Mula Hasan A.S\n")
file_write.write("Imam Mula Hussain A.S\n")

file_write.close()


print('----------------------')
print("Append method in file handling")

file_append = open("_25fileappend.txt", "a")

for x in range(5):
    file_append.write("Imam Mula Ali A.S\n")

file_append.close()


print('----------------------')

'''
    x — Create Mode

    x ka use new file create karne ke liye hota hai.
    Agar file already exist karti ho to FileExistsError aata hai.
'''

print("Create a new file")

file_create = open("_25newfile.txt", "a")
file_create.write("Hello Python")
file_create.close()


print('-----------------------')
print("Another best method: with open()")

# with open() use karne ka faida:
# file automatically close ho jati hai.

with open("_25fileread.txt", "r") as file:
    data = file.read()
    print(data)


print('------------------------')
print("Enter the student data")

while True:

    name = input("Enter your name: ")
    age = input("Enter your age: ")
    city = input("Enter your city: ")

    question = input(
        "If you want to enter another student, press Enter. "
        "Otherwise type 'no': "
    )

    with open("_25student.txt", "a") as file:

        file.write("New Student -----\n")
        file.write("\n")

        file.write(f"Name: {name.title()}\n")
        file.write(f"Age: {age}\n")
        file.write(f"City: {city.title()}\n")

        file.write("\n")

    if question.lower() == "no":
        break

'''
    Note:
        is ko run karnay kay liya ap ko exect file directory open karna hoti hay 


'''