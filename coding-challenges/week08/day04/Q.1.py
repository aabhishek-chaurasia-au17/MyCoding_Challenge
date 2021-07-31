"""
Q - 1) Write a program to print sum of right diagonal of a matrix: (5 marks)
Right diagonal is shown below:
"""

def rightDiagonal(mat, n, m):
	print("Right Diagonal: ", end = "")

	for i in range(n):
		for j in range(m):
            
			if ((i + j) == (n - 1)):
				print(mat[i][j], end = ", ")
	print()

n = 3
m = 4

a = [[1, 2, 3, 4 ],
	[ 5, 6, 7, 8 ],
    [ 9, 10,11,12]]
	
rightDiagonal(a, n, m)

