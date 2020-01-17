# 读取文件
file_tele = open(".\infiles\TeleAddressBook.txt", "rb")
file_email = open(".\infiles\EmailAddressBook.txt", "rb")

# 跳过第一行
file_tele.readline()
file_email.readline()

# 读取实际数据
lines_tele = file_tele.readlines()
lines_email = file_email.readlines()

# 建立空字典用于存储姓名、电话、Email：
dict_tele = {}
dict_email = {}

# 获取TeleAddressBook.txt中的信息：
for line in lines_tele:
    elements = line.split()
    dict_tele[elements[0]] = str(elements[1].decode('gbk'))

for line in lines_email:
    elements = line.split()
    dict_email[elements[0]] = str(elements[1].decode('gbk'))

# 合并处理
lines = ['姓名\t电话\t\t邮箱\n']
# 按索引方式遍历list1_name
for key in dict_tele:
    s = ''
    if key in dict_email:
        s = '\t'.join([str(key.decode('gbk')), dict_tele[key], dict_email[key]])
        s += '\n'
    else:
        s = '\t'.join([str(key.decode('gbk')), dict_tele[key], str('---------------')])
        s += '\n'
    lines.append(s)

# 处理list2_name中剩余的行
for key in dict_email:
    s = ''
    if key not in dict_tele:
        s = '\t'.join([str(key.decode('gbk')), str('-----------'), dict_email[key]])
        s += '\n'
    lines.append(s)

# 将新生成的合并数据写入新的文件中
file_tele_email = open(".\outfiles\AddressBookDict.txt", "w")
file_tele_email.writelines(lines)

# 关闭文件
file_tele.close()
file_email.close()
file_tele_email.close()

print("The addressBooks are merged!")

