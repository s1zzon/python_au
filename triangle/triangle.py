import math
import sys


def get_all_lines_from_file(file_name):
    file = open(file_name)
    lines = file.readlines()
    return lines


class Point:
    def __init__(self, coordinates_in_string):
        self.X = float(coordinates_in_string.split(' ')[0])
        self.Y = float(coordinates_in_string.split(' ')[1])


def length(first_point, second_point):
    return math.sqrt((first_point.X - second_point.X) ** 2 + (first_point.Y - second_point.Y) ** 2)


class Triangle:
    def __init__(self, p1, p2, p3):
        self.l1 = length(p1, p2)
        self.l2 = length(p2, p3)
        self.l3 = length(p3, p1)

    def is_this_triangle_isosceles(self):
        if self.l1 == self.l2 or self.l2 == self.l3 or self.l3 == self.l1:
            return True
        else:
            return False

    def is_this_triangle_exists(self):
        if (max(self.l1, self.l2, self.l3) < self.l1 + self.l2 and
                max(self.l1, self.l2, self.l3) < self.l2 + self.l3 and
                max(self.l1, self.l2, self.l3) < self.l1 + self.l3):
            return False
        else:
            return True

    def square(self):
        p = (self.l1 + self.l2 + self.l3) / 2
        s = math.sqrt(p * (p - self.l2) * (p - self.l2) * (p - self.l3))
        return s


def create_triangle(line):
    line = line.rstrip('\n')
    p1 = Point(line)
    line = ' '.join(line.split(' ')[2:])
    p2 = Point(line)
    line = ' '.join(line.split(' ')[4:])
    p3 = Point(line)
    return Triangle(p1, p2, p3)
