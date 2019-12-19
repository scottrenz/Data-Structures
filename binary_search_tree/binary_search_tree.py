import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value == value:
            return
        if self.contains(value):
            return
        if value > self.value:
            current_next = self.right
            if current_next is None:
                self.right = BinarySearchTree(value)
                return
            else:
                current_next.insert(value)    
                return
        else:
            current_next = self.left
            if current_next is None:
                self.left = BinarySearchTree(value)
                return
            else:
                current_next.insert(value)    
                return
        return

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        current_next = self.right if target > self.value else self.left    
        if current_next is not None:
            if current_next.value == target:
                return True
            else:
                current_next.contains(target)
        else:    
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        maxv = self.value
        current_next = self.right
        if current_next is None:
            return maxv
        return current_next.get_max()
        
    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
# bst = BinarySearchTree(5)
# bst.insert(2)
# bst.insert(7)
# bst.insert(1)
# rst = bst.left
# print(bst.value,bst.left if bst.left is None else bst.left.value ,bst.right if bst.right is None else bst.right.value)
# print(rst.value,rst.left if rst.left is None else rst.left.value ,rst.right if rst.right is None else rst.right.value)

