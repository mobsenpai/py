text=input("Enter a string: ")

count = 0
# 1st method
# for i in text:
#     if i== " ":
#         count = count +1

# print(count)

textarr=text.split(" ")

for i in textarr:
    if i.isalpha():
        count = count + 1

print(count)
