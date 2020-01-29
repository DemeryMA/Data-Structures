import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements? because of the many functions in our DLL which will allow for data control
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        return self.storage.add_to_tail(value)
        # enque should be adding an item to the back of the que

    def dequeue(self):
        if self.size != 0:
            size -= 1
            return self.storage.remove_from_head()
        else:
            return
        # dequeue should remove and return an item from the front of the queue.

    def len(self):
        # return len(self.storage)
        return self.size

