n = input("Enter any value: ")

if n.isalpha():
    print("It is a character")
else:
    n = int(n)
    if n > 0:
        print("It is a positive number")
    elif n < 0:
        print("It is a negative number")
    else:
        print("It is zero")
