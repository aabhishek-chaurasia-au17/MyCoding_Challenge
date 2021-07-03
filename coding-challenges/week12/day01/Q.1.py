
"""
Q-1 ) Write a program to print nodes in a BST having odd values:
(Easy)
(5 marks)
Input:
Sample output:
3
1
7
13
"""



class newNode:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None


def inorder( root) :
	if (root != None):
		inorder(root.left)
		print(root.key, end = " ")
		inorder(root.right)
	

def insert(node, key):
	if (node == None):
		return newNode(key)

	if (key < node.key):
		node.left = insert(node.left, key)
	else:
		node.right = insert(node.right, key)

	return node


def oddNode(root) :

	if (root != None):
		oddNode(root.left)
		
		if (root.key % 2 != 0):
			print(root.key, end = " ")
		oddNode(root.right)


if __name__ == '__main__':
	
	root = None
	root = insert(root, 5)
	root = insert(root, 3)
	root = insert(root, 2)
	root = insert(root, 4)
	root = insert(root, 7)
	root = insert(root, 6)
	root = insert(root, 8)

	oddNode(root)


