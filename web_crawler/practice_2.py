# import requests
# import os
#
#
# url = "https://c-ssl.duitang.com/uploads/item/201803/09/20180309203626_qgnvp.jpeg"
# root = "C://Users//anyanqing//Pictures//本机照片//"
# path = root + url.split('/')[-1]
# try:
#     if not os.path.exists(root):
#         os.mkdir(root)
#     if not os.path.exists(path):
#         r = requests.get(url)
#         print(r.status_code)
#         r.raise_for_status()
#
#         with open(path, 'wb') as f:
#             f.write(r.content)
#             f.close()
#             print("文件保存成功")
#     else:
#         print("文件已存在")
# except:
#     print("爬取失败")


import requests


url = "http://m.ip138.com/ip.asp"
# kv = {'ip': '10.10.20.163'}
kv = {'ip': '202.204.80.112'}
try:
    r = requests.get(url, params=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print("爬取失败")

