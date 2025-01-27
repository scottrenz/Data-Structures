import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


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
        # cb(self.value)
        # if self.left:
        #     self.left.for_each(cb)
        # if self.right:
        #     self.right.for_each(cb)
        stack = Stack()
        stack.push(self)
        while stack.len() > 0:
            current_node = stack.pop()
            # do the thing here
            cb(current_node.value)
            if current_node.right:
                stack.push(current_node.right)
            if current_node.left:
                stack.push(current_node.left)
            # don't do this thing down here
# Breadth First Traversal
# Make a queue
# Put root in the queue
# While queue is not empty
#     pop out front of queue
# 	DO THE THING!
#     if left:
#        add left to bck of queue
#     if right:
# 	   add right to back of queue


    # DAY 2 Project -----------------------
        # stack = Stack()
        # stack.push(self)
        # que = Queue()
    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left is not None:
            self.in_order_print(node.left)
        print(node.value)
        if node.right is not None:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(self)
        while queue.len() > 0:
            current_node = queue.dequeue()
            # do the thing here
            print(current_node.value)
            if current_node.right:
                queue.enqueue(current_node.right)
            if current_node.left:
                queue.enqueue(current_node.left)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(self)
        while stack.len() > 0:
            current_node = stack.pop()
            # do the thing here
            print(current_node.value)
            if current_node.right:
                stack.push(current_node.right)
            if current_node.left:
                stack.push(current_node.left)

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

