import requests

import json

import pandas as pd

input = pd.read_excel(r'AMap_adcode_citycode.xlsx')


def coords(cityname, citycode):
    # 输入API问号前固定不变的部分
    url = 'https://restapi.amap.com/v3/geocode/geo'

    # 将两个参数放入字典
    params = {'key': 'e9698c1e0ee5dd69fb37ecd65440134c',
              'address': cityname,
              'city': citycode}

    res = requests.get(url, params)

    jd = json.loads(res.text)

    return jd['geocodes'][0]['adcode']+','+jd['geocodes'][0]['location']


def text_save(output, data):  # output为写入CSV文件的路径，data为要写入数据列表.

    file = open(output, 'a')
    s = str(data)

    file.write(s)
    file.write('\n')

    file.close()


for row in range(0, input.shape[0]):
    cityname = input['中文名'][row]
    citycode = input['citycode'][row]
    # print(cityname, citycode)
    try:
        out = coords(cityname, citycode)
    except:
        out = 0
    # out='adcode'+','+'lng'+','+'lat'
    print(out)
    text_save('output_latitude&longitude_2', out)


# # test
# out = coords('朝阳区', '010')
# print(out)
# text_save('output_test', out)
