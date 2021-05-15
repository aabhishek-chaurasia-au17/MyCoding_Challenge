"""
1. The Apartment has the following attributes:
flats: list of all flats
builder_name: name of the builder who built the apartment
amneties: list of all amneties in the apartments
parking_spots: number of parking spots available
number_floors: number of floors in the building
maintenance_monthly: monthly maintenance to be paid to the society
has_elevator: True or False depending on whether the building has an elevator
num_stairs: Number of stairs in the building
fire_safety: True or False depending on whether the building has fire safety
certification.

2. The Apartment Object supports the following methods:
rent_flat(): Takes the first unrented flat from the list of flats and calls its

rent_out() function. To the returned value add 500 if the building has lift
facility and an extra 500 if fire safety measures are present. Add to this 500
for each of the amneties in the apartment and also adds the monthly societal
maintenance to return the final rent.

issue_parking_spot(): Issues a new parking spot if one is available

revoke_parking_spot(flat): takes a flat as input and revokes its parking
permissions and makes the new parking spot available.

"""
# from flat import *


class Apartment:
    def __init__(self, flats, builder_name, amneties, parking_spots, number_floors, maintenance_monthly, has_elevator, num_stairs, fire_safety):
        self.flats = flats
        self.builder_name = builder_name
        self.amneties = amneties
        self.parking_spots = parking_spots
        self.number_floors = number_floors
        self.maintenance_monthly = maintenance_monthly
        self.has_elevator = has_elevator
        self.num_stairs = num_stairs
        self.fire_safety = fire_safety

    def rent_flat(self):
        print("**********rent_flat***********")
        print(f"First flat is : Flat {self.flats[0]}")
        self.flats[0] = "Rented"
        return f"This flat is {self.flats[0]}"

    def rent_out(self):
        rent_amount = 5000
        if self.has_elevator == True:
            rent_amount += 500
        if self.fire_safety == True:
            rent_amount += 500
        print(rent_amount)
        a = len(self.amneties)
        rent_amount += 500 * a
        print(rent_amount)
        rent_amount += my_apartment.maintenance_monthly
        return f"Totat rent amount is {rent_amount}"

    def issue_parking_spot(self):
        if self.parking_spots > 0:
            print("Parking spot is available. ")
            self.parking_spots -= 1
            return self.parking_spots
        else:
            return "Parking spot is not available. "

    def revoke_parking_spot(self):
        flat_name = input("Please enter your flat name : ")
        if flat_name in self.flats:
            return f"Your parking spot is revoked and your spot is parking lot number {flat_name}"
        else:
            return "You are not allowed to park your vehicle here because you are not a flat member."


my_apartment = Apartment(['A', 'B', 'C'], "Abhishek", [ "Gym", "Park"], 5, 15, 4500, True, 250, True)

print(f"The list of all flats are : {my_apartment.flats}")
print(f"The name of the builder who built the apartment is {my_apartment.builder_name} ")
print(f"The list of all amneties in the apartments are {my_apartment.amneties} ")
print(f"The number of parking spots available are {my_apartment.parking_spots}")
print(f"The number of floors in the building are {my_apartment.number_floors}")
print(f"The monthly maintenance to be paid to the society is {my_apartment.maintenance_monthly}")
print(f"The building has an elevator? : {my_apartment.has_elevator}")
print(f"The number of stairs in the building are : {my_apartment.num_stairs}")
print(f"Whether the building has fire safety certification? : {my_apartment.fire_safety} ")

print(my_apartment.rent_flat())
print(my_apartment.rent_out())
print(my_apartment.rent_out())
print(my_apartment.issue_parking_spot())
print(my_apartment.revoke_parking_spot())
