# 读取文件
file_tele = open(".\infiles\TeleAddressBook.txt", "rb")
file_email = open(".\infiles\EmailAddressBook.txt", "rb")

# 跳过第一行
file_tele.readline()
file_email.readline()

# 读取实际数据
lines_tele = file_tele.readlines()
lines_email = file_email.readlines()

# 建立空列表用于存储姓名、电话、Email：
list1_name = []
list1_tele = []
list2_name = []
list2_email = []

# 获取TeleAddressBook.txt中的信息：
for line in lines_tele:
    elements = line.split()
    list1_name.append(str(elements[0].decode('gbk')))
    list1_tele.append(str(elements[1].decode('gbk')))

for line in lines_email:
    elements = line.split()
    list2_name.append(str(elements[0].decode('gbk')))
    list2_email.append(str(elements[1].decode('gbk')))

# 合并处理
lines = ['姓名\t电话\t\t邮箱\n']
# 按索引方式遍历list1_name
for i in range(len(list1_name)):
    s = ''
    if list1_name[i] in list2_name:
        j = list2_name.index(list1_name[i])  # 找到list1_name对应list2_name中的索引位置
        s = '\t'.join([list1_name[i], list1_tele[i], list2_email[j]])
        s += '\n'
    else:
        s = '\t'.join([list1_name[i], list1_tele[i], str('---------------')])
        s += '\n'
    lines.append(s)

# 处理list2_name中剩余的行
for i in range(len(list2_name)):
    s = ''
    if list2_name[i] not in list1_name:
        s = '\t'.join([list2_name[i], str('-----------'), list2_email[i]])
        s += '\n'
    lines.append(s)

# 将新生成的合并数据写入新的文件中
file_tele_email = open(".\outfiles\AddressBookList.txt", "w")
file_tele_email.writelines(lines)

# 关闭文件
file_tele.close()
file_email.close()
file_tele_email.close()

print("The addressBooks are merged!")

