class Teacher():
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
class Sports():
    def __init__(self, sport):
        self.sport = sport
class SportsTeacher(Teacher, Sports):
    def __init__(self, name, subject, sport):
        Teacher.__init__(self, name, subject)
        Sports.__init__(self,sport)
    def display_info(self):
        print(self.name, self.subject, self.sport)
p1 = SportsTeacher("Yash", "PHE", "Football")
p1.display_info()
