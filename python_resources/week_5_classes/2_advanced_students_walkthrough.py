class Student:
    #Student record with basic info, schedule, and allergies.
    #Simpler version for teaching: assume inputs are valid.
    
    #this is unique info for the class, to help distinguish it from the other classes being used that are similar
    def __init__(self, name, student_id, grade, classes, allergies=None):
        self.name = name
        self.student_id = student_id
        self.grade = grade
        self.classes = classes  # list of 4 classes, in daily order
        self.allergies = allergies or []
        print(f"Student {self.name} created.")

    #we need to be able to add alergies to the list if something comes up
    def add_allergy(self, allergy):
        if allergy not in self.allergies:
            self.allergies.append(allergy)

    #if the student changes a class, we can manage their schedule here
    def swap_class(self, period_index, new_class):
        old = self.classes[period_index]
        self.classes[period_index] = new_class
        print(f"Swapped {old} → {new_class}")

    #here, so we can print off a receipt of who they are
    def receipt(self):
        print("-" * 40)
        print(" HELIX HIGH SCHOOL — STUDENT RECORD ")
        print("-" * 40)
        print(f"Name: {self.name}")
        print(f"ID:   {self.student_id}   Grade: {self.grade}")
        print(f"Allergies: {', '.join(self.allergies) if self.allergies else '(none)'}")
        print("\nDaily Schedule:")
        periods = ["Period 1 (8:00–9:20)", "Period 2 (9:30–10:50)",
                   "Period 3 (11:20–12:40)", "Period 4 (12:50–2:10)"]
        for i, course in enumerate(self.classes):
            print(f" {periods[i]:20} {course}")
        print("-" * 40)

    def __del__(self):
        #Destructor: pretend we’re removing from database.
        print(f"Student {self.name} (ID: {self.student_id}) has been deleted.")

def main():
    a = Student(
        name="John Smith",
        student_id="1234",
        grade=10,
        classes=["Algebra", "English", "Chemistry", "Intro to Programming"],
        allergies=["peanuts", "shellfish"]
    )

    #lets show their profile right now
    a.receipt()

    #lets make some changes now
    a.add_allergy("strawberries")
    a.swap_class(2, "Biology")

    #show the changes
    a.receipt()

    #the student doesnt go here anymore, time to delete
    del a

if __name__ == "__main__":
    main()
