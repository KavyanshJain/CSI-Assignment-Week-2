# CSI-Assignment-Week-2

CSI Assignment Week 2

## Problem Statement
Create a Python program that implements a singly linked list using Object-Oriented Programming (OOP) principles. Your implementation should include the following: A Node class to represent each node in the list. A LinkedList class to manage the nodes, with methods to: Add a node to the end of the list Print the list Delete the nth node (where n is a 1-based index) Include exception handling to manage edge cases such as: Deleting a node from an empty list Deleting a node with an index out of range Test your implementation with at least one sample list.

## Answer/Solution
Use the main.py file and see the OOPs implementation of LinkedList in python.

### The working of main.py
We created a class Node which have a data part and other a pointer part.
The next we created a LinkedList class where we will create our fuction to operate this following taks:
- Adding a node to the end.
- Printing the list.
- Deleting the nth node(where indexing starts at 1).
- Printing the Length of the Linked-List.
- A indicitor at end to see if our list is empty after the operation.

We have also created a class "LinkedListException" where we done our error handling while operating this operations.

### Test cases
- Tested our function to see the length of the list and check if it is empty.

- Creating our Linked-List from given values by adding one by one through looping.

- Checking if our delete_nth_node() function deleting the choices as according the index starting as 1.

- Testing our Exception/Error Handling for different scenarios like n index less than 1, or out of range.