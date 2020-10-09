class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prv = None
        while head:
            temp = head.next
            head.next = prv
            prv = head
            head = temp

        head = prv
        return head