class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print ("error must be in LL")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        
        last.next = new_node

llist = LinkedList()
 
llist.head = Node(1)
second = Node(2)
third = Node(3)
 
llist.head.next = second; # Link first node with second
second.next = third; # Link second node with the third node
llist.push(12)
llist.printList()
print("INSERTAFTER OPERATION")
llist.insertAfter(second, 22)
llist.printList()
