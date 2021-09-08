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

# printing the list using for loops in a different way
# (credit to snakify's python tutorial!)
for row in list2:
    for elem in row:
        print(elem, end = ' ')
    print()

# creating and printing a dummy list that resembles the cgol board
list3 = [' ', '#', ' ', '#']
print(list3)

# doing the same with a list of lists
list4 = [['', '#', '', '#'], ['#', '', '#', '']]
print(list4)

# printing it
for row in list4: # somehow this version looks like what I want - it just prints the characters!
    for elem in row:
        print(elem, end = ' ')
    print()

# trying out something from a list comprehension tutorial
list5 = [] # creates empty list
for i in range(12):
    if i % 2 == 1: # if number is odd
        list5.append(i) # add odds to list
print(list5)
