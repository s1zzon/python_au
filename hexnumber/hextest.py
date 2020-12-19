import unittest
from hexnumber import LinkedHexNumber
from hexnumber import Node


class TestLinkedHexNumber(unittest.TestCase):
    def test_from_hex_to_decimal(self):
         first = LinkedHexNumber('ABC')
         first = first.from_hex_to_decimal()
         expect = 33
         result = first.head.val+first.head.next.val + first.head.next.next.val
         self.assertEqual(expect, result)

    def test_from_decimal_to_hex(self):
        first = LinkedHexNumber('A1B2')
        first = first.from_hex_to_decimal()
        first = first.from_decimal_to_hex()
        expect = "A1B2"
        result = str(first.head.val) + str(first.head.next.val) + str(first.head.next.next.val) + str(first.head.next.next.next.val)
        self.assertEqual(expect, result)

    def test_sum(self):
        first = LinkedHexNumber('ABC')
        second = LinkedHexNumber('111')
        expect = "BDF"
        result = first.sum(second).head.val+first.sum(second).head.next.val+first.sum(second).head.next.next.val
        self.assertEqual(expect, result)


if __name__ == '__main__':
    unittest.main()