class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.len = 0
        self.counter = 0

    def get(self, index: int) -> int:
        if index >= self.len:
            return -1
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.val

    def add_at_head(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.len += 1

    def add_at_tail(self, val: int) -> None:
        new_node = Node(val)
        if self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.len += 1

    def add_at_index(self, index: int, val: int) -> None:
        if index is self.len:
            self.add_at_tail(val)
        elif index is 0:
            self.add_at_head(val)
        elif index < self.len:
            new_node = Node(val)
            prev = self.head
            cur = self.head.next
            for i in range(1, index):
                prev = prev.next
                cur = cur.next
            prev.next = new_node
            new_node.next = cur
            new_node.prev = prev
            cur.prev = new_node
            self.len += 1

    def delete_at_index(self, index: int) -> None:
        if index is 0 and self.len is 1:
            self.head = None
            self.tail = None
            self.len -= 1
        elif index is 0:
            a = self.head.next
            a.prev = None
            self.head = a
            self.len -= 1
        elif index is (self.len - 1):
            a = self.tail.prev
            a.next = None
            self.tail = a
            self.len -= 1
        elif (index < self.len) and (index > 0):
            n = 0
            cur = self.head
            while n is not index:
                n += 1
                cur = cur.next
            a = cur.prev
            b = cur.next
            a.next = b
            b.prev = a
            self.len -= 1

    def print_list(self):
        a = self.head
        for i in range(self.len):
            print(a.val)
            a = a.next

    def __next__(self):

        if self.counter < self.len:
            self.counter += 1
            return self.get(self.counter - 1)
        else:
            raise StopIteration

    def __iter__(self):
        return self
