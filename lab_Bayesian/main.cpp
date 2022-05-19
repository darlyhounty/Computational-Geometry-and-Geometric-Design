#include "mainwindow.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    BezierCurve w;
    w.show();
    return app.exec();
}
