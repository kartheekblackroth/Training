# Day 3 - Magic Methods and Operator Overloading

# 1. __str__() - Returns a readable string for an object
# 2. __repr__() - Returns a developer-friendly representation
# 3. __len__() - Returns the length or count of an object
# 4. __eq__() - Compares two objects for equality
# 5. __lt__() - Checks whether one object is less than another
# 6. __gt__() - Checks whether one object is greater than another
# 7. __add__() - Defines the behavior of the + operator
# 8. __sub__() - Defines the behavior of the - operator


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.subjects = ["Python", "Math", "English"]

    def __str__(self):
        # Return student details in a readable format
        return f"Student Name: {self.name}, Marks: {self.marks}"

    def __repr__(self):
        # Return a developer-friendly representation of the object
        return f"Student('{self.name}', {self.marks})"

    def __len__(self):
        # Return the number of subjects studied by the student
        return len(self.subjects)

    def __eq__(self, other):
        # Compare the marks of two students
        if not isinstance(other, Student):
            return NotImplemented
        return self.marks == other.marks

    def __lt__(self, other):
        # Check whether this student's marks are lower
        if not isinstance(other, Student):
            return NotImplemented
        return self.marks < other.marks

    def __gt__(self, other):
        # Check whether this student's marks are higher
        if not isinstance(other, Student):
            return NotImplemented
        return self.marks > other.marks

    def __add__(self, other):
        # Add the marks of two students
        if not isinstance(other, Student):
            return NotImplemented
        return self.marks + other.marks

    def __sub__(self, other):
        # Find the difference between two students' marks
        if not isinstance(other, Student):
            return NotImplemented
        return self.marks - other.marks


# Create two Student objects to test the magic methods
student1 = Student("Ravi", 85)
student2 = Student("Anil", 75)


# 1. Test __str__()
print("--- __str__() Example ---")
print(student1)


# 2. Test __repr__()
print("\n--- __repr__() Example ---")
print(repr(student1))


# 3. Test __len__()
print("\n--- __len__() Example ---")
print("Number of subjects:", len(student1))


# 4. Test __eq__()
print("\n--- __eq__() Example ---")
print("Same marks:", student1 == student2)


# 5. Test __lt__()
print("\n--- __lt__() Example ---")
print("Ravi has fewer marks than Anil:", student1 < student2)


# 6. Test __gt__()
print("\n--- __gt__() Example ---")
print("Ravi has more marks than Anil:", student1 > student2)


# 7. Test __add__()
print("\n--- __add__() Example ---")
print("Total marks:", student1 + student2)


# 8. Test __sub__()
print("\n--- __sub__() Example ---")
print("Difference in marks:", student1 - student2)