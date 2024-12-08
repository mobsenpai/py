a = input("Enter any string: ")
b = input("Enter a character to search for: ")

count = 0

for x in a:
    if x == b:
        count += 1
print(count)        
