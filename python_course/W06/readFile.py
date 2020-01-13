# # 写入文件
# outfile = open('./outfiles/outfile.txt', 'w')
# outfile.write("Hello\nnihao")
# outfile.close()

# # 读取文件
# infile = open('./outfiles/outfile.txt', 'r')
# data = infile.read()
# infile.close()
# print(data)

# 遍历文件，通用代码框架
someFile = ""
file = open(someFile, 'r')
for line in file:
    # 处理一行文件内容
    print(line)
file.close()
