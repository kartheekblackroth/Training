# Task 6: OOP Coding Challenges
# File Name: coding_challenges.py


# ============================================================
# 1. STUDENT CLASS
# ============================================================

class Student:
    def __init__(self, name, roll_number, marks):
        # Initialize student details
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_details(self):
        # Display student information
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")


print("\n--- 1. Student Class ---")
student = Student("Rahul", 101, 85)
student.display_details()


# ============================================================
# 2. BANK ACCOUNT CLASS
# ============================================================

class BankAccount:
    def __init__(self, account_holder, balance=0):
        # Initialize account holder and balance
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        # Deposit money if the amount is positive
        if amount > 0:
            self.balance += amount
            print(f"Deposited: Rs.{amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        # Withdraw money if sufficient balance is available
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: Rs.{amount}")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        # Display the current balance
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: Rs.{self.balance}")


print("\n--- 2. Bank Account Class ---")
account = BankAccount("Rahul", 5000)
account.deposit(2000)
account.withdraw(1000)
account.display_balance()


# ============================================================
# 3. EMPLOYEE MANAGEMENT
# ============================================================

class Employee:
    def __init__(self, employee_id, name, salary):
        # Store employee information
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    def display_details(self):
        # Display employee information
        print(
            f"ID: {self.employee_id}, "
            f"Name: {self.name}, Salary: Rs.{self.salary}"
        )


class EmployeeManagement:
    def __init__(self):
        # Store all employees in a list
        self.employees = []

    def add_employee(self, employee):
        # Add an employee to the list
        self.employees.append(employee)
        print(f"{employee.name} added successfully.")

    def display_employees(self):
        # Display all employees
        for employee in self.employees:
            employee.display_details()


print("\n--- 3. Employee Management ---")
manager = EmployeeManagement()
manager.add_employee(Employee(1, "Anil", 30000))
manager.add_employee(Employee(2, "Priya", 35000))
manager.display_employees()


# ============================================================
# 4. VEHICLE INHERITANCE
# ============================================================

class Vehicle:
    def __init__(self, brand, model):
        # Initialize common vehicle details
        self.brand = brand
        self.model = model

    def display_details(self):
        # Display vehicle information
        print(f"Brand: {self.brand}, Model: {self.model}")


class Car(Vehicle):
    def __init__(self, brand, model, doors):
        # Reuse the parent class constructor
        super().__init__(brand, model)
        self.doors = doors

    def display_details(self):
        # Display car-specific information
        super().display_details()
        print(f"Number of Doors: {self.doors}")


class Bike(Vehicle):
    def __init__(self, brand, model, engine_capacity):
        # Reuse the parent class constructor
        super().__init__(brand, model)
        self.engine_capacity = engine_capacity

    def display_details(self):
        # Display bike-specific information
        super().display_details()
        print(f"Engine Capacity: {self.engine_capacity} cc")


print("\n--- 4. Vehicle Inheritance ---")
car = Car("Toyota", "Innova", 4)
car.display_details()

bike = Bike("Honda", "Shine", 125)
bike.display_details()


# ============================================================
# 5. SHAPE AREA CALCULATOR
# ============================================================

import math


class Shape:
    def area(self):
        # Base method to be implemented by child classes
        raise NotImplementedError("Subclasses must implement area().")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        # Calculate rectangle area
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Calculate circle area using pi * radius squared
        return math.pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        # Calculate triangle area
        return 0.5 * self.base * self.height


print("\n--- 5. Shape Area Calculator ---")
print("Rectangle Area:", Rectangle(10, 5).area())
print("Circle Area:", round(Circle(7).area(), 2))
print("Triangle Area:", Triangle(10, 6).area())


# ============================================================
# 6. SHOPPING CART
# ============================================================

class Product:
    def __init__(self, name, price):
        # Store product details
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        # Create an empty shopping cart
        self.items = []

    def add_item(self, product):
        # Add a product to the cart
        self.items.append(product)
        print(f"{product.name} added to cart.")

    def remove_item(self, product_name):
        # Remove the first matching product
        for product in self.items:
            if product.name == product_name:
                self.items.remove(product)
                print(f"{product_name} removed from cart.")
                return
        print(f"{product_name} not found in cart.")

    def calculate_total(self):
        # Calculate the total price of all products
        return sum(product.price for product in self.items)

    def display_items(self):
        # Display cart items and the total amount
        for product in self.items:
            print(f"{product.name}: Rs.{product.price}")
        print(f"Total: Rs.{self.calculate_total()}")


print("\n--- 6. Shopping Cart ---")
cart = ShoppingCart()
cart.add_item(Product("Keyboard", 1000))
cart.add_item(Product("Mouse", 500))
cart.display_items()
cart.remove_item("Mouse")
cart.display_items()


# ============================================================
# 7. MOVIE RATING SYSTEM
# ============================================================

class Movie:
    def __init__(self, title):
        # Initialize movie title and ratings list
        self.title = title
        self.ratings = []

    def add_rating(self, rating):
        # Accept ratings only between 1 and 5
        if 1 <= rating <= 5:
            self.ratings.append(rating)
            print(f"Rating {rating} added for {self.title}.")
        else:
            print("Rating must be between 1 and 5.")

    def average_rating(self):
        # Calculate the average rating
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)

    def display_rating(self):
        # Display the movie's average rating
        print(f"Movie: {self.title}")
        print(f"Average Rating: {self.average_rating():.2f}/5")


print("\n--- 7. Movie Rating System ---")
movie = Movie("RRR")
movie.add_rating(5)
movie.add_rating(4)
movie.add_rating(5)
movie.display_rating()


# ============================================================
# 8. HOSPITAL PATIENT RECORDS
# ============================================================

class Patient:
    def __init__(self, patient_id, name, age, diagnosis):
        # Store patient information
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.diagnosis = diagnosis

    def display_record(self):
        # Display the patient's medical record
        print(f"Patient ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Diagnosis: {self.diagnosis}")


class Hospital:
    def __init__(self):
        # Store patient records
        self.patients = []

    def add_patient(self, patient):
        # Add a patient record
        self.patients.append(patient)
        print(f"Patient {patient.name} added successfully.")

    def search_patient(self, patient_id):
        # Find a patient using the patient ID
        for patient in self.patients:
            if patient.patient_id == patient_id:
                patient.display_record()
                return
        print("Patient not found.")


print("\n--- 8. Hospital Patient Records ---")
hospital = Hospital()
hospital.add_patient(Patient(101, "Ravi", 35, "Fever"))
hospital.add_patient(Patient(102, "Meena", 28, "Cold"))
hospital.search_patient(101)


# ============================================================
# 9. SCHOOL RESULT PROCESSING
# ============================================================

class SchoolResult:
    def __init__(self, student_name, marks):
        # Store student name and subject marks
        self.student_name = student_name
        self.marks = marks

    def calculate_total(self):
        # Calculate total marks
        return sum(self.marks)

    def calculate_average(self):
        # Calculate average marks
        if not self.marks:
            return 0
        return self.calculate_total() / len(self.marks)

    def calculate_grade(self):
        # Assign a grade based on average marks
        average = self.calculate_average()

        if average >= 90:
            return "A"
        elif average >= 75:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 40:
            return "D"
        else:
            return "Fail"

    def display_result(self):
        # Display the student's result
        print(f"Student: {self.student_name}")
        print(f"Total Marks: {self.calculate_total()}")
        print(f"Average: {self.calculate_average():.2f}")
        print(f"Grade: {self.calculate_grade()}")


print("\n--- 9. School Result Processing ---")
result = SchoolResult("Rahul", [85, 90, 78, 88, 92])
result.display_result()


# ============================================================
# 10. ONLINE COURSE MANAGEMENT
# ============================================================

class Course:
    def __init__(self, course_id, title, instructor):
        # Store course information
        self.course_id = course_id
        self.title = title
        self.instructor = instructor
        self.students = []

    def enroll_student(self, student_name):
        # Enroll a student if not already enrolled
        if student_name not in self.students:
            self.students.append(student_name)
            print(f"{student_name} enrolled in {self.title}.")
        else:
            print(f"{student_name} is already enrolled.")

    def display_course(self):
        # Display course details and enrolled students
        print(f"Course ID: {self.course_id}")
        print(f"Course: {self.title}")
        print(f"Instructor: {self.instructor}")
        print(f"Enrolled Students: {', '.join(self.students) or 'None'}")


print("\n--- 10. Online Course Management ---")
course = Course(201, "Python Programming", "Mr. Kumar")
course.enroll_student("Rahul")
course.enroll_student("Priya")
course.display_course()


# =====================================