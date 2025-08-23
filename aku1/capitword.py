text = input("Enter a string: ")
textarr = text.split(" ")
new=""

for i in textarr:
    word = i.capitalize()    
    new = new + " " +  word
print(new)
