class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    # This function prints contents of linked list
    # starting from head
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next
#Nodes of the lists have been created
llist = Linkedlist()
llist.head = Node(1)
second = Node(2)
third = Node(3)

#connect the nodes to form a linked list 
llist.head.next = second
second.next = third

llist.printList()



        