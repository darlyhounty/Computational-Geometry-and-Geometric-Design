#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "dialog.h"
#include <QRandomGenerator>
#include <QMouseEvent>
#include <QGraphicsView>
#include <QRubberBand>
#include "qcustomplot.h"
#include <QLineEdit>
#include <QTextEdit>
extern QString globaldata;
MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{

    delete ui;
}

void MainWindow::paintEvent(QPaintEvent*)
{
    QPen pen;
    QPainter painter(this);
    pen.setWidth(2);
    for(int i=0;i<1000001;i++){//1000001

        pen.setColor(QColor(QRandomGenerator::global()->bounded(255),QRandomGenerator::global()->bounded(255)
                            ,QRandomGenerator::global()->bounded(255)
                            ,QRandomGenerator::global()->bounded(255)));
        painter.setPen(pen);
        painter.drawPoint(QRandomGenerator::global()->bounded(1800),QRandomGenerator::global()->bounded(1200));
    }

}

void MainWindow::mousePressEvent(QMouseEvent *event)
{
    origin = event->pos();
    if (!rubberBand)
        rubberBand = new QRubberBand(QRubberBand::Rectangle, this);
    rubberBand->setGeometry(QRect(origin, QSize()));
    rubberBand->show();
}

void MainWindow::mouseMoveEvent(QMouseEvent *event)
{
    rubberBand->setGeometry(QRect(origin, event->pos()).normalized());
}

void MainWindow::mouseReleaseEvent(QMouseEvent *event)
{
    rubberBand->hide();
    // determine selection, for example using QRect::intersects()
    // and QRect::contains().
}






