

class Node:
    def __init__(self, k):
        self.key = k
        self.prev = None
        self.next = None



TC, AS:  O(1)
def insert_at_beg(head, key):
    # Create a new node with the given key.
    new_node = Node(k=key)
    
    # If the list is empty, return the new node as the head.
    if head is None:
        return new_node
    
    # Otherwise, link the new node before the current head.
    new_node.next = head   # New node's next pointer is set to the current head.
    head.prev = new_node   # Current head's prev pointer is set to the new node.
    
    # Return the new node as the new head of the list.
    return new_node

Ts : O(n)
AS: O(1)
There is also an optimized approach where you need to keep tail reference where TC will be O(1)

def insert_last(head,key):
    newnode = Node(key)
    if head == None:
        return newnode
    current = head
    while current.next != None:
        current =current.next

    current.next = newnode
    newnode.prev = current
    return head
def delete_head(head):
    if head == None:
        return None
    if head.next == None:
        return None

    head = head.next
    head.prev = None
    return None


def delete_last_node(head):
    if head == None:
        return None
    if head.next == None:
        return None

    current = head
    while current.next.next !=None:
        current = current.next

    current.next = None

    return head

def reverse_dll(head):
        if head == None:
            return None
        if head.next == None:
            return head
        current = head
        prev =None
        while current != None:
            prev = current
            current.next, current.prev = current.prev, current.next
            # Since current.prev now points to B (original next), this effectively moves current forward in the original list
            current = current.prev
        return prev



def print_dll(head):
    current =head
    while current !=  None:
        print(current.key, end=' ')
        current = current.next
