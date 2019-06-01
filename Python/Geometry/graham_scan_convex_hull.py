"""
Convex Hull is the smallest convex polygon containing all the points of the set S. In other words, its the smallest
convex polygon P for which each point Q either lies on the boundary of P or in its interior.

Graham's Scan - O(n log n)
"""


class Point(object):
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y


def cross_product_orientation(a, b, c):
    """Returns the orientation of the set of points.
        >0 if x,y,z are clockwise, <0 if counterclockwise, 0 if co-linear.
     """

    return (b.y - a.y) * \
           (c.x - a.x) - \
           (b.x - a.x) * \
           (c.y - a.y)


def graham_scan_convex_hull(points):
    """Calculate conve hull using graham's scan algorithm.

    :param points: A set of points.
    :return convex_hull: A set of points forming convex hull.
    """
    no_of_points = len(points)

    # find bottom most point
    curr_min = 0
    for i in range(no_of_points):
        if (points[i].y < curr_min.y) or (points[i].y == curr_min.y and points[i].x < curr_min.x):
            curr_min = i

    points[0], points[curr_min] = points[curr_min], points[0]

    for i in range(no_of_points):
        pass
