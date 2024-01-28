class Node:
    """A node in a singly linked list."""
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """Class for singly linked list."""
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        """Append a new node at the end of the list."""
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def display(self):
        """Display the contents of the list."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

def reverse_linked_list(linked_list):
    """Reverse the linked list in place."""
    prev = None
    current = linked_list.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    linked_list.head = prev

def merge_sorted_lists(list1, list2):
    """Merge two sorted linked lists into a single sorted list."""
    dummy = Node()
    tail = dummy

    while list1 and list2:
        if list1.data < list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 or list2
    return dummy.next

def get_middle(node):
    """Get the middle of the linked list."""
    if not node:
        return node

    slow = node
    fast = node

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def merge_sort_list(head):
    """Sort the linked list using merge sort algorithm."""
    if not head or not head.next:
        return head

    middle = get_middle(head)
    next_to_middle = middle.next

    middle.next = None

    left = merge_sort_list(head)
    right = merge_sort_list(next_to_middle)

    sorted_list = merge_sorted_lists(left, right)
    return sorted_list

# Example usage
linked_list = SinglyLinkedList()
linked_list.append(3)
linked_list.append(1)
linked_list.append(5)
linked_list.append(2)

print("Original List:", linked_list.display())

reverse_linked_list(linked_list)
print("Reversed List:", linked_list.display())

sorted_head = merge_sort_list(linked_list.head)
sorted_linked_list = SinglyLinkedList(head=sorted_head)
print("Sorted List:", sorted_linked_list.display())
