"""
1. The Bathroom Object has the following attributes:
length: length of the closet in feet
breadth: breadth of the closet in feet
has_sink: True or False depending on whether the bathroom has a slab or not
has_bathtub: True or False depending on whether the bathroom has a bathtub or not
has_tap: True or False depending on whether the bathroom has a tap or not
has_shower: True or False depending on whether the bathroom has a shower or not

2. The Bathroom Object supports the following methods:
bathing(): checks if atleast any one of the tap, shower or sink are available
and returns “Suitable for bathing”, if not available it returns “Unsuitable for
bathing”

"""

class Bathroom():

    def __init__(self, length, breadth, has_sink, has_bathtub, has_tap, has_shower):
        self.length = length
        self.breadth = breadth
        self.has_sink = has_sink
        self.has_bathtub = has_bathtub
        self.has_tap = has_shower
        self.has_shower = has_shower
    
    def bathing(self):
        if self.has_sink == True or self.has_tap == True or self.has_shower == True:
            return "Suitable for bathing. "
        else:
            return "Unsuitable for bathing. "
    
my_bathroom = Bathroom(20,15,True,True,True,True)


print(f"The length of the bathroom is {my_bathroom.length} ft")
print(f"The breadth of the bathroom is {my_bathroom.breadth} ft")
print(f"The bathroom has a slab : {my_bathroom.has_sink} ")
print(f"The bathroom has a bathtub : {my_bathroom.has_bathtub} ")
print(f"The bathroom has a shower : {my_bathroom.has_shower} ")

print(my_bathroom.bathing())



