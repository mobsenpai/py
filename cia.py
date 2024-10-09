### Exam practices
## Bitwise Operators
# a = 5
# b = 10
# print(a & b)
# print(a | b)
# print(~a)


## DA, HRA, MA
# # Accepting basic salary from user
# basic_salary = float(input("Enter the basic salary: "))

# # Fixed values for DA, HRA, and MA
# DA = basic_salary * 0.2  # Example: 20% of basic salary
# HRA = basic_salary * 0.3  # Example: 30% of basic salary
# MA = 2000                 # Fixed medical allowance

# # Calculate gross salary using operators
# gross_salary = basic_salary + DA + HRA + MA  # Using + operator

# # Output the result
# print("Gross Salary:", gross_salary)

## factorial
# n = 5
# f = 1
# for i in range(1, n+1):
#     f = f * i
# print(f)


## reverse
# n = "1234"
# rev = ""
# for i in n:
#     rev = i + rev
# print(rev)

# n = "1234"
# for i in range(len(n) -1, -1, -1):
#     print(n[i], end="")


## armstrong numbers
# n = "152"
# arm = 0
# for i in n:
#     arm = arm + int(i) ** 3
# if arm == int(n):
#     print(f"{n} is an armstrong number")
# else:
#     print(f"{n} is not an armstrong number")
# print(arm)

## lcm & hcf
# n1 = 12
# n2 = 15
# n3 = 20

# a,b,c = n1,n2,n3

# while b:
#     a, b = b, a%b
# hcf = a

# while c:
#     hcf, c = c, hcf % c

# print(hcf)

# lcm = (n1 * n2) // hcf
# lcm1 = (lcm * n3) // hcf

# print(lcm1)


# n = "hello how are you?"
# ns = n.split() # ['1234']
# print(ns)
# nl = list(n)
# print(nl)
# print(sum(nl))


# l = [[1,2,3], [2,3,4], [4,5,6]]
# print(l[0], type(l[0]))
# print(sum(l[0]))


# n = 4
# sum = 0
# count = 1
# while count <= n:
#     sum = sum + count
#     count +=1
# print(sum)


# n = int(input("Enter a number: "))

# while n != 7:
#     n = int(input("Enter a number: "))
# print("Loop successfully exited")


# n = 4
# f = 1
# count = 1
# while count <= n:
#     f = f * count
#     count += 1
# print(f)


n = 11
count = 2
while count <= n:
    if n == 0 or n == 1:
        print("not prime")
    elif n % count == 0:
        print("not prime")
        break
    else:
        print(f"The number {n} is a prime number")
        break
    count += 1
    
