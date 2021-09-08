# creating a list
list = [0, 0, 0, 0]
print(list)

# creating a list of lists
list2 = [[0, 0, 0, 0], [0, 0, 0, 0]]
print(list2)

# printing list using for loops
for i in range(len(list2)):
    for j in range(len(list2[i])):
        print(list2[i][j], end = ' ')
    print()
