import turtle

# 设置画布窗口信息
screen = turtle.Screen()
screen.title("数据驱动的动态路径绘制")
screen.setup(800, 600, 0, 0)

# 设置画笔
pen = turtle.Turtle()
pen.shape("turtle")
pen.pensize(5)
pen.speed(6)

# 读取文件信息
result = []
file = open(".\infiles\data.txt", "r")
for line in file:
    result.append(list(map(float, line.split(','))))
print(result)

# 根据文件数据画图
for i in range(len(result)):
    pen.color((result[i][3], result[i][4], result[i][5]))
    pen.forward(result[i][0])
    if result[i][1]:
        pen.right(result[i][2])
    else:
        pen.left(result[i][2])
turtle.done()
