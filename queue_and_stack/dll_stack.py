import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

dll = DoublyLinkedList()

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = dll
    def push(self, value):
        return self.storage.add_to_tail(value)

    def pop(self):
        if self.storage.length > 0:
            return self.storage.remove_from_tail()
        return


    def len(self):
        return self.storage.length
