import turtle


def drawSnake(rad, angle, len, neckrad):
    for i in range(len):
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle/2)
    turtle.fd(rad)  # 小海龟往前走rad距离
    turtle.circle(neckrad+1, 180)
    turtle.fd(rad*2/3)  # 小海龟往前走2/3*rad距离
    turtle.done()


def main():
    turtle.setup(1300, 800, 0, 0)
    pythonsize = 30
    turtle.pensize(pythonsize)
    turtle.pencolor("blue")
    turtle.seth(-40)
    drawSnake(40, 80, 5, pythonsize/2)


main()
