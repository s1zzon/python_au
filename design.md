+ [Min Stack](#min-stack)
+ [Implement Stack using Queues](#implement-stack-using-queues)
+ [Implement Queue using Stacks](#implement-queue-using-stacks)
+ [Design Twitter](#design-twitter)
<!-----solution----->

## Design Twitter

https://leetcode.com/problems/design-twitter/

```python

def __init__(self):
    self.timer = itertools.count(step=-1)
    self.tweets = collections.defaultdict(collections.deque)
    self.followees = collections.defaultdict(set)

def postTweet(self, userId, tweetId):
    self.tweets[userId].appendleft((next(self.timer), tweetId))

def getNewsFeed(self, userId):
    tweets = heapq.merge(*(self.tweets[u] for u in self.followees[userId] | {userId}))
    return [t for _, t in itertools.islice(tweets, 10)]

def follow(self, followerId, followeeId):
    self.followees[followerId].add(followeeId)

def unfollow(self, followerId, followeeId):
    self.followees[followerId].discard(followeeId)
```

## Implement Queue using Stacks

https://leetcode.com/problems/implement-queue-using-stacks/

```python

def __init__(self):
    """
    Initialize your data structure here.
    """
    self.main_stack = []
    self.sup_stack = []

def push(self, x: int) -> None:
    """
    Push element x to the back of queue.
    """
    for i in range(len(self.main_stack)):
        self.sup_stack.append(self.main_stack.pop())
    self.main_stack.append(x)
    for i in range(len(self.sup_stack)):
        self.main_stack.append(self.sup_stack.pop())

def pop(self) -> int:
    """
    Removes the element from in front of queue and returns that element.
    """
    return self.main_stack.pop()

def peek(self) -> int:
    """
    Get the front element.
    """
    return self.main_stack[-1]

def empty(self) -> bool:
    """
    Returns whether the queue is empty.
    """
    if len(self.main_stack) == 0:
        return True
    else:
        return False
```

## Implement Stack using Queues

https://leetcode.com/problems/implement-stack-using-queues/

```python

def __init__(self):
    """
    Initialize your data structure here.
    """
    self.q1 = []
    self.q2 = []
    

def push(self, x: int) -> None:
    """
    Push element x onto stack.
    """
    self.q2.append(x)
    for i in range(len(self.q1), 0, -1):
        self.q2.append(self.q1.pop(i-1))
    self.q1,self.q2 = self.q2,self.q1
    

def pop(self) -> int:
    """
    Removes the element on top of the stack and returns that element.
    """
    for i in range(len(self.q1), 1, -1):
        self.q2.append(self.q1.pop(i-1))
    pop_res = self.q1.pop()
    self.q1,self.q2 = self.q2,self.q1
    return pop_res
    

def top(self) -> int:
    """
    Get the top element.
    """
    return self.q1[0]
    
    

def empty(self) -> bool:
    """
    Returns whether the stack is empty.
    """
    if self.q1 == []:
        return True
    else:
        return False
```

## Min Stack

https://leetcode.com/problems/min-stack/

```python
def __init__(self, val=None, minimum=None, next=None):
    self.val = val
    self.minimum = minimum
    self.next = next

s MinStack:

def __init__(self):
    """
    initialize your data structure here.
    """
    self.head = None
    

def push(self, val: int) -> None:
    if self.head is None:
        node = Node(val, val)
        self.head = node
    else:
        node = Node(val, min(val, self.head.minimum), self.head)
        self.head = node
    

def pop(self) -> None:
    self.head = self.head.next
    

def top(self) -> int:
    return self.head.val
    

def getMin(self) -> int:
    return self.head.minimum
```