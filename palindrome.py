a = input("Enter any string: ")

# print(a[::-1])

# if a == a[::-1]:
#     print("Palindrome")
# else:
#     print("NOT a palindrome")


rev = ""

for i in a:
    rev = i + rev

if rev == a:
    print("Palindrome")
else:
    print("Not palindrome")
