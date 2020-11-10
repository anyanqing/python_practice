
datas = [{"aaa": 111, "bbb": 222}, {"aaa": 333, "bbb": 444}]

for data in datas:
    data.update({"aaa": 999})
    data.update({"ccc": 000})

print(datas)

# from urllib.parse import quote, unquote
# url = 'file://appform/headimg/202009/3a5c9a44da244f9a921e969cabf1fb1f_简历照片 蒋志宇.jpg?belong=pHh0xxxxxe'.encode('utf8')
# print(url)
# q_url = 'http://api-t2.dqprism.com/user/v4/headimg/auth?url={url}&userId=0&hrId=94968&appid=A11005&interfaceid=A11005001'.format(url=quote(url))
# print(q_url)
