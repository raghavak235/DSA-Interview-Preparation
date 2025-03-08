LL introduction:


TC: O(n) as it need to traverse n nodes
AC=SC=O(1)

# Define a Node class for the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Helper function to print the linked list in a visual (box) format
def print_linked_list(head):
    current = head
    while current:
        # Print the node in a box-like format
        print(f"[ {current.data} ]", end="")
        if current.next:
            print(" -> ", end="")
        current = current.next
    print()  # Newline at the end

def main():
    # Step 1: Create the first node with data "A"
    node1 = Node("A")
    # Visual representation:
    # +-----+
    # |  A  | -> None
    # +-----+
    print("Step 1: Created Node1")
    print_linked_list(node1)
    
    # Step 2: Create the second node with data "B" and link it to Node1
    node2 = Node("B")
    node1.next = node2
    # Visual representation:
    # +-----+      +-----+
    # |  A  | ---> |  B  | -> None
    # +-----+      +-----+
    print("Step 2: Created Node2 and linked Node1 to Node2")
    print_linked_list(node1)
    
    # Step 3: Create the third node with data "C" and link it to Node2
    node3 = Node("C")
    node2.next = node3
    # Visual representation:
    # +-----+      +-----+      +-----+
    # |  A  | ---> |  B  | ---> |  C  | -> None
    # +-----+      +-----+      +-----+
    print("Step 3: Created Node3 and linked Node2 to Node3")
    print_linked_list(node1)

if __name__ == "__main__":
    main()

TC: O(n) as it need to traverse n nodes
AC=SC=O(1)
def searchNode(head, x):
    curr = head
    counter = 1
    while curr != None:
        if curr.key == x:
            return counter
        counter += 1
        curr = curr.next
    
    return -1

TC: O(n) as it need to traverse n nodes
AC=SC=O(1)
def insertEnd(head, key):
    if head == None:
        return Node(key)

    current = head
    while current.next != None:
        current = current.next
    current.next = Node(key)
    return head

# Explanation of insertBegining Function in a Linked List

## Overview

The given Python code implements a function to insert a new node at the beginning of a linked list. We will explain each step in detail with visual representations.

---

## Code

```python
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

def insertBegining(head, key):
    tmp = Node(key)  # Step 1: Create a new node
    tmp.next = head  # Step 2: Point new node's next to the current head
    return tmp       # Step 3: Return new head

if __name__ == "__main__":
    head = None
    head = insertBegining(head, key=1)  # Insert first node
    head = insertBegining(head, key=2)  # Insert second node
```

---

## Step-by-Step Execution

### Step 1: Creating a Node Class

We define a `Node` class with:

- A `key` attribute to store the data.
- A `next` pointer to link to the next node.

### Step 2: Implementing `insertBegining` Function

This function inserts a new node at the beginning of the linked list:

1. Create a new node with the given key.
2. Point the new node’s `next` to the current head.
3. Return the new node as the new head.

### Step 3: Inserting Nodes

#### Initial State (Empty List)

```
head = None
```

```
(None)
```

#### Insert 1

```python
head = insertBegining(head, key=1)
```

New list:

```
[1] -> None
```

#### Insert 2

```python
head = insertBegining(head, key=2)
```

New list:

```
[2] -> [1] -> None
```

---

## Final Representation

The linked list now looks like:

```
head -> [2] -> [1] -> None
```

This method efficiently inserts elements at the beginning of the linked list.

## Notes

- **Time Complexity**: O(1), as insertion at the head is constant time.
- **Space Complexity**: O(1), as we only create one new node per call.


# Visual Explanation of `insert_position`

This document provides a step-by-step, visual explanation of the following function:

```python
def insert_position(head, key, pos):
    tmp = Node(key)
    current = head
    if pos == 1:
        tmp.next = head
        return tmp

    for i in range(pos-2):
        current = current.next
        # If during traversal, current becomes None (end of list reached before expected), the function returns the original list (insertion is invalid).
        if current == None:
            return head

    tmp.next = current.next
    current.next = tmp
    return head

         +--------------------------------------------------+
         |            Start: insert_position              |
         +--------------------------------------------------+
                             │
                             ▼
                 +-------------------------+
                 | Create new node: tmp =  |
                 |       Node(key)         |
                 +-------------------------+
                             │
                             ▼
                +--------------------------+
                | Set current = head       |
                +--------------------------+
                             │
                             ▼
              +-------------------------------+
              | Is pos equal to 1?            |
              +-------------------------------+
               /              \
              / Yes            \ No
             ▼                  ▼
+---------------------+   +-----------------------------+
| tmp.next = head     |   | Execute for loop:           |
| Return tmp          |   | for i in range(pos-2):      |
+---------------------+   |   current = current.next    |
                          |   if current is None:       |
                          |       return head           |
                          +-----------------------------+
                                        │
                                        ▼
                          +-----------------------------+
                          | Set tmp.next = current.next |
                          | Update current.next = tmp   |
                          +-----------------------------+
                                        │
                                        ▼
                             +----------------------+
                             | Return head          |
                             +----------------------+


Comparision of different Operations:

| **Operation**             | **Array-Based List**                                                                                               | **Linked List**                                                                                            | **Reasoning**                                                                                                                                                                           |
|---------------------------|--------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Access/Indexing**       | O(1) – Direct indexing is possible.                                                                              | O(n) – Must traverse from the head node.                                                                   | Arrays store elements contiguously in memory allowing direct access; linked lists require sequential traversal to reach an element.                                                     |
| **Search (unsorted)**     | O(n) – Must check each element.                                                                                    | O(n) – Must traverse sequentially.                                                                         | Both structures have to scan elements in the worst-case. Note: a sorted array can use binary search (O(log n)), but linked lists cannot efficiently support binary search.            |
| **Insertion at End**      | Amortized O(1) – Fast if capacity exists; worst-case O(n) when resizing.                                             | O(1) – If a tail pointer is maintained.                                                                    | Arrays can add elements quickly until capacity is exceeded (which then requires a costly resize), while linked lists can append in constant time if the tail is tracked.             |
| **Insertion at Beginning**| O(n) – All elements must be shifted.                                                                               | O(1) – Just update the head pointer.                                                                       | Inserting at the beginning of an array requires shifting all elements to create space; a linked list only needs to update a pointer.                                                     |
| **Insertion in Middle**   | O(n) – Elements after the insertion point must be shifted.                                                         | O(n) – Traversal to the insertion point is needed, but insertion itself is O(1).                             | The cost in arrays is dominated by shifting elements; linked lists pay a traversal cost to reach the point, but then insertion is fast.                                                 |
| **Deletion at End**       | O(1) – Simply reduce the array size.                                                                               | O(n) – For singly linked lists (unless a tail pointer and previous pointer are maintained), O(1) for doubly linked lists with a tail pointer. | Array deletion at the end is simple; in linked lists, if only singly linked without backward pointers, you might need to traverse to update the previous node.                         |
| **Deletion at Beginning** | O(n) – All elements must be shifted left.                                                                          | O(1) – Just update the head pointer.                                                                       | Deleting the first element in an array shifts all subsequent elements; linked lists can quickly remove the head by changing a pointer.                                                 |
| **Deletion in Middle**    | O(n) – Elements after the deletion point must be shifted.                                                          | O(n) – Traversal is required to reach the element, then removal is O(1).                                     | Both require a cost: arrays must shift elements, while linked lists must traverse to the node before deletion.                                                                        |
| **Memory Overhead**       | Low – Only stores the elements.                                                                                    | Higher – Stores additional pointers for each node.                                                         | Arrays are compact in memory; linked lists require extra space for storing pointers along with the data.                                                                              |
| **Cache Locality**        | High – Data is stored contiguously, leading to better cache performance.                                           | Low – Nodes can be scattered in memory.                                                                    | Contiguous memory in arrays improves cache performance, while linked lists may lead to cache misses due to non-sequential memory allocation.                                           |
| **Insertion/Deletion given direct pointer** | Not applicable – Direct pointer manipulation isn’t used in arrays.                                                      | O(1) – If you already have the pointer to the node (and its predecessor, if needed).                        | In linked lists, if you already know the location, you can adjust pointers quickly without additional traversal.                                                                      |




Cache Locality:  

Arrays are stored in contiguous blocks of memory. This means that once you load one element, nearby elements are likely already loaded into the processor's cache due to a phenomenon called spatial locality. When a processor fetches data, it doesn't just fetch one byte or one element; it fetches a block of adjacent memory. As a result, when you access elements in an array sequentially, you're likely to hit the cache, which makes data retrieval much faster.

On the other hand, linked lists are made up of nodes that are typically allocated separately in memory. Because these nodes may be scattered around, accessing one node doesn't guarantee that the next node is already in the cache. This lack of cache locality means that the processor may need to fetch data from slower main memory more often, leading to potential cache misses and, consequently, slower performance.
