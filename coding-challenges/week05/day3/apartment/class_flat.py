"""
1. The Flat has the following attributes:
bed_rooms: a list of all the bedrooms in the house, initialize as empty list
bath_rooms: a list of all the bathrooms in the house, initialize as empty list
kitchens: a list of all the kitchens in the house, initialize as empty list
owner_name: name of the flat owner, initialize as None
current_renter: name of the current renter, initialize as None

2. The Flat Object supports the following methods:
rent_out(): Checks if flat is already on rent, if not then it returns the rent
of the flat which is calculated as 5*carpet_area per month. Then it asks the
user whether they agree to pay that amount or not using input(), if they say
Y/Yes/yes then take another input() as their name and set the current_renter
attribute.
PS: carpet area of the flat is the sum of carpet area of all the rooms in the
house.
change_owner(): Takes a name as input from the user and changes the owner of the
flat to that person

"""
# from bedroom.my_bedroom import carpet_area

class Flat():
    def __init__(self,bed_rooms,bath_rooms,kitchens,owner_name,current_renter):
        self.bed_rooms = bed_rooms
        self.bath_rooms = bath_rooms
        self.kitchens = kitchens
        self.owner_name = owner_name
        self.current_renter = current_renter

    def rent_out(self):
        if self.current_renter == None:
            room_length = int(input("Please enter the length of the room : "))
            room_breadth = int(input("Please enter the breadth of the room : "))
            rent = 5*(room_length*room_breadth)
            print(f"The flat is ready for rent. Amount of the flat is : {rent}")
            user_input = input(f"Do you want to take this flat on rent in {rent} amount  :  ")
            if user_input == 'Y' or user_input == 'Yes' or user_input == 'yes':
                user_name = input("Please enter your name : ")
                self.current_renter = user_name
                return f"The renter of the flat is {self.current_renter}"
                

    def change_owner(self):
        name = input("Please enter the name of the owner. : ")
        self.owner_name = name
        return  f"The new owner name is {self.owner_name} "
    

my_flat = Flat([],[],[],None,None)

print(my_flat.change_owner())
print(my_flat.rent_out())

print(f"The list of all the bedrooms in the house are {my_flat.bed_rooms} ")
print(f"The list of all the bathroooms in the house are {my_flat.bath_rooms} ")
print(f"The list of all the kitchens in the house are {my_flat.kitchens} ")
print(f"The name of the flat owner is {my_flat.owner_name} ")
print(f"The name of the current renter is {my_flat.current_renter} ")

    


