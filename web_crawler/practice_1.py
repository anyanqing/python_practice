# import requests
#
#
# url = "https://www.amazon.cn/dp/B07FPFQXRR"
# try:
#     kv = {'user-agent': 'Mozilla/5.0'}  # 修改头部信息
#     r = requests.get(url, headers=kv)
#     print(r.status_code)
#     r.raise_for_status()
#     r.encoding = r.apparent_encoding
#     print(r.text[1000:2000])
#     # print(r.text)
# except:
#     print("爬取失败")


import requests


try:
    kv = {'wd': 'Python'}
    r = requests.get("http://www.baidu.com", params=kv)
    print(r.status_code)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("爬取失败")
