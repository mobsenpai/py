n=int(input("Enter a number: "))

def oddeven(n):
    if(n%2==0):
        return "Even"
    else:
        return "Odd"


print(f"{n} is {oddeven(n)}")
