# 4. Python function to check whether a number falls within a given a range
def check_range(a, b, c):
    x = range(b, c)
    if a in x:
        print(str(a) + " is within the range of "+ str(range(b, c)))
    else:
        print(str(a) + " is not within the range of "+ str(range(b, c)))
check_range(2, 10, 20)