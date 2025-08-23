n = int(input("Enter a number: "))

def fact(n):
    if (n>1):
        return n * fact(n-1)
    else:
        return 1

print("FACT:", fact(n))
