# 1. The Closet Object has the following attributes:
# length: length of the closet in feet
# breadth: breadth of the closet in feet
# height: breadth of the closet in feet
# max_capacity: Total number of items that a closet supports
# items: The list of items in the closet. [All strings]
# 2. The Closet Object supports the following methods:
# store_item(): Takes a string as input and adds it to the items list
# fetch_item(): Returns the frontmost object in the items list

class Closet:
    def __init__(self, length, breadth, height, capacity, items):
        self.length = length
        self.breadth = breadth
        self.height = height
        self.max_capacity = capacity
        self.items = items

                
    def store_item(self):
        a = input("PLease enter an item : ")
        self.items.append(a)
        return self.items

    def fetch_item(self):
        return self.items[0]


b = Closet(6.0, 4.0, 7, 2600, ['laptop','bottle','glass'])

print(f"length of the closet in feet : {b.length}")
print(f"breadth of the closet in feet : {b.breadth}")
print(f"breadth of the closet in feet : {b.height}")
print(f"Total number closet supports : {b.max_capacity}")
print(b.store_item())
print(b.fetch_item())
