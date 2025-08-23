temp=float(input("Enter temp value: "))
c=int(input("1: celcius\n2: farenheit\n"))
cf=0
fc=0
if(c==1):
    cf=(temp*9/5)+32
    print(f"{cf}")
elif(c==2):
    fc=(temp-32)*5/9
    print(f"{fc}")
else:
    print("Invalid choice")
