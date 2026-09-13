# Base Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Derived Class
class Student(Person):
    def __init__(self, name, age, student_id):
        # Call the constructor of the base class
        super().__init__(name, age)
        self.student_id = student_id

    def display_student(self):
        # Call base class method
        self.display_info()
        print(f"Student ID: {self.student_id}")

# Create an object of Student
s1 = Student("Alice", 21, "STU12345")

# Call method
s1.display_student()
