f = open("demo.txt", "w")
f.write('''Hello world
How are you''')
f.close()
f = open("demo.txt", "r")
words = 0
chars = 0
lines = 0
for x in f:
    words = len(x.split()) + words
    chars = len(x) + chars
    lines +=1
print(words, chars, lines)

import os
os.remove("demo.txt")
