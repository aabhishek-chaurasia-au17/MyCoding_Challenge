# 1. The Bed Object has the following attributes:
# length: length of the bed in feet
# breadth: breadth of the bed in feet
# year_made: Year in which the bed was made
# has_headboard: True or False depending on whether the bed has a headboard or not
# has_posts: True or False depending on whether the bed has sideposts or not
# material: material is wood, steel, plywood and so on.

class Bed:
    def __init__(self, length_in_feet, breadth_in_feet, year_made, headboard, sideposts, meterial):
        self.length = length_in_feet
        self.breadth = breadth_in_feet
        self.year_made = year_made
        self.has_headboard = headboard
        self.has_posts = sideposts
        self.meterial = meterial

a = Bed(6.6, 6.0, 2021, True, True, "PlyWood")

print(f"Lenth in feet : {a.length}")
print(f"Breadth in feet : {a.breadth}")
print(f"Year of Made : {a.year_made}")
print(f"Has Head board True or False \n {a.has_headboard}")
print(f"Has Posts True or False \n {a.has_posts}")
print(f"Meterial Type : {a.meterial}")