'''
Q1) Create a Vehicle class with max_speed and mileage instance
attributes
'''

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

car = Vehicle(220, 70)
print(car.max_speed, car.mileage)