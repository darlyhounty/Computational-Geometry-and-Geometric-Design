from PyQt5 import *
import sys, random

from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt

long_size = 6
point_x = []
point_y = []
for i in range(long_size):
    x = random.randint(0, 1000)
    y = random.randint(0, 500)
    point_x.append(x)
    point_y.append(y)


def ccw(A_x, A_y, B_x, B_y, C_x, C_y):
    return (C_y - A_y) * (B_x - A_x) > (B_y - A_y) * (C_x - A_x)


# Return true if line segments AB and CD intersect
def intersect(A_x, A_y, B_x, B_y, C_x, C_y, D_x, D_y):
    return ccw(A_x, A_y, C_x, C_y, D_x, D_y) != ccw(B_x, B_y, C_x, C_y, D_x, D_y) and ccw(A_x, A_y, B_x, B_y, C_x, C_y) != ccw(A_x, A_y, B_x, B_y, D_x, D_y)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('draw')
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        pen = QPen(Qt.blue, 2, Qt.SolidLine)
        qp.setPen(pen)
        size = self.size()
        for i in range(long_size):
            qp.drawEllipse(point_x[i], point_y[i], 3, 3)
            print(point_x[i], point_y[i])
            # qp.drawLine(point_x[i], point_y[i], point_x[i + 1], point_x[i + 1])
        for i in range(0, long_size, 2):
            qp.drawLine(point_x[i], point_y[i], point_x[i + 1], point_y[i + 1])
            print("line:",i,i+1,point_x[i], point_y[i], point_x[i + 1], point_y[i + 1])
            #print("draw",i,i+1)
        pen = QPen(Qt.red, 2, Qt.SolidLine)
        qp.setPen(pen)
        for i in range(0, long_size, 2):
            for j in range(0, long_size,2):
                if i != j:
                    #print(i,i+1,j,j+1)
                    if intersect(point_x[i], point_y[i], point_x[i + 1], point_y[i + 1],
                                 point_x[j], point_y[j], point_y[j + 1], point_y[j + 1]):
                        #print(point_x[i], point_y[i], point_x[i + 1], point_y[i + 1],"first")
                        #print(point_x[j], point_y[j], point_x[j + 1], point_y[j + 1],"second")
                        #print(i,i+1,j,j+1)
                        qp.drawLine(point_x[i + 1], point_y[i + 1], point_x[i], point_y[i])
                        qp.drawLine(point_y[j + 1], point_y[j + 1], point_x[j], point_y[j])

        # for i in range(0, long_size, 2):
        #     for j in range(i+2, long_size,2):
        #         if i != j:
        #             print(i,i+1,j,j+1)
        #             if intersect(point_x[i], point_y[i], point_x[i + 1], point_y[i + 1],
        #                          point_x[j], point_y[j], point_y[j + 1], point_y[j + 1]):
        #                 print(i,i+1,j,j+1)
        #                 qp.drawLine(point_x[i], point_y[i], point_x[i + 1], point_y[i + 1])
        #                 qp.drawLine(point_x[j], point_y[j], point_y[j + 1], point_y[j + 1])
                    #if intersect(point_x[i],point_y[i],point_x[j],point_y[j])

            # if intersects(point_x[i],point_y[i],point_x[j],point_y[j])==0:
            #     qp.drawLine(point_x[i], point_y[i], point_x[i + 1], point_y[i + 1])
        # qp.drawLine(point_x[1], point_y[1], point_x[3], point_x[3])
        qp.setPen(Qt.red)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    #print(intersect(0,0,2,3,2,0,0,3))
