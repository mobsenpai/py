n=int(input("Enter a number: "))

def prime(n):
    if (n<2):
        return 0
    else:
        for i in range(2,n,1):
            if(n%i==0):
                return 0
    return 1

r=prime(n)
if(r):
    print("Prime")
else:
    print("Not prime")
