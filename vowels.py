n = input("Enter any value: ")

if n.isalpha():
    if n == "a" or n == "e" or n == "i" or n == "o" or n == "u":
        print (f"{n} is a vowel")
    else:
        print(f"{n} is a consonant")
else:
    print(f"{n} is a number")
