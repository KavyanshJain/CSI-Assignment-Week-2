# Creating a Singly list node using class
class Node:
       
    def __init__(self, data):
        self.data = data
        self.next = None

# Class to handle Exception messages
class LinkedListException(Exception):
    pass

# Class to handle linkedlist operations
class LinkedList:  
    def __init__(self):
        self.head = None
    
    def add_node(self, data):
        new_node = Node(data)

        # If the list is empty, make the new node the head
        if not self.head:
            self.head = new_node
            return
        
        # Traverse to the end of the list
        current = self.head
        while current.next:
            current = current.next
        
        # Add the new node at the end
        current.next = new_node
    
    def print_list(self):
        # Check if list is empty
        if not self.head:
            print("List is empty")
            return
        #creat a traversing header
        current = self.head
        elements = []
        
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print(" -> ".join(elements))
    
    def delete_nth_node(self, n):
        # Check if list is empty
        if not self.head:
            raise LinkedListException("Cannot delete from an empty list")
        
        # Check for invalid index
        if n < 1:
            raise LinkedListException("Index must be greater than 0 (1-based indexing)")
        
        # If deleting the first node
        if n == 1:
            self.head = self.head.next
            return
        
        # Traverse to find the (n-1)th node
        current = self.head
        for i in range(1, n - 1):
            if not current.next:
                raise LinkedListException(f"Index {n} is out of range")
            current = current.next
        
        # Check if the nth node exists
        if not current.next:
            raise LinkedListException(f"Index {n} is out of range")
        
        # Delete the nth node by updating the link
        current.next = current.next.next
    
    def get_length(self):
        # Printing the size of linkedlist
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def is_empty(self):
        
        return self.head is None
    

def test_linked_list():
    print("\t\t=== Testing Singly Linked List Implementation ===\n")
    
    # Create a new linked list
    l1 = LinkedList()
    
    # Test 1: Print empty list
    print("1. Testing empty list:")
    l1.print_list()
    print(f"Length: {l1.get_length()}")
    print(f"Is empty: {l1.is_empty()}\n")
    
    # Test 2: Add nodes to the list
    print("2. Adding nodes (10, 20, 30, 40, 50):")
    for value in [10, 20, 30, 40, 50]:
        l1.add_node(value)
        print(f"Added {value}")
    
    print("Current list:")
    l1.print_list()
    print(f"Length: {l1.get_length()}")
    print(f"Is empty: {l1.is_empty()}\n")
    
    # Test 3: Delete nodes with valid indices
    print("3. Testing valid deletions:")
    
    # Delete first node (index 1)
    print("Deleting node at index 1 (first node):")
    l1.delete_nth_node(1)
    l1.print_list()
    
    # Delete middle node (index 2)
    print("Deleting node at index 2:")
    l1.delete_nth_node(2)
    l1.print_list()
    
    # Delete last node (index 3)
    print("Deleting node at index 3 (last node):")
    l1.delete_nth_node(3)
    l1.print_list()
    print()
    
    # Test 4: Exception handling
    print("4. Testing exception handling:")
    
    # Test deleting from current list (should work)
    try:
        l1.delete_nth_node(1)
        print("Deleted node at index 1")
        l1.print_list()
    except LinkedListException as e:
        print(f"Error: {e}")
    
    # Test deleting from empty list
    try:
        l1.delete_nth_node(1)  # This should raise an exception
        print("Deleted node at index 1")
    except LinkedListException as e:
        print(f"Error: {e}")
    
    # Test invalid index (negative)
    l1.add_node(100)  # Add a node back
    
    
    try:
        l1.delete_nth_node(0)  # Invalid index
    except LinkedListException as e:
        print(f"Error: {e}")
    
    # Test index out of range
    try:
        l1.delete_nth_node(5)  # Out of range
    except LinkedListException as e:
        print(f"Error: {e}")
    
    print("\nFinal list:")
    l1.print_list()


test_linked_list()