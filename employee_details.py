class Employee:
    def __init__(self, name, id, dept):
        self.name = name
        self.id = id
        self.dept = dept
    def display(self):
        print(self.name, self.id, self.dept)
emp1 = Employee("Yash", 12, "BCA")
emp1.display()
