
"""
Q-1 ) Maximum path sum in matrix - solve with DP
https://practice.geeksforgeeks.org/problems/path-in-matrix3805/1
(5 marks)
(Medium)
Given a NxN matrix of positive integers. There are only three possible moves
from a cell Matrix[r][c].
1. Matrix [r+1] [c]
2. Matrix [r+1] [c-1]
3. Matrix [r+1] [c+1]
Starting from any column in row 0 return the largest sum of any of the paths up to
row N-1.
Example 1:
Input: N = 2
Matrix = {{348, 391},
{618, 193}}
Output: 1009
Explaination: The best path is 391 -> 618.
It gives the sum = 1009.
"""





def findMaxPath(mat):

	res = -1
	for i in range(M):
		res = max(res, mat[0][i])

	for i in range(1, N):

		res = -1
		for j in range(M):

			if (j > 0 and j < M - 1):
				mat[i][j] += max(mat[i - 1][j],
								max(mat[i - 1][j - 1],
									mat[i - 1][j + 1]))

			elif (j > 0):
				mat[i][j] += max(mat[i - 1][j],
								mat[i - 1][j - 1])

			elif (j < M - 1):
				mat[i][j] += max(mat[i - 1][j],
								mat[i - 1][j + 1])

			res = max(mat[i][j], res)
	return res

N=4
M=6
mat = ([[ 10, 10, 2, 0, 20, 4 ],
		[ 1, 0, 0, 30, 2, 5 ],
		[ 0, 10, 4, 0, 2, 0 ],
		[ 1, 0, 2, 20, 0, 4 ]])
			
print(findMaxPath(mat))

