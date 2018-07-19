# coding=utf-8
from __future__ import print_function

"""
Area of polygon given ordered coordinates of a polygon with n vertices. Find area of the polygon. Here ordered mean
that the coordinates are given either in clockwise manner or anticlockwise from first vertex to last.

We can compute area of a polygon using Shoelace formula.

Area =  | 1/2 [ (x1*y2 + x2*y3 + ... + xn-1*yn + xn*y1) -
           (x2*y1 + x3*y2 + ... + xn*yn-1 + x1*yn) ] |
"""


class Point(object):
    """
    Structure for point
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y


def polygon_area(points):
    """
    Method to calculate area of polygon using shoelace formula

    :param points: A set of tuples having  and y coordinates of points
    :return area: Integer area of polygon
    """
    no_of_cord = len(points)
    area = 0.0

    j = no_of_cord - 1
    for i in range(no_of_cord):
        area += (points[j].x + points[i].x) * (points[j].y - points[i].y)
        j = i

    return int(abs(area) / 2.0)


points = [Point(0, 1), Point(2, 3), Point(4, 7)]
expected_answer = 2
result = polygon_area(points)

print('Calculated area of Polygon:', result)
assert result == expected_answer
