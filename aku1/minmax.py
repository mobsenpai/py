a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))

def my_max(a,b,c):
    if(a>=b and a>=c):
        nmax=a
    elif(b>=a and b>=c):
        nmax=b
    else:
        nmax=c
    return nmax


def my_min(a,b,c):
    if(a<=b and a<=c):
        nmin=a
    elif(b<=a and b<=c):
        nmin=b
    else:
        nmin=c
    return nmin


nmax=my_max(a,b,c)
nmin=my_min(a,b,c)

print("MAX:", nmax)
print("MIN:", nmin)
