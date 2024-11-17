student = (12, "yash", "raj", 19)

course1 = set({})

grades = dict({})

for i in range(1,6):
    courses = input(f"Enter course: {i} ")
    course1.add(courses)

for i in course1:
    marks = int(input(f"Enter marks of: {i} "))
    grades.update({i : marks})

# avg of grades
avg = sum(grades.values())/ len(grades)

# printing all info
print(f"ID: {student[0]}")
print(f"First Name: {student[1]}")
print(f"Last Name: {student[2]}")
print(f"Age: {student[3]}")
for i, j in grades.items():
    print(f"Course Erolled: {i}, Marks obtained: {j}")
print(f"Average marks obtained: {avg}")
