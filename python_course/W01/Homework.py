# # 字符串拼接
# name = input("请输入一个人的名字：")
# country = input("请输入一个国家的名字：")
# print("世界这么大，{name}想去{country}看看。".format(name=name, country=country))

# # 整数序列求和
# n = input("请输入整数N：")
# sum = 0
# for i in range(int(n)):
#     sum += i + 1
# print("1到N求和结果：", sum)

# # 九九乘法表输出
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("{j}*{i}={r:<2d} ".format(j=j, i=i, r=i*j), end='')
#     print()  # 利用函数中 end='\n' 参数，充当换行的作用

# # 阶乘计算
# sum, tmp = 0, 1
# for i in range(1, 11):
#     tmp *= i
#     sum += tmp
# print("运算结果是：{res}".format(res=sum))

# # 猴子吃桃
# n = 1
# for i in range(5, 0, -1):
#     n = 2 * (n + 1)
# print(n)

# # 健康食谱输出.列出5中不同的食材，请输出它们可能组成的所有菜式名称。
# diet = ['西红柿', '花椰菜', '黄瓜', '牛排', '虾仁']
# for x in range(0, 5):
#     for y in range(x+1, 5):
#         print("{0}{1}".format(diet[x], diet[y]))

# # 五角星的绘制
# from turtle import *
# fillcolor("red")
# begin_fill()
# while True:
#     forward(200)
#     right(144)
#     # 查看画笔是否回到原点，回到原点时为真，则退出循环
#     if abs(pos()) < 1:  # 小海龟几乎回到远点，1单位是像素，几乎是0，就是说回到出发点。
#         break
# end_fill()
# done()

# # 太阳花的绘制
# from turtle import *
# color("red", "yellow")
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()

# # 螺旋线绘制
# import turtle
# import time
# turtle.speed("fastest")
# turtle.pensize(2)
# for x in range(400):
#     turtle.forward(2*x)
#     turtle.left(90)
# time.sleep(3)
# turtle.done()

# 彩色螺旋线的绘制
import turtle
turtle.pensize(2)
# turtle.speed("fastest")
turtle.bgcolor("black")
colors = ["red", "yellow", "purple", "blue"]
turtle.tracer(False)
for x in range(400):
    turtle.forward(2*x)
    turtle.color(colors[x % 4])
    turtle.left(91)
turtle.tracer(True)
turtle.done()
