# check given word is palindrome or not


l1 = ["word", "eye", "level", "wow", "abhishek", "nayana"]
result = list(filter(lambda x: (x == "".join(reversed(x))), l1))
print(result)


word = input("Enter the character :")
if word == word[::-1]:
    print("The string is Palindrome")
else:
    print("Not palindrome")