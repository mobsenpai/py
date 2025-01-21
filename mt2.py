# # comparing length of strings
# str1 = "Hello world how are you"
# str2 = "Hello world"

# def compare_string(str1, str2):
#     if len(str1) > len(str2):
#         return str1
#     elif len(str1) <  len(str2):
#         return str2
#     else:
#         return "Equal"

# print(compare_string(str1, str2))


## slicing
# str = "Hello world"
# print(str[3:5]) # end value is not included
# print(str[-1:0:-1])

# # palindrome (1st method)
# def using_slice(str):
#     if str == str[::-1]:
#         return "Palindrome"
#     else:
#         return "Not Palindrome"
# print(using_slice("ded"))

# # palindrome (2nd method)
# # rev = "" # global variable, but can't modify inside function
# def using_loop(str):
#     rev = ""
#     for i in str:
#        # rev = i + rev # key error # cannot modify global variable like this
#        rev = i + rev
#     if str == rev:
#         return "Palindrome"
#     else:
#         return "Not Palindrome"
# print(using_loop("twin"))


# # string library functions
# # python has a rich collection of build-in methods for strings
# str = " Hello world how are   you?"
# print(str.upper())
# print(str.lower())
# print(str.capitalize())
# print(str.title()) # capitalize first character of each word
# print(str.strip()) # leading and trailing whitespace
# print(str.replace("o", "O", 1))
# print(str.split())
# print(str.isalpha())
# print(str.find("o"))
# print(str.count("o"))


# # dictionary
# test = {
#     "Name": "yashraj",
#     "Roll no": 12,
#     "Dept": "BCA",
#     "Day": "Monday"
# }

# print(test["Name"])
# print(len(test))
# test1 = dict(name = "pritam", age = 18, country = "India")
# print(type(test1))
# print(test.keys())
# print(test.values())
# test["Day"] = "Tuesday"
# print(test.values())
# print(test["Day"])
# print(test.get("Day"))
# print(test.items()) #list of tuples of key and value pairs
# for i,j in test.items():
#     print(i,j)


# # Sets
# # a = {} # just this will make dictionary
# # a = set({1,2, "hello", True})
# # b = dict(name="Yashraj", class = 12) # class is a keybord hence error
# # b = dict({
# #              "name": "yashraj",
# #              "class": "bca",
# #              "age": 12
# #          })
# # print(type(b))
# # print(b)

# # b = {1,2,3,4, "yashraj"}
# # print(type(b))
# # b.add("Check")
# # c = {"apple", "banana", "cherry", True, 1, 2}
# # b.update(c)
# # print(b)
# # print(c)
# # d = {1, 2, 3, 4, 5} # not actually random, so not a good example use strings for this
# # print(d)
# f = {1,2,3,4, "yashraj"}
# f.remove(4)
# f.discard("yashraj")
# f.pop() # remove random item
# print(f)


# Functions
# def name(para1):
    
#     def inner():
#         return "How are you?"
#     print(inner())

#     return para1
# print(name("Yash"))


# map(str.upper(), ["hello", "world"])

# def x():
#     return "Hello"

# y = x
# y1 = x()

# print(y)
# print(y1)

# print(x)
# print(y())

# a = "154"
# sum = 0
# for x in a:
#     sum = sum + int(x)**3
# if sum == int(a):
#     print("Armstrong")
# lambda


# modules
# import calculate_area
# calc = calculate_area.calcuate_area
# print(calc(3,3))


# exception handling
# try:
#     print(x)
# except:
#     print("Please provide x")


# file handling
# f = open("calculate_area.py")
# # print(f.read(5))
# print(f.readline())
# # print(f.readline())
# # for x in f:
# #     print(x)

# f.close()

# f = open("demo.txt", "w")
# f.write("Overwrite the file")
# f.close()
# f = open("demo.txt", "a")
# f.write("\nNew lines added")
# f.write("\nNew New line added")
# f.close()

# f = open("demo.txt", "r")
# print(f.read())

# f.close()

# f = open("created_file.txt", "w")
# f.write("Hello world")
# f.close()
# f = open("created_file.txt", "r")
# print(f.read())


# import os
# os.remove("demo.txt")
# os.remove("created_file.txt")
