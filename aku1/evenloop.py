n=20

def even(n):
    if(n%2==0):
        return 1
    else:
        return 0


for i in range(0,n+1):
    if(even(i)):
        print(i)
