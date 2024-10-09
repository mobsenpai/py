a = input("Enter a string: ")
rev = ""

# method: 1
# for x in range(len(a) - 1, -1, -1):
#     # print(a[x], end="")
#     rev = rev + a[x]
# print(rev)

# method 2:
for i in a:
    rev = i + rev
print(rev) 
