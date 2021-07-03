
"""
(Maximum marks -15)
Q-1 ) Dry run the recursive function “reverse_LL_rec(head prev)” from the
code given below, take input provided in the code:
                                                        
(5 marks)                                                       (Super Easy)
"""



class Node:
    def __init__(self,x): # Initialize and create an empty node
        self.data = x
        self.next = None

def printList(head): #This function is to print our tree it returns the value of all our trees one by one
    cur = head        
    while cur!=None:
        print(cur.data, end = " ")
        cur = cur.next

new_head = None
def reverse_LL_rec(head,prev):
    global new_head
    if head is None:    # If our root is empty then come out of the function
        return
    if head.next is None:
        head.next = prev
        return head
    new_head = reverse_LL_rec(head.next,head)    # Here we are calling our reverse function again and again
    head.next = prev
    return new_head


if __name__ == "__main__": 

    head = Node(5)
    head.next = Node(15)
    head.next.next = Node(25)
    head.next.next.next = Node(35)

    printList(head)
    print()
    head_rev = reverse_LL_rec(head,None)
    printList(head_rev)
