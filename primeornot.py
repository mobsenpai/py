num = int(input("Enter the number here: "))
# Negative numbers, 0 and 1 are not primes
if num > 1:
  
    # Iterate from 2 to n // 2
    for i in range(2, (num//2)+1):
      
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


# NOTE: in the range 2//2 gives 1 and 2//2+1 gives 2 hence is 2 in range 2 
# excluding 2, so its gets false and the loop doesn't continue for 2 and gives 
# the else value
