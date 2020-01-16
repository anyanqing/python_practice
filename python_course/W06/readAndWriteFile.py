# # 写入文件
# outfile = open('./outfiles/outfile.txt', 'w')
# outfile.write("Hello\nnihao")
# outfile.close()

# # 读取文件
# infile = open('./outfiles/outfile.txt', 'r')
# data = infile.read()
# infile.close()
# print(data)

# # 遍历文件，通用代码框架
# someFile = ""
# file = open(someFile, 'r')
# for line in file:
#     # 处理一行文件内容
#     print(line)
# file.close()

# 文件拷贝
def main():
    # 用户输入文件名
    f1 = input("Enter a source file:").strip()
    f2 = input("Enter a source file:").strip()

    # 打开文件
    infile = open(f1, "r")
    outfile = open(f2, "w")

    # 拷贝数据
    countlines = countchars = 0
    for line in infile:
        countlines += 1
        countchars += len(line)
        outfile.write(line)
    print(countlines, "lines and", countchars, "chars copied.")

    infile.close()
    outfile.close()


main()
