# existing file
# f = open("demo.txt", "w")
# f.write("Hello world")
# f.close()

# appending to existing file
f = open("demo.txt", "a")
f.write("new line")
f.close()

f = open("demo.txt", "r")
print(f.read())

# import os
# os.remove("demo.txt")
