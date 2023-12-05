#3. Python function to find d maximum of 3 numbers

def max(a, b, c):
    if(a>b & a>c):
        print("The maximmum no: " ,a)
    elif(b>a & b>c):
        print("The maximmum no: " ,b)
    else:
        print("The maximum no: ", c)
max(2,4,6)