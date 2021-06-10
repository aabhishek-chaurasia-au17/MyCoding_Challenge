"""
# Q- 2 ) Average Salary Excluding the Minimum and Maximum Salary (5
# marks)
# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
# Given an array of unique integers salary where salary[i] is the salary of the
# employee i.
# Return the average salary of employees excluding the minimum and maximum
# salary.
"""
# Example 1:
# Input: salary = [4000,3000,1000,2000]
# Output: 2500.00000
# Explanation: Minimum salary and maximum salary are 1000 and 4000
# respectively.
# Average salary excluding minimum and maximum salary is (2000+3000)/2= 2500




def average(salary):

    salary.remove(min(salary))
    salary.remove(max(salary)) 

    return sum(salary) / len(salary)

if __name__ == "__main__":

    salary = [4000,3000,1000,2000]
    print(average(salary))


