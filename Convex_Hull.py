import sys, random
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from functools import cmp_to_key

point_output_x = []
point_output_y = []


# A class used to store the x and y coordinates of points
class Point:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y


# A global point needed for sorting points with reference
# to the first point
p0 = Point(0, 0)


# A utility function to find next to top in a stack
def nextToTop(S):
    return S[-2]


# A utility function to return square of distance
# between p1 and p2
def distSq(p1, p2):
    return ((p1.x - p2.x) * (p1.x - p2.x) +
            (p1.y - p2.y) * (p1.y - p2.y))


# To find orientation of ordered triplet (p, q, r).
# The function returns following values
# 0 --> p, q and r are collinear
# 1 --> Clockwise
# 2 --> Counterclockwise
def orientation(p, q, r):
    val = ((q.y - p.y) * (r.x - q.x) -
           (q.x - p.x) * (r.y - q.y))
    if val == 0:
        return 0  # collinear
    elif val > 0:
        return 1  # clock wise
    else:
        return 2  # counterclock wise


# A function used by cmp_to_key function to sort an array of
# points with respect to the first point
def compare(p1, p2):
    # Find orientation
    o = orientation(p0, p1, p2)
    if o == 0:
        if distSq(p0, p2) >= distSq(p0, p1):
            return -1
        else:
            return 1
    else:
        if o == 2:
            return -1
        else:
            return 1


# Prints convex hull of a set of n points.
def convexHull(points, n):
    # Find the bottommost point
    ymin = points[0].y
    min = 0
    for i in range(1, n):
        y = points[i].y

        # Pick the bottom-most or chose the left
        # most point in case of tie
        if ((y < ymin) or
                (ymin == y and points[i].x < points[min].x)):
            ymin = points[i].y
            min = i

    # Place the bottom-most point at first position
    points[0], points[min] = points[min], points[0]

    # Sort n-1 points with respect to the first point.
    # A point p1 comes before p2 in sorted output if p2
    # has larger polar angle (in counterclockwise
    # direction) than p1
    p0 = points[0]
    points = sorted(points, key=cmp_to_key(compare))

    # If two or more points make same angle with p0,
    # Remove all but the one that is farthest from p0
    # Remember that, in above sorting, our criteria was
    # to keep the farthest point at the end when more than
    # one points have same angle.
    m = 1  # Initialize size of modified array
    for i in range(1, n):

        # Keep removing i while angle of i and i+1 is same
        # with respect to p0
        while ((i < n - 1) and
               (orientation(p0, points[i], points[i + 1]) == 0)):
            i += 1

        points[m] = points[i]
        m += 1  # Update size of modified array

    # If modified array of points has less than 3 points,
    # convex hull is not possible
    if m < 3:
        return

    # Create an empty stack and push first three points
    # to it.
    S = []
    S.append(points[0])
    S.append(points[1])
    S.append(points[2])

    # Process remaining n-3 points
    for i in range(3, m):

        # Keep removing top while the angle formed by
        # points next-to-top, top, and points[i] makes
        # a non-left turn
        while ((len(S) > 1) and
               (orientation(nextToTop(S), S[-1], points[i]) != 2)):
            S.pop()
        S.append(points[i])

    # Now stack has the output points,
    # print contents of stack
    while S:
        p = S[-1]
        point_output_x.append(int(p.x))
        point_output_y.append(int(p.y))
        S.pop()

long_size=10
point_x = [0]
point_y = [0]
for i in range(long_size):
    x = random.uniform(10, 1500)
    y = random.uniform(10, 1000)
    point_x.append(x)
    point_y.append(y)
input_points = list(zip(point_x, point_y))
points = []
for point in input_points:
    points.append(Point(point[0], point[1]))
n = len(points)
convexHull(points, n)
print(len(point_output_x))
print(point_output_y)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        # self.button = QPushButton("input here", self)
        # self.button.pressed.connect(self.paintEvent)
        # self.button.released.connect(self.paintEvent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('convex hull')
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        pen = QPen(Qt.blue)
        size = self.size()
        for i in range(long_size):
            qp.drawEllipse(int(point_x[i]), int(point_y[i]), 3, 3)

        qp.setPen(Qt.red)
        for i in range(len(point_output_x)):
            qp.drawLine(point_output_x[i - 1], point_output_y[i - 1], point_output_x[i], point_output_y[i])
            qp.drawEllipse(point_output_x[i - 1], point_output_y[i - 1], 3, 3)

        print(point_output_x[len(point_output_x) - 1], point_output_y[len(point_output_x) - 1])
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
