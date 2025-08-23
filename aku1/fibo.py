n=10

a=0
b=1

# method 1
print(a,b)

for i in range(3, n):
    c=a+b
    print(c)
    a=b
    b=c
