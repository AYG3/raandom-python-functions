
def factorial(a):
    num = 1
    for i in range(1, a+1):
        num = num * i
    print(num)

num1 = int(input("Enter your number: "))


factorial(num1)

