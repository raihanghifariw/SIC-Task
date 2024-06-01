# Indexing 2D Lists

list_array = [[1,2,3], 
            [4,5,6], 
            [7,8,9]]

print(list_array[0])
# Output: [1, 2, 3]

print(list_array[0][1])
# Output: 2

print(len(list_array))
# Output: 3

print(len(list_array[len(list_array) - 1]))
# Output: 3

index = len(list_array) - 1
element = list_array[index]  
# Output: 9
print('=========================================')

# Modifying lists
# list_array[0][1] = "A"
# Output: A

# 2D Lists dengan Single For Loop
for item in list_array:
    print('item =',item)
print('=========================================')

# 2D Lists dengan Double For Loop

for i in list_array:
    for j in i:
        print(j, end = ' ')
    print()
print('=========================================')

"""
for loop luar for i in list_array: mengakses kolom demi kolom dari seluruh lists ke variable i.
for loop dalam for j in i: mengakses seluruh elemen dari i dan mencetaknya ke console.
"""

list_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for item in list_array:
  if item == [1, 2, 3]:
    print("Hello!")
    continue
  print('item =', item)