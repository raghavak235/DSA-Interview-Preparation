
class Node:
    def __init__(self, data):
        self.data = data
        self.next_ptr = None

class LinkedList:
    # Linked List Initialization
    def __init__(self):
        self.head=None

    # Time Complexity:O(1)
    # Function to insert the new data at the beginning of LL
    def insertAtBegning(self, new_data):
        new_node = Node(new_data)
        new_node.next_ptr = self.head
        self.head = new_node

    # Time Complexity:O(1)
    # Function to insert the new data at the middle of LL
    def insertAfterNodeWithReference(self, prev_node, new_data):
        if prev_node is None:
            print('Given node must be present inside the LL')
            return
        new_node = Node(new_data)
        new_node.next_ptr = prev_node.next_ptr
        prev_node.next_ptr = new_node


    # Time Complexity:O(n)
    # Function to insert the new data at the very end of LL
    def insertAtEnd(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next_ptr:
            temp = temp.next_ptr
        temp.next_ptr = new_node

    # Time Complexity:O(n)
    # Function to search the given data in LL
    def searchNode(self, nodeData):
        if self.head is None:
            return False

        temp = self.head
        while temp:
            if temp.data == nodeData:
                return True
            temp= temp.next_ptr
        return False

    # function to count the number of nodes in LL
    def countNodes(self):
        count=0
        temp = self.head
        while temp:
            count = count + 1
            temp = temp.next_ptr
        return count


    # Printing the values of LL
    def printLL(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next_ptr



ll = LinkedList()
ll.insertAtBegning(10)
ll.insertAtBegning(20)
ll.insertAtEnd(30)
ll.insertAfterNodeWithReference(ll.head.next_ptr, 25)
result = ll.countNodes()
print(result)
ll.printLL()
search = ll.searchNode(40)
print(search)