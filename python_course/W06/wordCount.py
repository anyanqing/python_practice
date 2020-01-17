import turtle

## 全局变量 ##
# 词频排列显示个数
count = 20
# 单词频率数组--作为y轴数据
data = []
# 单词数组--作为x轴数据
words = []
# y轴显示放大倍数--可以根据词频数量进行调节
yScale = 0.5
# x轴显示放大倍数--可以根据count数量进行调节
xScale = 30


# 从点(x1, y1)到(x2, y2)绘制线段
def drawLine(pen, x1, y1, x2, y2):
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    pen.goto(x2, y2)


# 在坐标(x, y)处写文字
def drawText(pen, x, y, text):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.write(text)


# 绘制矩形柱体
def drawRectangle(pen, x, y):
    x = x * xScale
    y = y * yScale
    drawLine(pen, x-5, 0, x-5, y)
    drawLine(pen, x-5, y, x+5, y)
    drawLine(pen, x+5, y, x+5, 0)
    drawLine(pen, x+5, 0, x-5, 0)


# 绘制多个矩形柱体
def drawBar(pen):
    for i in range(count):
        drawRectangle(pen, i+1, data[i])


# 绘制柱状图
def drawGraph(pen):
    # 绘制x/y轴线
    drawLine(pen, 0, 0, 800, 0)
    drawLine(pen, 0, 800, 0, 0)
    # x轴：坐标及描述
    for x in range(count):
        x = x + 1  # 向右移一位，为了不画在原点上
        drawText(pen, x*xScale-4, -20, words[x-1])
        drawText(pen, x*xScale-4, (data[x-1]+10)*yScale, data[x-1])
    drawBar(pen)
    turtle.done()


# 统计一行词频
def processLine(line, wordCounts):
    # 用空字符替换标点符号
    line = replacePunctuations(line)
    # 从每行获取每个词
    words = line.split()
    for word in words:
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1
    return wordCounts


# 标点符号替换为空字符
def replacePunctuations(line):
    for char in line:
        if char in '~@#$%^&*()_-+=<>?/,.:;{}[]|\'"""!`':
            line = line.replace(char, "")
        return line


# 词频排序
def wordSort(wordCounts):
    items = list(wordCounts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    return items


# 输出count个词频结果
def outputWords(items):
    for i in range(count):
        print(items[i][0] + '\t' + str(items[i][1]))
        data.append(items[i][1])
        words.append(items[i][0])


def main():
    filename = input("Please Enter a FileName:").strip()
    infile = open(filename, "r")
    # 建立一个空字典
    wordCounts = {}
    # 对每一行进行统计
    for line in infile:
        processLine(line.lower(), wordCounts)
    # 词频排序
    items = wordSort(wordCounts)
    # 输出count个词频结果
    outputWords(items)
    # 关闭文件
    infile.close()

    # 设置画布
    screen = turtle.Screen()
    screen.title("词频结果柱状图")
    screen.setup(1800, 1500, 0, 0)

    # 设置画笔
    pen = turtle.Turtle()
    # pen.hideturtle()
    pen.pensize(3)
    pen.speed(6)

    # 绘制柱状图
    drawGraph(pen)


if __name__ == '__main__':
    main()
