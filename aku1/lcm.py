a=int(input("Enter 1 number: "))
b=int(input("Enter 2 number: "))
c=int(input("Enter 3 number: "))

max=a

if(a>=b and a>=c):
    max=a
elif(b>=a and b>=c):
    max=b
elif(c>=a and c>=b):
    max=c

while(max%a!=0 or max%b!=0 or max%c!=0):
    max+=1

print("LCM:", max)
