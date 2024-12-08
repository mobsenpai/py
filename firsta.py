a = input("Enter any string: ")

count = 0
while count <= len(a):
    if a[count] == "a":
        print("At index", count+1)
        break
    count+=1
