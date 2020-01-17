# # 1、理解文本和二进制打开方式的区别
# infile_txt = open(".\infiles\\test.txt", mode="r", encoding='utf-8')
# infile_bin = open(".\infiles\\test.txt", mode="rb")
#
# lines_txt = infile_txt.read()
# lines_bin = infile_bin.read()
#
# print(lines_txt)
# print(lines_bin.decode('utf-8'))

# # 文件处理
# dict = {}
# fo = open('.\infiles\TeleAddressBook.txt', 'r', encoding='gbk')
# fo.readline()  # 去掉第一行
# for line in fo:
#     # 处理一行数据
#     elem = line.split()
#     dict[elem[0]] = elem[1]
# print(dict)
# fo.close()

