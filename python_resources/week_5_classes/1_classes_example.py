class Student:
    def __init__(self, name, grade_level):
        self.name = name
        self.grade_level = grade_level
        self.credits = 0

    def add_credits(self, n):
        self.credits += n

    def promote(self):
        self.grade_level += 1

    def summary(self):
        return f"{self.name} (grade {self.grade_level}) has {self.credits} credits."

# quick test
s = Student("Ari", 10)
s.add_credits(5)
print(s.summary())
s.promote()
print(s.summary())
