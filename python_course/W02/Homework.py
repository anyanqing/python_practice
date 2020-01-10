# # 温度转换程序，eval()替换float()，eval()的作用是去掉一层引号
# val = input("请输入带温度表示符号的温度值（例如：32C或90F）： ")
# if val[-1] in ['C', 'c']:
#     f = 1.8 * eval(val[0:-1]) + 32
#     print("转换后的温度为：{:.2f}F".format(f))
# elif val[-1] in ['F', 'f']:
#     c = (eval(val[0:-1]) - 32) / 1.8
#     print("转换后的温度为：{:.2f}C".format(c))
# else:
#     print("输入有误")

# # 彩色蟒蛇绘制
# import turtle
#
#
# def drawSnake(rad, angle, len, neckrad):
#     color1 = ['red', 'orange', 'yellow', 'green', 'turquoise', 'blue', 'purple']
#     for i in range(len):
#         turtle.pencolor(color1[i])
#         turtle.circle(rad, angle)
#         turtle.circle(-rad, angle)
#     turtle.pencolor("black")
#     turtle.circle(rad, angle/2)
#     turtle.pencolor("pink")
#     turtle.fd(rad)
#     turtle.pencolor("gray")
#     turtle.circle(neckrad+1, 180)
#     turtle.pencolor("brown")
#     turtle.fd(rad*2/3)
#     turtle.done()
#
#
# def main():
#     turtle.setup(1300, 800, 0, 0)
#     pythonsize = 30
#     turtle.pensize(pythonsize)
#     turtle.pencolor("purple")
#     turtle.seth(-40)
#     drawSnake(40, 80, 5, pythonsize/2)
#
#
# main()

# 绘制等边三角形
import turtle


def drawEquilateralTriangle(len, angle):
    turtle.fillcolor('white')
    turtle.begin_fill()
    while True:
        turtle.fd(len)
        turtle.left(angle)
        if abs(turtle.pos()) < 1:
            break
    turtle.end_fill()
    turtle.done()


def main():
    drawEquilateralTriangle(100, 120)


main()
