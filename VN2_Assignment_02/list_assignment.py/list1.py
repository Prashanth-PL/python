# Traversing the elements of list
#  by using while loop

print("************TRAVERSING BY USING WHILE LOOP*************")

list1 = [3, 8, 52, 78, 6, 12]
length = len(list1)
i = 0
while i < length:
    print(list1[i])
    i += 1


print("*************TRAVERSING BY FOR LOOP*****************")


# by using for loop

list2 = [1, 9, 5, 6, 7, 3]
for i in list1:
    print(i)


print("***************DISPLAY EVEN NUMBERS****************")


# To Display only even numbers

l1 = [2, 5, 3, 8, 6, 10, 20, 7, 55, 7, 30, 22]
for num in l1:
    if num %2 ==0:
        print(num, end = ' ')
    

