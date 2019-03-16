#Write code to remove duplicates from an unsorted linked list

import unittest

class Node():
    def __init__(self,value):
        self.value=value
        self.next=None

def remove_dups(node):
    hash_table={}
    hash_table[node.value]=True
    while node.next!=None:  #haven reach the end of linked list
        if node.next.value in hash_table:   #if there is duplicate
            node.next=node.next.next
        else:   #if no duplicate, update it in the hash table
            hash_table[node.next.value]=True
            node=node.next
    return node

class TestFactorial(unittest.TestCase):
    def test_remove_dups(self):
        head=Node(1)
        head.next=Node(3)
        head.next.next=Node(1)
        remove_dups(head)
        self.assertEqual(head.value,1)
        self.assertEqual(head.next.value,3)
        self.assertEqual(head.next.next,None)

if __name__ == "__main__":
  unittest.main()
