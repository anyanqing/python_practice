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


# # 哈姆雷特词频统计
# excludes = {'a', 'an', 'for', 'the', 'you', 'and', 'to', 'of', 'i', 'my', 'in', 'you', 'that', 'it', 'is', 'his',
#             'not', 'with', 'this', 'your', 'but', 'as', 'be', 'he', 'what', 'have', 'o', 'will', 'so', 'me', 'do',
#             'are', 'him', 'our', 'by', 'if', 'on', 'or', 's', 'd', 'by', 'thou', 'they', 'there', 'from', 'her',
#             'how', 'at', 't', 'was', 'would', 'well', 'll', 'them', 'may', 'should', 'we'}
#
# special_characters = {'~', '!', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '-', '`', '{', '}', '[', ']',
#                       ':', '"', '|', '\\', '\\n', '\\s', "'", ';', '<', '>', '?', ',', '.', '/'}
#
#
# def getText(file):
#     infile = open(file, 'r', encoding='utf-8').read().strip()
#     infile_lower = infile.lower()
#     for ch in special_characters:
#         infile_lower = infile_lower.replace(ch, ' ')
#     return infile_lower
#
#
# def printWords(infile, num):
#     words = infile.split()
#     counts = {}
#     for word in words:
#         if word in excludes:
#             continue
#         counts[word] = counts.get(word, 0) + 1
#
#     items = list(counts.items())
#     items.sort(key=lambda x: x[1], reverse=True)
#     for i in range(num):
#         word, count = items[i]
#         print('{word:<10}{count:>5}'.format(word=word, count=count))
#
#
# def main():
#     hamletTxt = getText('D:\Repository\PycharmProjects\python_practice\python_course\W06\infiles\hamlet.txt')
#     printWords(hamletTxt, 20)
#
#
# if __name__ == '__main__':
#     main()


# 中文分词学习
import jieba
print(jieba.lcut('中国是一个伟大的国家'))
print(jieba.lcut("我是一条小青龙，小青龙"))
