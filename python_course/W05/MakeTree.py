
import turtle

# # 绘制并填充一个五角星
# p = turtle.Turtle()
# p.speed(3)
# p.pensize(3)
# p.color("black", "red")
# p.begin_fill()
# for i in range(5):
#     p.forward(200)
#     p.right(144)
# p.end_fill()
# turtle.done()


# 树的绘制
def tree(plist, l, a, f):
    """
    :param plist: list of pens
    :param l: length of branch
    :param a: half of the angle between 2 branches
    :param f: factor by which branch is shortened
    :return:
    """
    if l > 5:
        lst = []
        for p in plist:
            p.forward(l)
            q = p.clone()
            p.left(a)
            q.right(a)
            lst.append(p)
            lst.append(q)
        tree(lst, l*f, a, f)


def makeTree(x, y):
    p = turtle.Turtle()
    p.color("green")
    p.pensize(3)
    p.hideturtle()
    # p.getscreen().tracer(30, 0)
    p.speed(30)
    p.left(90)
    p.penup()
    p.goto(x, y)
    p.pendown()
    tree([p], 200, 65, 0.6375)
    turtle.done()


def main():
    makeTree(0, -200)


main()
