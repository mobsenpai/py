n1=int(input("Enter 1st number: "))
n2=int(input("Enter 2nd number: "))
c=int(input("1: add\n2: sub\n3: mult\n4: div"))

def calc(a,b,c):
    if (c==1):
        return a + b
    elif (c==2):
        return a - b
    elif (c==3):
        return a * b
    elif (c==4):
        return a / b
    else:
        return "Invalid"

r=calc(n1,n2,c)
print(r)
