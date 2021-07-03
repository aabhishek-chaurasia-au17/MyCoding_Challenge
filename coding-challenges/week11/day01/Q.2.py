"""
Q-2 )Trapping Rain Water (7.5 marks)
https://leetcode.com/problems/trapping-rain-water/
(Hard)
Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it can trap after raining.
Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by
array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are
being trapped.
Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
(Hint: solve using stacks to precompute L and R list, of max element on right and
max element on left, respectively, for each element. Use formula
min(max_height_Right,max_height_Left)-current_height to get water level.
Use logic of just greatest element on the right question discussed on friday night
class)
"""


def TrappingWater(height):
 
        if len(height)<= 2:
            return 0
        
        ans = 0
        
        i = 1
        j = len(height) - 1
        
        lmax = height[0]
        rmax = height[-1]
        
        while i <=j:
            
            if height[i] > lmax:
                lmax = height[i]
            if height[j] > rmax:
                rmax = height[j]
            
            if lmax <= rmax:
                ans += lmax - height[i]
                i += 1

            else:
                ans += rmax - height[j]
                j -= 1
                
        return ans

   
if __name__ == "__main__" :
    
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    ans = TrappingWater(height)
    print(ans)
