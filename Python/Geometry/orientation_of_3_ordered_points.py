# coding=utf-8
from __future__ import print_function

"""
Orientation of an ordered triplet of points in the plane can be
1. counterclockwise
2. clockwise
3. collinear

If orientation of (p1, p2, p3) is collinear, then orientation of (p3, p2, p1) is also collinear.
If orientation of (p1, p2, p3) is clockwise, then orientation of (p3, p2, p1) is counterclockwise and
    vice versa is also true.

Slope of line segment (p1, p2): σ = (y2 - y1)/(x2 - x1)
Slope of line segment (p2, p3): τ = (y3 - y2)/(x3 - x2)

If  σ < τ, the orientation is counterclockwise (left turn)
If  σ = τ, the orientation is collinear
If  σ > τ, the orientation is clockwise (right turn)

Using above values of σ and τ, we can conclude that,
the orientation depends on sign of  below expression:

(y2 - y1)*(x3 - x2) - (y3 - y2)*(x2 - x1)

Above expression is negative when σ < τ, i.e., counterclockwise
Above expression is 0 when σ = τ, i.e., collinear
Above expression is positive when σ > τ, i.e., clockwise
"""


class Point(object):
    """
    Structure for point
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y


def orientation(point_1, point_2, point_3):
    """
    Method to find orientation of three points

    :param point_1: First point
    :param point_2: Second point
    :param point_3: Third point

    :return orientation: String denoting orientation of points
    """

    value = (point_2.y - point_1.y) * (point_3.x - point_2.x) - \
            (point_2.x - point_1.x) * (point_3.y - point_2.y)

    print(value)
    return 'collinear' if value == 0 \
        else 'clockwise' if value > 0 else 'counter clockwise'


p_1 = Point(0, 0)
p_2 = Point(4, 4)
p_3 = Point(1, 2)

result = orientation(p_1, p_2, p_3)
expected_result = 'counter clockwise'

print('These points are:', result)
assert result == expected_result
