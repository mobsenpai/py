content = [
    "Hello world\n"
    "How are you?\n"
]

f = open("demo.txt", "w")
for i in content:
    f.write(i)
f.close()

f = open("demo.txt", "r")
print(f.read())

import os
os.remove("demo.txt")
