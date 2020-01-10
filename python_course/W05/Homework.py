import turtle
import time

p = turtle.Turtle()


def drawSegmentGap(segment_gap):  # 每条线段之间的间隙
    p.penup()
    p.forward(segment_gap)


def drawDigitGap(digit_gap):  # 每个数字之间的间隙，画笔转向
    p.penup()
    p.forward(digit_gap)
    p.left(90)


def drawSegment(draw, segment_len, segment_gap):  # 画线段
    drawSegmentGap(segment_gap)
    p.pendown() if draw else p.penup()
    p.forward(segment_len)
    drawSegmentGap(segment_gap)


def drawDigit(digit, segment_len, segment_gap, digit_gap):  # 绘制数字

    drawDigitGap(digit_gap)

    drawSegment(True, segment_len, segment_gap) \
        if digit in [0, 4, 5, 6, 8, 9] else drawSegment(False, segment_len, segment_gap)  # f

    p.right(90)
    drawSegment(True, segment_len, segment_gap) \
        if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawSegment(False, segment_len, segment_gap)  # a

    p.right(90)
    drawSegment(True, segment_len, segment_gap) \
        if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawSegment(False, segment_len, segment_gap)  # b

    drawSegment(True, segment_len, segment_gap) \
        if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawSegment(False, segment_len, segment_gap)  # c

    p.right(90)
    drawSegment(True, segment_len, segment_gap) \
        if digit in [0, 2, 3, 5, 6, 8, 9] else drawSegment(False, segment_len, segment_gap)  # d

    p.right(90)
    drawSegment(True, segment_len, segment_gap) \
        if digit in [0, 2, 6, 8] else drawSegment(False, segment_len, segment_gap)  # e

    p.right(90)
    drawSegment(True, segment_len, segment_gap) \
        if digit in [2, 3, 4, 5, 6, 8, 9] else drawSegment(False, segment_len, segment_gap)  # g


def drawDot(segment_gap, segment_len):  # 画小数点
    diameter = segment_gap  # 圆直径
    # 箭头由右向下转，并前进segment_gap + segment_len + diameter距离
    p.right(90)
    p.penup()
    p.forward(segment_gap + segment_len + diameter)
    # 箭头转向右，并前进diameter距离
    p.left(90)
    p.forward(diameter)
    # 画圆，颜色跟前面数字颜色保持一致
    p.dot(diameter)
    # 箭头转向上，并前进segment_gap + segment_len距离，回到画数字的原点，转向右
    p.left(90)
    drawSegment(False, segment_len, segment_gap)
    p.right(90)


def drawDate(date, segment_len, segment_gap, digit_gap,
             hideturtle=True, speed=10, y_color='red', m_color='green', d_color='blue'):  # 绘制日期
    p.hideturtle() if hideturtle else p.showturtle()
    p.pensize(segment_gap)
    p.speed(speed)
    p.pencolor(y_color)
    for i in date:
        if i == '-':
            p.forward(digit_gap)  # 左间距
            p.write("年", font=('Arial', segment_gap * 2, 'normal'))
            p.forward(digit_gap + segment_gap)  # 右间距
            p.pencolor(m_color)  # 设置后面数字的颜色
        elif i == '+':
            p.forward(digit_gap)
            p.write("月", font=('Arial', segment_gap * 2, 'normal'))
            p.forward(digit_gap + segment_gap)
            p.pencolor(d_color)
        elif i == '=':
            p.forward(digit_gap)
            p.write("日", font=('Arial', segment_gap * 2, 'normal'))
            p.forward(digit_gap + segment_gap)
        else:
            drawDigit(eval(i), segment_len, segment_gap, digit_gap)
            drawDot(segment_gap, segment_len)


def goto_xy(x, y):  # 移动到绝对坐标(x,y)处
    p.penup()
    p.goto(x, y)


def main():
    turtle.setup(1600, 800, 0, 0)
    date = time.strftime('%Y-%m+%d=', time.localtime())

    goto_xy(-500, 0)
    drawDate(date, 40, 10, 15)

    goto_xy(-500, -200)
    drawDate(date, 40, 10, 15, hideturtle=False, speed=1)

    turtle.done()


main()
