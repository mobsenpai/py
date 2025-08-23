text=input("Enter a string: ")
rev=""
for i in text:
    rev=i+rev
print("REV", rev)
print("REV", text[::-1])
