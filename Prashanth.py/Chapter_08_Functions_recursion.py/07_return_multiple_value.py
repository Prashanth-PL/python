def  calculation(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    return add, sub, mul
a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
add, sub, mul, = calculation(a, b)
print("Addition is :", add)
print("Substraction is : ", sub)
print("Multiplication : ", mul)
