# SOLID Principles in Python

# SOLID principles help developers create code that is
# maintainable, reusable, flexible, and easy to understand.


# ==========================================
# 1. SINGLE RESPONSIBILITY PRINCIPLE (SRP)
# ==========================================

# Concept:
# A class should have only one responsibility.

# Real-World Example:
# In a car rental company, one department manages car details,
# while another department generates rental bills.

# Explanation:
# Managing car details and generating bills are different tasks.
# If both responsibilities are placed in one class, changing
# the billing process may affect the car management code.
# By separating them into different classes, each class has
# one clear responsibility and can be maintained independently.

# Code:

class Car:
    def __init__(self, brand, model):
        # Store the car's brand and model
        self.brand = brand
        self.model = model


class RentalBilling:
    def generate_bill(self, days, rent_per_day):
        # Calculate the total rental amount
        total = days * rent_per_day

        # Display the rental bill
        print(f"Total Rental Bill: Rs.{total}")


# Create a car object
car = Car("Toyota", "Innova")
print(f"Car: {car.brand} {car.model}")

# Generate the rental bill using a separate class
billing = RentalBilling()
billing.generate_bill(3, 2000)


# ===================================
# 2. OPEN/CLOSED PRINCIPLE (OCP)
# ===================================

# Concept:
# Software entities should be open for extension but closed
# for modification.

# Real-World Example:
# A car rental company rents regular cars and luxury cars.
# The company may introduce new categories, such as electric
# cars, with different rental prices.

# Explanation:
# Each car category has its own pricing rule. Instead of
# modifying the existing rent calculation function every time
# a new category is introduced, we can create a new pricing
# class. This allows the system to support new categories
# without changing the existing calculation logic.

# Code:

from abc import ABC, abstractmethod


class RentalPricing(ABC):
    @abstractmethod
    def calculate_rent(self, days):
        # Every pricing class must implement this method
        pass


class RegularCarPricing(RentalPricing):
    def calculate_rent(self, days):
        # Calculate rent for a regular car
        return days * 2000


class LuxuryCarPricing(RentalPricing):
    def calculate_rent(self, days):
        # Calculate rent for a luxury car
        return days * 5000


class ElectricCarPricing(RentalPricing):
    def calculate_rent(self, days):
        # Calculate rent for an electric car
        return days * 3000


def calculate_total_rent(pricing, days):
    # Use the supplied pricing rule without modifying this function
    return pricing.calculate_rent(days)


# Calculate rental prices for different car categories
print("Regular Car Rent:", calculate_total_rent(RegularCarPricing(), 3))
print("Luxury Car Rent:", calculate_total_rent(LuxuryCarPricing(), 3))
print("Electric Car Rent:", calculate_total_rent(ElectricCarPricing(), 3))


# =========================================
# 3. LISKOV SUBSTITUTION PRINCIPLE (LSP)
# =========================================

# Concept:
# Objects of a child class should be usable wherever objects
# of their parent class are expected without breaking the program.

# Real-World Example:
# A car rental company offers sedans and SUVs.
# Both types of cars provide daily rental prices.

# Explanation:
# The booking system should be able to calculate the rent
# for either a sedan or an SUV using the same common method.
# Each car type follows the behavior defined by its parent
# class. Therefore, one car type can replace another without
# requiring changes to the booking function.

# Code:

class RentalCar(ABC):
    @abstractmethod
    def get_daily_rent(self):
        # Every rental car must provide its daily rental price
        pass


class Sedan(RentalCar):
    def get_daily_rent(self):
        # Return the daily rent for a sedan
        return 2500


class SUV(RentalCar):
    def get_daily_rent(self):
        # Return the daily rent for an SUV
        return 4000


def display_daily_rent(car):
    # This function works with any valid RentalCar object
    print("Daily Rent: Rs.", car.get_daily_rent())


# Use different car types with the same function
display_daily_rent(Sedan())
display_daily_rent(SUV())


# ===========================================
# 4. INTERFACE SEGREGATION PRINCIPLE (ISP)
# ===========================================

# Concept:
# A class should not be forced to implement methods
# that it does not need.

# Real-World Example:
# A car rental company has basic cars and GPS-enabled cars.
# Basic cars support renting, while GPS-enabled cars support
# both renting and navigation.

# Explanation:
# If one large interface requires every car to support
# navigation, basic cars would have to implement a feature
# they do not provide. By separating the renting and GPS
# interfaces, each car implements only the features it needs.
# This keeps the design simple and avoids unnecessary methods.

# Code:

class Rentable(ABC):
    @abstractmethod
    def rent_car(self):
        # Every rentable car must support renting
        pass


class GPSAvailable(ABC):
    @abstractmethod
    def navigate(self):
        # Only GPS-enabled cars need navigation
        pass


class BasicRentalCar(Rentable):
    def rent_car(self):
        # Rent a basic car
        print("Basic car rented successfully.")


class GPSRentalCar(Rentable, GPSAvailable):
    def rent_car(self):
        # Rent a GPS-enabled car
        print("GPS-enabled car rented successfully.")

    def navigate(self):
        # Start the car's navigation system
        print("GPS navigation started.")


# A basic car only implements the renting feature
basic_car = BasicRentalCar()
basic_car.rent_car()

# A GPS-enabled car implements both required features
gps_car = GPSRentalCar()
gps_car.rent_car()
gps_car.navigate()


# =========================================
# 5. DEPENDENCY INVERSION PRINCIPLE (DIP)
# =========================================

# Concept:
# High-level modules should depend on abstractions,
# not directly on low-level modules.

# Real-World Example:
# After a customer books a rental car, the company sends
# a confirmation through email or SMS.

# Explanation:
# The booking system should not be tightly connected to
# only an email service. It should depend on a common
# notification abstraction. Email and SMS services implement
# that abstraction, and the booking system receives the
# required service from outside. Therefore, the company can
# switch notification methods without changing the booking logic.

# Code:

class NotificationService(ABC):
    @abstractmethod
    def send_confirmation(self, message):
        # Every notification service must implement this method
        pass


class EmailNotification(NotificationService):
    def send_confirmation(self, message):
        # Send the booking confirmation through email
        print("Email Confirmation:", message)


class SMSNotification(NotificationService):
    def send_confirmation(self, message):
        # Send the booking confirmation through SMS
        print("SMS Confirmation:", message)


class CarRentalBooking:
    def __init__(self, notification_service):
        # Receive a notification service from outside
        self.notification_service = notification_service

    def book_car(self, car_model):
        # Create the booking confirmation message
        message = f"Your booking for {car_model} is confirmed."

        # Display the booking confirmation
        print(message)

        # Send the message using the supplied service
        self.notification_service.send_confirmation(message)


# Create a booking that uses email notifications
email_service = EmailNotification()
email_booking = CarRentalBooking(email_service)
email_booking.book_car("Toyota Innova")

# Switch to SMS without changing the booking class
sms_service = SMSNotification()
sms_booking = CarRentalBooking(sms_service)
sms_booking.book_car("Hyundai Creta")


# ==================================