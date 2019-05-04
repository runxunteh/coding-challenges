"""
https://leetcode.com/problems/add-two-numbers/
Given 2 non-empty linked list representing 2 non-negative integers.
The digits are stored in reverse order and each of their nodes contain a
single digit. Add the two numbers and return it as a linked list

Example:
Input: (2->4->3)+(5->6->4)
Output: 7->0->8
Explanation: 342+465=807
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2, carry):
        total=l1.val+l2.val+carry
        carry=total//10
        l3=ListNode(total%10)

        if l1.next!=None or l2.next!=None or carry!=0:
            if l1.next==None:
                l1.next=ListNode(0)
            if l2.next==None:
                l2.next=ListNode(0)
            l3.next=self.addTwoNumbers(l1.next,l2.next,carry)
        return l3
                


List1=ListNode(2)
List1.next=ListNode(4)
List1.next.next=ListNode(3)

List2=ListNode(5)
List2.next=ListNode(6)
List2.next.next=ListNode(4)

new=Solution()
x=new.addTwoNumbers(List1,List2,0)
print(x.val)
print(x.next.val)
print(x.next.next.val)

