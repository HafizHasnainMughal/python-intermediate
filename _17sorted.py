# Sort () Method in python
'''
    sorting method is uesd in list for ascenging or desending  values
    sort(reverse=False) by default hota hay
'''
print("------------")
print('sorted methos in python ')

color_names=['Red','Green','Yellow','Black','White','Blue','Purple']
print(f"before sort method {color_names}")

color_names.sort(reverse=False)
print(sorted(color_names))
# OR
print(f"after the sort method {color_names}")

print("------------")
data=[('Hassan','B',88),
      ('Ali','C',78),
      ('Ahmad','D',68),
      ('Abbas','A',98)
      ]
for x in data:
    print(x)
print("sorted the data  in the base of grade")
grade=lambda grade:grade[1]
data.sort(key=grade)
for x in data:
    print(x)

'''
    Note:
        in sort() many items in list by using sort(key=index_number) and used  lambda function 
        in Numbering reverse=True beacuse num is starting 0,1,2,3,4.........
'''

