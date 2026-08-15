# file handling in python
'''
    the most important method in phon is file handling.

    File Handling ka matlab hai Python program ke through kisi file ko:
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
print("read the text file ")
file_read = open("_25fileread.txt", "r")
data = file_read.read()
print(data)
file_read.close()

print('----------------------')
print('write method in filehandling ')
# w ka matlab write hai.
# Iska use file mein data write karne ke liye hota hai.')

file_write = open("_25filewrite.txt", "w")
file_write.write("Imam Mula Ali A.S ")
file_write.close()

'''
    important note:
        w Mode
        w existing file ke old content ko overwrite kar deta hai.
        w = Write + Old Data Replace
'''

print('----------------------')
print("for multiple lines write ")
file_write = open("_25filewrite.txt", "w")
file_write.write("Imam Mula Ali A.S\n")
file_write.write("Imam Mula Hasan A.S\n")
file_write.write("Imam Mula Hussain A.S\n")
file_write.close()

print('----------------------')
print('apend method in file handling ')
file_append=open('_25fileappend.txt','a')
for x in range(0,5):
    file_append.write("Imam Mula Ali A.S\n")
file_append.close()

print('----------------------')
'''
    x — Create Mode
    x ka use new file create karne ke liye hota hai.
    
'''
print("create the new file ")
# not : if file already exist karti ho tu error aye aye ga
file_create = open("_25newfile.txt", "x")
file_create.write("Hello Python")
file_create.close()

print('-----------------------')
print('the another best method ')
with open("_25fileread.txt", "r") as file:
    data = file.read()
    print(data)


print('------------------------')
print("Enter the student data  ")
while True:
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    city = input("Enter your city: ")
    question=input("if you enter another student data press enter other-wise type 'no' :")
    with open("_25student.txt", "a") as file:
        file.write(f"new student -----\n")
        file.write("\n")
        file.write(f"Name: {name.title()}\n")
        file.write(f"Age: {age.title()}\n")
        file.write(f"City: {city.title()}\n")
        file.write("\n")
    if question.lower()=='no':
        break

