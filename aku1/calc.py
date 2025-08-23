a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("1: add\n2: sub\n3: mult\n4: div\n"))

if(c==1):
    print(f"{a} + {b} = {a+b}")
elif(c==2):
    print(f"{a} - {b} = {a-b}")
elif(c==3):
    print(f"{a} * {b} = {a*b}")
elif(c==4):
    print(f"{a} / {b} = {a/b}")
else:
    print("Invalid input")
