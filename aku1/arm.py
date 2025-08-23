n=int(input("Enter a number: "))
t=n
arm=0
while(t>0):
    r=t%10
    arm=(r*r*r)+arm
    t=t//10

if(arm==n):
    print("armstrong")
else:
    print("NOT")
