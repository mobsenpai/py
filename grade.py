grade = input("Enter a grade(A,B,C,D,F): ")
grade = grade.capitalize()

if grade == "A":
    print("Excellent")
elif grade == "B":
    print("Good")
elif grade == "C":
    print("Satisfactory")
elif grade == "D":
    print("Pass")
elif grade == "F":
    print("Fail")
else:
    print("Please enter the grade correctly i.e one of A, B, C, D, or F")
