import sys


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedHexNumber:
    def __init__(self, num):
        self.len = len(num)
        a = Node(num[0])
        self.head = a
        for i in range(1, len(num)):
            a.next = Node(num[i])
            a = a.next

    def from_hex_to_decimal(self):
        letters = ['A', 'B', 'C', 'D', 'E', 'F']
        a = self.head
        for i in range(self.len):
            if a.val in letters:
                a.val = 10 + letters.index(a.val)
            else:
                a.val = int(a.val)
            a = a.next
        return self

    def from_decimal_to_hex(self):
        letters = ['A', 'B', 'C', 'D', 'E', 'F']
        a = self.head
        for i in range(self.len):
            if a.val > 9:
                a.val = letters[a.val - 10]
            a = a.next
        return self

    def sum(self, second):
        first = self.from_hex_to_decimal()
        second = second.from_hex_to_decimal()
        if self.len < second.len:
            first, second = second, first
        len = second.len
        sum = first
        first = first.head
        second = second.head
        for i in range(len):
            if first.val + second.val <= 15:
                first.val = first.val + second.val
            else:
                first.val = first.val + second.val
                first.next.val, first.val = first.next.val + 1, first.val - 16
            first = first.next
            second = second.next
        sum = sum.from_decimal_to_hex()
        return sum

    def __str__(self):
        res = ""
        a = self.head
        for i in range(self.len):
            a.val = str(a.val)
            res = res + a.val
            a = a.next
        res = res[::-1]
        if res[0] == '0':
            res = res[1:]
        return res


def main(first, second):
    buff = '0'
    first = buff + first
    second = second[::-1]
    first = first[:: -1]
    first = LinkedHexNumber(first)
    second = LinkedHexNumber(second)
    first = first.sum(second)
    print(first)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
