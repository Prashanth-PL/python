from unittest import result


def sum(a, b):
    res = a + b
    return res
print("After Exit")
a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
result = sum(a, b)
print ("Res is : ", result)