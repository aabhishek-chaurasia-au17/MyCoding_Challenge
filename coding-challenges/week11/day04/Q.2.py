"""
Q-2 ) Write postorder and inorder traversal function for the tree given
below, including declaring classes, providing input and perform the dry run
also.                                                           
(5 marks)                                                   (Lengthy but easy)
"""


class Node:
    def __init__(self, data):   # Initialize and create an empty node
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root is None:   # If our root is empty then come out of the function
        return
    
    inorder(root.left)   # Here we are calling our reverse function again and again
    print(root.data)
    inorder(root.right)  # Here we are calling our reverse function again and again

def postorder(root):
    if root is None:
        return
    
    postorder(root.left)  # Here we are calling our reverse function again and again
    postorder(root.right)  # Here we are calling our reverse function again and again
    print(root.data)

if __name__ == "__main__":

    root = Node(15)
    root.left = Node(11)
    root.right = Node(33)

    root.left.right = Node(66)
    root.left.left = Node(99)
    
    inorder(root)

