#2. Write the python program to square and cube every number in a given list of integers using lambda

dlist = [2, 4, 6, 8, 10]
cube = lambda x: x ** 3
square = lambda y: y** 2

cube_list = list(map(cube, dlist))
square_list = list(map(square, dlist))

print("Cubed list : " + str(cube_list))
print("Squared list: " + str(square_list))