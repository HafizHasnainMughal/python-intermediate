# enumerate in python 
'''
    enumerate() kisi iterable ke har item ke saath
    uska index (position number) provide karta hai.

    syntex:
        enumerate(iterable, start=0)
'''

print("---------------------")
colour=['red','blue','black','yellow','pink','green']
for index,x in enumerate(colour,start=1):
    print(index,x)

print("---------------------")
numbers = [10, 20, 30]
result = list(enumerate(numbers))
print(result)

print("---------------------")
print("for find character in word ")
word='mughal'.title()
for index,y in enumerate(word,start=1):
    print(index,y)

