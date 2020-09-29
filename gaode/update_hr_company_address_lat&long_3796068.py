import requests
import json
import pymysql
from sshtunnel import SSHTunnelForwarder


list_address_missing_records_fields = []


def get_mysql_company_address_record(company_id):
    # conn = pymysql.connect(host='db-d.dqprism.com', port=3306, user='daqi', password='7f1a45eac5985519829c929e7bbf0557')  # 沙盒
    # SSH隧道
    server = SSHTunnelForwarder(
        # 指定ssh登录的跳板机的address
        ssh_address_or_host=('devold.dqprism.com', 22),
        # 跳板机的用户
        ssh_username='wengjianfei',
        # # 连接跳板机的私钥
        # ssh_pkey='ZUalYqE0rH3crFs3',
        # 数据库密码
        ssh_password='ZUalYqE0rH3crFs3',
        # 远程数据库的地址和端口
        remote_bind_address=('rr-2zehn9v0te8409164.mysql.rds.aliyuncs.com', 3306)
    )
    server.start()
    conn = pymysql.connect(host='127.0.0.1', port=server.local_bind_port, user='readonly', password='MoSeeker')  # 线上

    cursor = conn.cursor()
    sql = '''
        select
                a.id
                ,a.address_name
                ,a.company_id
                ,a.province
                ,a.city
                ,a.region
                ,a.address
                ,a.department_id
                ,a.address_type
                ,a.disable
                ,concat(b.name, c.name, a.address) as address_2
        from hrdb.hr_company_address a
        left join dictdb.dict_city b on a.province=b.code
        left join dictdb.dict_city c on a.city=c.code
        where a.company_id={company_id} and a.disable=1 and (a.longitude is null or a.latitude is null)
        ;
    '''.format(company_id=company_id)

    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    server.close()
    print(results)
    for result in results:

        dict_address_missing_record_fields = {}

        dict_address_missing_record_fields['id'] = result[0]
        dict_address_missing_record_fields['addressName'] = result[1]
        dict_address_missing_record_fields['companyId'] = result[2]
        dict_address_missing_record_fields['province'] = result[3]
        dict_address_missing_record_fields['city'] = result[4]
        dict_address_missing_record_fields['region'] = result[5]
        dict_address_missing_record_fields['address'] = result[6]
        dict_address_missing_record_fields['departmentId'] = result[7]
        dict_address_missing_record_fields['addressType'] = result[8]
        dict_address_missing_record_fields['disable'] = result[9]
        dict_address_missing_record_fields['address_2'] = result[10]

        print(dict_address_missing_record_fields)
        list_address_missing_records_fields.append(dict_address_missing_record_fields)

    print(list_address_missing_records_fields)
    return list_address_missing_records_fields


def get_longitude_latitude_data(address):
    gaode_url = "https://restapi.amap.com/v3/geocode/geo"
    gaode_params = {'key': 'e9698c1e0ee5dd69fb37ecd65440134c', 'address': address}
    result = requests.get(url=gaode_url, params=gaode_params)
    # json.loads()函数是将字符串转化为字典，json.dumps()相反
    dict_result = json.loads(result.text)
    longitude, latitude = dict_result['geocodes'][0]['location'].split(',')
    return longitude, latitude


def put_data_to_company_address(new_address_record):
    url = 'http://47.93.181.36:11007/v5/company/address'  # 线上
    # url = 'http://39.96.43.140:11007/v5/company/address'  # 沙盒
    headers = {'Content-Type': 'application/json'}
    params = new_address_record

    res = requests.put(url, data=params, headers=headers)
    print(res.status_code, res.text)
    return res


# if __name__ == '__main__':
def main(company_id):
    mysql_address_records = get_mysql_company_address_record(company_id)
    for address in mysql_address_records:
        try:
            longitude, latitude = get_longitude_latitude_data(address.get('address_2'))
            # longitude, latitude = get_longitude_latitude_data(address.get('address'))
            address['longitude'] = float(longitude)
            address['latitude'] = float(latitude)
            del address['address_2']  # 删除辅助的字段
            address_str = json.dumps(address)
            print(address_str)
            put_data_to_company_address(address_str)
        except (IndexError, UnboundLocalError, KeyError):
            print("数据异常")
        else:
            print("执行成功")


main(3796068)  # 捞王
