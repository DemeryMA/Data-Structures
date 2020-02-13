import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements? for inserting and deleting nodes
        # self.storage = ?
        self.storage = DoublyLinkedList()

    # The push() method adds new items to the end of an array, and returns the new length.
    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    # ? Why is the answer add_to_head when push() methods are supposed to add to the end of an array

    #  The pop method removes the last element from an array and returns that value to the caller. pop is intentionally generic; this method can be called or applied to objects resembling arrays.
    def pop(self):
        if self.size != 0:
            self.size -= 1
            return self.storage.remove_from_head()
        else:
            return
    # ? Why is the answer remove_from_head when pop() is supposed to remove the last element from an array
    # is it because with a stack we do LIFO (last in first out?)

    def len(self):
        # return len(self.storage)
        return self.size
