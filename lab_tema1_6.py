import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPalette, QPolygon, QBrush, QPainter, QColor
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPolygonItem, QMainWindow, QApplication, QWidget, QScrollArea
from PyQt5.QtWidgets import QGraphicsView

points = []


def is_in_poly(p, poly):

    px, py = p
    is_in = False
    for i, corner in enumerate(poly):
        next_i = i + 1 if i + 1 < len(poly) else 0
        x1, y1 = corner
        x2, y2 = poly[next_i]
        if (x1 == px and y1 == py) or (x2 == px and y2 == py):  # if point is on vertex
            is_in = True
            break
        if min(y1, y2) < py <= max(y1, y2):  # find horizontal edges of polygon
            x = x1 + (py - y1) * (x2 - x1) / (y2 - y1)
            if x == px:  # if point is on edge
                is_in = True
                break
            elif x > px:  # if point is on left-side of line
                is_in = not is_in
    return is_in


class Window(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.polygon = None
        self.setFixedSize(1200, 800)
        self.bu = 0
        self.yes=0

    def mousePressEvent(self, ev):
        print(points)
        if ev.button() == QtCore.Qt.RightButton:
            self.polygon = QPolygon([QPoint(points[i][0], points[i][1]) for i in range(0, len(points))])
            self.bu = 1
            self.update()
        else:
            print(self.polygon)
            if self.polygon is None:
                self.polygon = QtGui.QPolygon()
            self.polygon << ev.pos()
            points.append([ev.x(), ev.y()])
            self.update()

    def mouseMoveEvent(self, ev):
        self.setMouseTracking(True)
        # painter.setBrush(QBrush(QtCore.Qt.red))
        #print(ev.x(), ev.y())
        if is_in_poly([ev.x(), ev.y()], points) == 1:
            print("Point:(",ev.x(),",", ev.y(),") inside the polygon")
            self.yes==1
            painter = QPainter(self)
            painter.drawPolygon(self.polygon)
            painter.setBrush(QColor(122, 163, 39))
        else:
            print("Point:(",ev.x(),",", ev.y(),") outside the polygon")

    def paintEvent(self, ev):
        painter = QPainter(self)
        if self.polygon is not None:
            painter.setPen(QtCore.Qt.blue)
            painter.drawPolyline(self.polygon)

        if self.bu == 1:
            print("XXXXXXXXXXXXXXXXXXXXXXX")
            painter.drawPolygon(self.polygon)
            painter.setBrush(QColor(122, 163, 39))

app = QApplication(sys.argv)
GUI = Window()  # CityscapesLabelTool()
GUI.show()
sys.exit(app.exec_())
