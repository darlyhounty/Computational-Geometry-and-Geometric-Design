#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QWidget>
#include <QPainter>
#include <QPen>
#include <QRubberBand>
#include <QLineEdit>
#include <QPushButton>
#include <QTextEdit>
QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();
public:
    void paintEvent(QPaintEvent*);
    void mousePressEvent(QMouseEvent*event);
    void mouseMoveEvent(QMouseEvent*event);
    void mouseReleaseEvent(QMouseEvent*event);

private:
    Ui::MainWindow *ui;
private:
    QRubberBand *rubberBand=nullptr;
    QPoint origin;
};
#endif // MAINWINDOW_H
