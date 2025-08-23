n = int(input("Enter a number: "))

def fact(n):
    f=1
    for i in range(1, n+1):
       f=f*i
    return f 

r=fact(n)
print("FACT: ", r)
