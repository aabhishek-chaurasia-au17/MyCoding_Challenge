"""
1. The Bed Object has the following attributes:
length: length of the bed in feet
breadth: breadth of the bed in feet
year_made: Year in which the bed was made
has_headboard: True or False depending on whether the bed has a headboard or not
has_posts: True or False depending on whether the bed has sideposts or not
material: material is wood, steel, plywood and so on.
2. The Bed Object does not support any following methods

"""

class Bed(): # Beds class made with followings attributes
    def __init__(self,length,breadth,year_made,has_headboard,has_posts,material):
        self.length = f"The length of the bed in feet is : {length} feet "
        self.breadth = f"The breadth of the bed in feet is {breadth} feet "
        self.year_made = f"The bed is made in the year of : {year_made} " 
        self.has_headboard = f"This bed has headboard : {has_headboard} "
        self.has_posts = f"This bed has posts : {has_posts} "
        self.material = f"The materials that use to make the bed is : {material}"

my_bed = Bed(10,5,2015,True,False,'Wood')

# for checking just uncomment below lines

print(my_bed.length)
print(my_bed.breadth)
print(my_bed.year_made)
print(my_bed.has_headboard)
print(my_bed.has_posts)
print(my_bed.material)
