n=int(input("Enter a number: "))

def div(n):
    if (n%2==0 and n%3==0):
        return 1
    else:
        return 0

r=div(n)
if(r):
    print(f"{n} is divisible by 2 and 3")
else:
    print(f"{n} is not divisible by 2 and 3")
