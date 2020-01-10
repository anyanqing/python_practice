from random import random, seed
from math import sqrt
from time import perf_counter

DARTS = 1200
hits = 0
perf_counter()
for i in range(1, DARTS):
    x, y = random(), random()
    dist = sqrt(x**2 + y**2)
    if dist <= 1.0:
        hits += 1
pi = 4 * (hits/DARTS)
print("Pi的值是 {pi}".format(pi=pi))
print("程序运行时间是 {second:>10.5f}s".format(second=perf_counter()))


'''
    format()方法
    {<参数名称或序号>:<格式控制标记>}
    <格式控制标记>格式：
        <填充><对齐><宽度>,<.精度><类型>
'''
# seed(1)
# print("程序运行时间是 {second:s>30,.3f}s".format(second=random()*10000000000000000))
# seed(1)
# print("程序运行时间是 {second:s>30,.3%}s".format(second=random()*10000000000000000))
# print("程序运行时间是 {second:s>30.0}s".format(second="123456789"))
# print("程序运行时间是 {second:s>30.3}s".format(second="123456789"))
# print("程序运行时间是 {second:s>30.10}s".format(second="123456789"))
