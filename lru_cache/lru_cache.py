import sys
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.dict = {}
        self.storage = DoublyLinkedList()


    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        val = self.dict.get(key)
        if val is None:
            return
        else:
            vs = self.storage.tail
            # start off finding the key in cache by seeing if it is at tail
            if vs.value == key:
                # if it is already at the tail, noting needs to be moved
                return val
            while True:
                vs = vs.prev
                # keep going through the storage until it is found
                if vs.value == key:
                    # when found, move it to the end of storage
                    # so it will be first one checked at next request
                    self.storage.move_to_end(vs)
                    # let while know that it was found
                    return val

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # see if anything in cache
        if self.storage.head is None:
            # if nothing in cache, put item in cache
            self.storage.add_to_tail(key)
            self.dict[key] = value
            return
        # at least one item is in cache
        # see if item coming in is already in cache    
        vd = self.dict.get(key)
        # if vd got a value, the key is already in cache
        if vd != None:
            # it is in cache
            self.dict[key] = value
            # set the item in the dictionary to the new value
            vs = self.storage.tail
            # start off finding the key in cache by seeing if it is at tail
            if vs.value == key:
                # if it is already at the tail, nothing needs to be moved
                return
            while True:
                vs = vs.prev
                # keep going through the storage until it is found
                if vs.value == key:
                    # when found, move it to the end of storage
                    # so it will be first one checked at next request
                    self.storage.move_to_end(vs)
                    # let while know that it was found
                    return
        else:
            # key was not found in dictionary
            # see if cache is at limit
            if self.storage.length == self.limit:
                # if at limit, remove oldest entry
                del self.dict[self.storage.head.value]
                self.storage.remove_from_head()
            # not in dictionary, so add it
            self.dict[key] = value
            self.storage.add_to_tail(key)