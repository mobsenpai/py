a = int(input("Enter your age: "));
if (a >= 18):
    print(f"Your age is {a}, and you are eligible to vote!")
elif (a == 17):
    print(f"Your age is {a}, you will be eligible to vote next year!")
elif (a == 16):
    print(f"Your age is {a}, you will be eligible to vote next to next year!")
else:
    print("You are not eligible to vote!")
print("EOC")
