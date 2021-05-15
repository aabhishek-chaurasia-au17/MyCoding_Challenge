"""
1. The Kitchen has the following attributes:
length: length of the bed in feet
breadth: breadth of the bed in feet
slab_material: whether the slab is granite, wood, marble and so on.
has_sink: True or False depending on whether the kitchen has a sink or not
has_slab: True or False depending on whether the kitchen has a slab or not
furnishing_material: whether the material is wood, steel, plywood and so on.
lpg_pipeline: True or False depending on whether the kitchen has an LPG pipeline
or not.

2. The Kitchen Object supports the following methods:
cook(): Checks if lpg connection, slab and sink exist and returns “Kitchen can
be used for cooking” .
"""


class Kitchen():
    def __init__(self, length, breadth, slab_material, has_sink, has_slab, furnishing_material, lpg_pipeline):
        self.length = length
        self.breadth = breadth
        self.slab_material = slab_material
        self.has_sink = has_sink
        self.has_slab = has_slab
        self.furnishing_material = furnishing_material
        self.lpg_pipeline = lpg_pipeline


    def cook(self):
        if self.lpg_pipeline == True and self.has_slab == True and self.has_sink == True:
            return "Kitchen can be used for cooking."
        else:
            return "Kitchen cannot be used for cooking."


my_kitchen = Kitchen(40,30,"Sandstone",True,True,"Plywood",True)


print(f"The length of the kitchen is {my_kitchen.length} ft")
print(f"The breadth of the kitchen is {my_kitchen.breadth} ft")
print(f"The slab material of the kitchen is  : {my_kitchen.slab_material} ")
print(f"The kitchen has a sink : {my_kitchen.has_sink} ")
print(f"The kitchen has a slab : {my_kitchen.has_slab} ")
print(f"The furniture materiial of the kitchen is : {my_kitchen.furnishing_material} ")
print(f"The kitchen has a lpg pipeline : {my_kitchen.lpg_pipeline} ")

print(my_kitchen.cook())







