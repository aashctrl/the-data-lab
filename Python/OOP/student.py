class Student:
    def __init__(self, name, grade, subject):
        self.name = name
        self.grade = grade
        self.subject = subject
    def __str__(self):
        return f"Name: {self.name}, Grade: {self.grade}, Subject: {self.subject}"

s1 = Student("Aditya", "A", "Maths")
s2 = Student("Sanvi", "B", "Science")
print(s1)
print(s2)
print(s2.grade)
