#https://www.interviewcake.com/question/python/queue-two-stacks

"""
This question from interviewcake is to implement a queue with two stacks and the queue
should have an enqueue and dequeue method.

--A queue will store items in a FIFO order. It can be implemented using linked list
where enqueue is to insert at the tail of the linked list and dequeue is to remove
at the head of the linked list.

--A stack will store items in a LIFO order. It can be implemented using linked list
and dynamic array.
                        Push                     Pop
Linked lists            Insert at head           Remove at head

Dynamic arrays          Append                   Remove last element

Solution:
--Two stacks: in_stack and out_stack

--To enqueue: push the enqueued item onto in_stack

--To dequeue on an empty out_stack, the oldest item is at the bottom of in_stack.
So we dig to the bottom of in_stack by pushing each item one-by-one onto out_stack
until we reach the bottom item which we return.
E.g. in_stack(a,b,c). out_stack(empty), so the oldest item is a(at the bottom)
After moving everything from in_stack to out_stack, the item that was enqueued the
2nd longest ago (after the item we just returned) is at the top of out_stack,
the item enqueued 3rd longest ago is just below it, etc.

--To dequeue on a non-empty out_stack, return the top item from out_stack

The code and solution is all from interview cake, this is for educational purposes only
"""

import unittest

class QueueTwoStacks(object):

    def __init__(self):
        self.in_stack  = []
        self.out_stack = []
    
    def enqueue(self, item):
        self.in_stack.append(item)
    
    def dequeue(self):
        if len(self.out_stack) == 0:
    
            # Move items from in_stack to out_stack, reversing order
            while len(self.in_stack) > 0:
                newest_in_stack_item = self.in_stack.pop()
                self.out_stack.append(newest_in_stack_item)
    
            # If out_stack is still empty, raise an error
            if len(self.out_stack) == 0:
                raise IndexError("Can't dequeue from empty queue!")
    
        return self.out_stack.pop()

# Tests
class Test(unittest.TestCase):

    def test_basic_queue_operations(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        queue.enqueue(4)

        actual = queue.dequeue()
        expected = 3
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 4
        self.assertEqual(actual, expected)

    def test_error_when_dequeue_from_new_queue(self):
        queue = QueueTwoStacks()

        with self.assertRaises(Exception):
            queue.dequeue()

    def test_error_when_dequeue_from_empty_queue(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        with self.assertRaises(Exception):
            queue.dequeue()

unittest.main(verbosity=2)
