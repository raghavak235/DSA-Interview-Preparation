


class Node:
    def __init__(self, key):
        self.key=key
        self.next = None

def print_cll(head):
    if head == None:
        return None
    print(head.key, end=' ')
    current = head.next
    while current != head:
        print(current.key, end=' ')
        current =current.next

def insert_beginning_cll(head, key):
    newnode = Node(key)
    if head == None:
        newnode.next = newnode
        return newnode
    newnode.next =head.next
    head.next = newnode
    head.key, newnode.key = newnode.key, head.key
    return head

# TC:O(1)
# SC:O(1)


def insert_end_cll_navie(head, key):
    tmp = Node(key)
    if head == None:
        tmp.next = tmp
        return tmp
    current = head
    while current.next != head:
        current = current.next
    current.next = tmp
    tmp.next = head
    return tmp

# TC:O(n)
# SC:O(1)


def insert_end_cll(head, key):
    newnode = Node(key)
    if head == None:
        newnode.next = newnode
        return newnode
    # head → [5] → [10] → [15] → None
    #                ↑
    # newnode → [20] ┘

    newnode.next = head.next
    head.next = newnode
    newnode.key, head.key = head.key, newnode.key
    return newnode # new head


# TC:O(1)
# SC:O(1)



def delete_head_cll(head):
    if head == None:
        return None
    if head.next == head:
        return None

    head.key = head.next.key
    head.next = head.next.next
    return head

def delete_kth_cll(head, k):
    if head == None:
        return None

    current = head
    for i in range(k-2):
        current = current.next
    current.next = current.next.next
    return head

head = Node(10)
head.next = Node(20)
head.next.next = head
# insert_beginning_cll(head, 5)
# insert_end_cll_navie(head, 25)
head= insert_end_cll(head, 30)
head= insert_end_cll(head, 35)
# head=delete_head_cll(head)
head = delete_kth_cll(head, 3)

print_cll(head)



