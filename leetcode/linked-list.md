# Linked List

+[Reverse Linked List](#reverse-linked-list)

##Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/

```python
 def reverseList(self, head: ListNode) -> ListNode:
        prv = None
        while head:
            temp = head.next
            head.next = prv
            prv = head
            head = temp
        head = prv
        return head
```

# Linked List

+[Middle of the Linked List](#middle-of-the-linked-list)

##Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/

```python
 def middleNode(self, head):
        tmp = head
        while tmp and tmp.next:
            head = head.next
            tmp = tmp.next.next
        return head
```
# Linked List

+[Palindrome Linked List](#palindrome-linked-list)

##Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/

```python
 def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        tmp = head
        while tmp:
            stack.append(tmp.val)
            tmp = tmp.next
        while head:
            if stack.pop() != head.val:
                return False
            else:
                head = head.next
        return True
```
# Linked List

+[Merge Two Sorted Lists](#merge-two-sorted-lists)

##Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/

```python
 def mergeTwoLists(self, ln1: ListNode, ln2: ListNode) -> ListNode:
        head = sort_list = ListNode(0)        
        while(ln1 and ln2):
            if (ln1.val < ln2.val):
                sort_list.next = ln1
                ln1 = ln1.next
                sort_list = sort_list.next                
            else:
                sort_list.next = ln2
                ln2 = ln2.next
                sort_list = sort_list.next
        sort_list.next = ln1 or ln2
        return head.next
        
```
# Linked List

+[Sort List](#sort-list)

##Sort List

https://leetcode.com/problems/sort-list/

```python
	def sortList(self, head: ListNode) -> ListNode:
		tmp = head
		a = []
		while(tmp):
			a.append(temp.val)
			tmp=tmp.next
		if not a:
			return head
		a.sort()
		head = ListNode(a[0])
		tmp= head
		for i in range(1, len(a)):
			tmp.next = ListNode(a[i])
			tmp = tmp.next
		return head
```