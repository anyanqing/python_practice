
for i in range(3):
    val = input("请输入带温度表示符号的温度值（例如：32C或90F）： ")
    if val[-1] in ['C', 'c']:
        f = 1.8 * float(val[0:-1]) + 32
        print("转换后的温度为：%.2fF" % f)
        print("转换后的温度为：{:.2f}F".format(f))
    elif val[-1] in ['F', 'f']:
        c = (float(val[0:-1]) - 32) / 1.8
        print("转换后的温度为：%.2fC" % c)
        print("转换后的温度为：{:.2f}C".format(c))
    else:
        print("输入有误")
