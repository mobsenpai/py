# class Teacher:
#     def __init__(self, name, subject):
#         self.name = name
#         self.subject = subject

# class Sports:
#     def __init__(self, sport):
#         self.sport = sport

# class SportsTeacher(Teacher, Sports):
#     def __init__(self, name, sport):
#         self.name = name
#         self.sport = sport
#     def display(self):
#         print(self.name)
#         print(self.sport)


# cricketCoach = SportsTeacher("Sunil Singh", "Cricket")
# cricketCoach.display()


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

class Sports:
    def __init__(self, sport):
        self.sport = sport

class SportsTeacher(Teacher, Sports):
    def __init__(self, name, subject, sport):
        Teacher.__init__(self, name, subject)
