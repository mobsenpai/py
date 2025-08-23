text=input("Enter a string: ")

# method 1
# rev=text[::-1]
# if(text==rev):
#     print("Palind")
# else:
#     print("NOT Palind")


# method 2
i=0
for w in text:
    i=i+1
i=i-1
    
j=0
f=1
while(j<=i):
    if(text[j]!=text[i]):
        f=0
        break
    j=j+1
    i=i-1


if(f):
    print("Palindrome")
else:
    print("Not palindrome")
