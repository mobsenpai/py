a = ["24", "04", "2024"]
# using for loop
a = [int(n) for n in a]
print(a)

# using map() func.
a = list(map(int, a))
print(a)
