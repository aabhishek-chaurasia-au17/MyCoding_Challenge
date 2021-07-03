
"""
Q-1 ) Write a program to remove first node from a linked list:
(5 marks)
(Super Easy)
Example 1:
Input(elements in linked list)
2
5
6
8
3
Output(elements after removing head of the linked list)
5
6
8
3
"""





class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = None

def addNodeAtEnd(x):
    global head

    if head is None:
        head = Node(x)
        return
    
    cur = head
    while cur.next != None:
        cur = cur.next
    
    cur.next = Node(x)


def printLinkedList():
    global head

    cur = head
    while cur != None:
        print(cur.data)
        cur = cur.next


def deleteAtHead():
    global head
    if head is None:
        return

    head = head.next


if __name__ == "__main__":

    addNodeAtEnd(2)
    addNodeAtEnd(5)
    addNodeAtEnd(6)
    addNodeAtEnd(8)
    addNodeAtEnd(3)
    
    deleteAtHead()
    printLinkedList()
    


