#  for loop 
'''
syntax:
for data in range (argument)
statement
         
'''

for i in range (5):
    print("The value is : ", i)
print("**************************")
for j in range (1, 5):
    print(" The value is : ", j)
print("***************************")
for k in range (1, 10, 2):
    print("The value is : ", k)
print("****************************")

print("------------------------------------------------------------")


sum = 0 
for i in range (10):
    sum = sum + i
    print(sum)
print (" EXIT FROM LOOP ")

print("-----------------------END OF FOR LOOP PY---------------------------------")

#  while loop

'''
initialization
while condition:
    statement
    updation / modification
'''

i = 0
while i < 0:
    print(" i is : ", i)
    i = i + 1
print("After exit from loop")

print("----------------------------------------------------------------------")


sum = 0
i = 0 
while i < 10:
    sum = sum + 1
    print(sum)
    i = i + 1
print ("Exit from the loop")

print("---------------------END OF WHILE LOOP PY-----------------------------------------")


# Nested loop

for i in range (1, 5 ):
    for j in range (3):
        print(" i is : ", i , "\n j is : ", j)
print(" EXIT FROM NESTED LOOP ")

print("-----------------------------END OF NESTED PY---------------------------------")

# while nested loop.py

x = 0
y = 0
while x < 5 :
    y = 0
    while y < 3:
        print(" x is : ", x ,"\n y is : ",y )
        y = y + 1
        x = x + 1

print("---------------------------END OF WHILE NESTED PY-----------------------------------------")


#  Break py

for i in range (1, 6):
    if i == 3:
        break
    print(" i is : ", i)

print("--------------------------END OF BREAK PY------------------------------------------------")


#  Continue py

for i in range (1, 6 ):
    if i == 3:
        continue
    print(" i is : ", i)


print("-----------------------END OF CONTINUE PY-------------------------------------")


#  Pass py

for i in range (1, 100):
    pass

print("----------------END OF PASS PY----------------------------")



#  Sum of given number py

num = int(input("Enter a number : "))
sumn = 0
rem = 0
while num > 0:
    rem = num % 10
    sumn = sumn + rem
    num = num // 10
print(" Sum of given number is : ", sum )

print("-------------------------END OF SUM OF GIVEN NUMBER -----------------------")


#  Pattern py

for i in range (1, 6):
    for j in range (i):
        print ("*", end = " ")
    print("\n")

print("-----------------END OF PATTERN PY-------------------------")