# from graphics import *
# circ = Circle(Point(100, 100), 30)
# win = GraphWin()
# circ.draw(win)
#
# from graphics import *
# win = GraphWin()
# face = Circle(Point(100,95),50)
# leftEye = Circle(Point(80,80),5)
# leftEye.setFill("yellow")
# leftEye.setOutline("red")
# rightEye = Circle(Point(120,80),5)
# rightEye.setFill("yellow")
# rightEye.setOutline("red")
# mouth = Line(Point(80,110),Point(120,110))
#
# face.draw(win)
# mouth.draw(win)
# leftEye.draw(win)
# rightEye.draw(win)
#
#
# from graphics import *
#
#
# def main():
#     win = GraphWin("Click Me!")
#     for i in range(10):
#         p = win.getMouse()
#         print("You clicked at:", p.getX(), p.getY())
#
#
# if __name__ == '__main__':
#     main()


from graphics import *


def main():
    win = GraphWin("Draw a polygon", 300, 300)
    win.setCoords(0.0, 0.0, 300.0, 300.0)
    message = Text(Point(150, 20), "Click on five points")
    message.draw(win)

    # 获得多边形的五个点
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    p4 = win.getMouse()
    p4.draw(win)
    p5 = win.getMouse()
    p5.draw(win)

    # 使用Polygon对象绘制多边形
    polygon = Polygon(p1,p2,p3,p4,p5)
    polygon.setFill("peachpuff")
    polygon.setOutline("black")
    polygon.draw(win)

    # 等待响应鼠标事件，推出程序
    message.setText("Click anywhere to quit.")
    win.getMouse()


if __name__ == '__main__':
    main()
