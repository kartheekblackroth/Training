
# Day 2 - OOP Implementation in Python

# 1. Encapsulation
# Encapsulation combines data and methods inside a class.
# It controls access to the data and helps protect an object's internal state.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Keep balance inside the class.

    def deposit(self, amount):
        if amount <= 0:  # Validate the amount before updating the balance.
            print("Deposit amount should be greater than zero.")
            return

        # Update the private balance only after validating the amount.
        self.__balance += amount
        print(f"{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount should be greater than zero.")
        elif amount > self.__balance:  # Prevent withdrawing more than the available balance.
            print("Not enough balance.")
        else:
            # Deduct the amount only when sufficient balance is available.
            self.__balance -= amount
            print(f"{amount} withdrawn successfully.")

    def show_balance(self):
        print(f"{self.owner}'s balance: {self.__balance}")


print("\n--- Encapsulation ---")
# Create an account object and test deposit, withdrawal, and balance display.
account = BankAccount("Ravi", 2000)
account.deposit(500)
account.withdraw(300)
account.show_balance()


# 2. Single Inheritance
# A child class inherits properties and methods from one parent class.

class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def show_details(self):
        print(f"Employee: {self.name}, ID: {self.employee_id}")


class Developer(Employee):
    # Developer inherits Employee's constructor and show_details() method.
    def write_code(self):
        print(f"{self.name} is working on a Python task.")


print("\n--- Single Inheritance ---")
# Use both the inherited method and the Developer's own method.
developer = Developer("Anil", "E101")
developer.show_details()
developer.write_code()


# 3. Multiple Inheritance
# A child class inherits properties and methods from more than one parent class.

class ReportWriter:
    def create_report(self):
        print("Creating the weekly report.")


class EmailSender:
    def send_email(self):
        print("Sending the report by email.")


class ReportAssistant(ReportWriter, EmailSender):
    # Reuse methods from both parent classes.
    def finish_report(self):
        self.create_report()
        self.send_email()


print("\n--- Multiple Inheritance ---")
# One object can access methods inherited from both parent classes.
assistant = ReportAssistant()
assistant.finish_report()


# 4. Multilevel Inheritance
# A class inherits from a child class forming a chain of inheritance.

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}.")


class Staff(Person):
    def attend_meeting(self):
        print(f"{self.name} is attending the team meeting.")


class TeamLead(Staff):
    # TeamLead inherits methods through Staff from Person.
    def assign_task(self):
        print(f"{self.name} assigned a task to the team.")


print("\n--- Multilevel Inheritance ---")
# The TeamLead object can use methods from all three levels.
lead = TeamLead("Kiran")
lead.introduce()
lead.attend_meeting()
lead.assign_task()


# 5. Hierarchical Inheritance
# Multiple child classes inherit from a single parent class.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle started.")


class Car(Vehicle):
    # Car inherits the common vehicle details and start() method.
    def drive(self):
        print(f"Driving the {self.brand} car.")


class Bike(Vehicle):
    # Bike also inherits the common vehicle details and start() method.
    def ride(self):
        print(f"Riding the {self.brand} bike.")


print("\n--- Hierarchical Inheritance ---")
# Both child objects use the shared parent method and their own methods.
car = Car("Toyota")
bike = Bike("Honda")
car.start()
car.drive()
bike.start()
bike.ride()


# 6. Polymorphism and Method Overriding
# Polymorphism allows the same method call to behave differently based on the object that invokes it.

class Payment:
    def pay(self, amount):
        print(f"Processing payment of {amount}.")


class CardPayment(Payment):
    # Override the parent method with card-specific behavior.
    def pay(self, amount):
        print(f"Paid {amount} using a card.")


class UpiPayment(Payment):
    # Override the same parent method with UPI-specific behavior.
    def pay(self, amount):
        print(f"Paid {amount} using UPI.")


print("\n--- Polymorphism and Method Overriding ---")
# The same method call produces different results for different payment objects.
payment_methods = [CardPayment(), UpiPayment()]
for method in payment_methods:
    method.pay(750)


# 7. Method overloading using default arguments
# Python does not support traditional method overloading by signature.
# Default arguments let one method work with different numbers of inputs.
class Calculator:
    # Default values allow second and third arguments to be optional.
    def add(self, first, second=0, third=0):
        return first + second + third


print("\n--- Default Arguments ---")
# Call the same method with one, two, and three numbers.
calculator = Calculator()
print("One number:", calculator.add(10))
print("Two numbers:", calculator.add(10, 20))
print("Three numbers:", calculator.add(10, 20, 30))


# 8. Composition
# Composition is a design principle where one class contains an instance of another class.
# An object owns another object as part of its structure.

class Battery:
    def power_on(self):
        print("Battery is supplying power.")


class Laptop:
    def __init__(self, model):
        self.model = model
        # Create the Battery object inside Laptop to demonstrate composition.
        self.battery = Battery()

    def start(self):
        # Laptop uses its contained Battery object when starting.
        self.battery.power_on()
        print(f"{self.model} laptop is starting.")


print("\n--- Composition ---")
laptop = Laptop("ThinkPad")
laptop.start()


# 9. Aggregation
# Aggregation is a has-a relationship where one class contains a reference to another class.

class TeamMember:
    def __init__(self, name, role):
        self.name = name
        self.role = role


class Department:
    def __init__(self, department_name, member):
        self.department_name = department_name
        # Receive an existing TeamMember object instead of creating it here.
        self.member = member

    def show_member(self):
        print(
            f"{self.member.name} works as {self.member.role} "
            f"in {self.department_name}."
        )


print("\n--- Aggregation ---")
# Create the member independently, then pass the same object to Department.
member = TeamMember("Meena", "Tester")
department = Department("Software", member)
department.show_member()
