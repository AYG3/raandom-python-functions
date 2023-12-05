#Program to create a lambda function that adds 10 to a given number passed on as arg, also create a lambda function that multiplies arg x with arg y and prints the result

check = lambda x: x+10
print(check(10))

check = lambda x, y: x * y
print(check(10, 20))


