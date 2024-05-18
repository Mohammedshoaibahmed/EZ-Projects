class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        """Adds a grade to the student's list of grades."""
        self.grades.append(grade)

    def calculate_average(self):
        """Calculates and returns the average grade of the student."""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_name(self):
        """Returns the name of the student."""
        return self.name

    def get_grades(self):
        """Returns the list of grades of the student."""
        return self.grades

# Create instances of the Student class
student1 = Student("Arun")
student2 = Student("Surya")
student3 = Student("Chandu")

# Add grades for each student
student1.add_grade(85)
student1.add_grade(92)
student1.add_grade(78)

student2.add_grade(88)
student2.add_grade(79)
student2.add_grade(95)

student3.add_grade(90)
student3.add_grade(85)
student3.add_grade(87)

# Create a list to store the student instances
students = [student1, student2, student3]

# Demonstrate adding grades and calculating averages
for student in students:
    print(f"Student: {student.get_name()}")
    print(f"Grades: {student.get_grades()}")
    print(f"Average Grade: {student.calculate_average():.2f}\n")
