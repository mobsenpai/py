a = input("Enter any string: ")

lista = a.split()
count = 0

for i in lista:
    if i.isalpha():
        count+=1

print(count)
