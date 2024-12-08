a = str(input("Enter any string: "))

vowels = "aeiouAEIOU"
total = 0

for i in a:
    if i in vowels:
        total+=1
print(total)
