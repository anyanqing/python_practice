
# while True:
#     height = eval(input("请输入您的身高(m):"))
#     weight = eval(input("请输入您的体重(kg):"))
#
#     if weight and height:
#         BMI = weight / height**2
#         print("您的BMI值为：{BMI:.2f}，正常的BMI指标区间为：国际18.5~25，国内18.5~24。".format(BMI=BMI))
#         if input("是否需要继续？是Y，否N：")[0].lower() == 'y':
#             continue
#         else:
#             break
#     else:
#         print("请重新输入您的身高(m)和体重(kg)!")

# if BMI < 18.5:
#     print("您目前体质偏瘦！请多增加营养摄入。。。")
# elif BMI <= 24:
#     print("恭喜！！！您目前体质正常，继续保持哦。。。")
# elif BMI <= 25:
#     print("按照国际标准来讲，您目前体质正常，但是按照国内标准来讲，您已偏胖，建议适当控制饮食，多多运动哦。。。")
# elif BMI < 28:
#     print("您目前体质偏胖，建议适当控制饮食，多多运动哦。。。")
# elif BMI < 30:
#     print("按照国际标准来讲，您目前体质偏胖，但是按照国内标准来讲，您已达到肥胖，建议严格控制饮食，加大运动量哦。。。")
# else:
#     print("您目前体质已达肥胖，建议严格控制饮食，加大运动量哦。。。")

score = eval(input("请输入你的分数："))

if score >= 90.0:
    grade = 'A'
elif score >= 80.0:
    grade = 'C'
elif score >= 70.0:
    grade = 'B'
elif score >= 60.0:
    grade = 'D'
else:
    grade = 'E'
print(grade)
