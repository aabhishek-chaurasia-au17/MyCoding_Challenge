"""
1. The Closet Object has the following attributes:
length: length of the closet in feet
breadth: breadth of the closet in feet
height: breadth of the closet in feet
max_capacity: Total number of items that a closet supports
items: The list of items in the closet. [All strings]
2. The Closet Object supports the following methods:
store_item(): Takes a string as input and adds it to the items list
fetch_item(): Returns the frontmost object in the items list

"""

class Closet():

    def __init__(self, length, breadth, height, max_capacity, items):
        self.length = f"The length of the closet in feet is {length} feet "
        self.breadth = f"The breadth of the closet in feet is {breadth} feet "
        self.height = f"The height of the closet in feet is {height} feet "
        self.max_capacity = f"Total number of items that this closet supports is : {max_capacity} "
        self.items = items
    
    def store_item(self):
        new_item = input("Please enter an item : ")
        self.items.append(new_item)
        return self.items
    
    def fetch_item(self):
        return self.items[0]



my_closet = Closet(6,5,12,25,['Bottle','Pants','Shirts','Keys','Bedsheet'])



print(my_closet.length)
print(my_closet.breadth)
print(my_closet.height)
print(my_closet.max_capacity)
print(my_closet.items)

print(my_closet.store_item())
print(my_closet.fetch_item())
