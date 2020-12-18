+ [Reverse Linked List](#reverse-linked-list)
+ [Middle of the Linked List](#middle-of-the-linked-list)
+ [Palindrome Linked List](#palindrome-linked-list)
+ [Merge Two Sorted Lists](#merge-two-sorted-lists)
+ [Sort List](#sort-list)
+ [Linked List Cycle](#linked-list-cycle)
+ [Remove Nth Node From End of List](#remove-nth-node-from-end-of-list)
+ [Intersection of Two Linked Lists](#intersection-of-two-linked-lists)
+ [Linked List Cycle II](#linked-list-cycle-ii)
<!-----solution----->

## Linked List Cycle II

https://leetcode.com/problems/linked-list-cycle-ii/

```python
def detectCycle(self, head: ListNode) -> ListNode:
    if head is None:
        return None
    fast = head
    slow = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    
    if fast is None or fast.next is None:
        return None
    
    while head != slow:
        head = head.next
        slow = slow.next
    
    
    return head
```

## Intersection of Two Linked Lists

https://leetcode.com/problems/intersection-of-two-linked-lists/

```python
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    curr_A, curr_B = headA, headB
    len_A, len_B = 0, 0

    while curr_A:
        len_A += 1
        curr_A = curr_A.next

    while curr_B:
        len_B += 1
        curr_B = curr_B.next

    if curr_A is not curr_B:
        return False

    chop_off_threshold = abs(len_A - len_B)

    shorter_head = headA if len_A < len_B else headB
    longer_head = headB if len_B > len_A else headA

    for _ in range(chop_off_threshold):
        longer_head = longer_head.next

    while shorter_head is not longer_head:
        shorter_head = shorter_head.next
        longer_head = longer_head.next

    return longer_head
```

## Remove Nth Node From End of List

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

```python
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    p = head
    i = 0
    while p:
        p = p.next
        i += 1
    p = head
    step = i-n
    if step == 0:
        head = head.next
    else:
        l = 1
        while l<step :
            p = p.next
            l += 1
        p.next = p.next.next
    return head
```

## Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/

```python
def hasCycle(self, head: ListNode) -> bool:
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if(slow == fast):
            return True
    return False
```

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
