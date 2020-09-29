# -*- coding: utf-8 -*-

import pymysql


def _table_insert(name, age):
    while True:
        conn = pymysql.connect(host='db-d.dqprism.com', port=3306, user='daqi',
                               password='7f1a45eac5985519829c929e7bbf0557')  # 沙盒mysql
        cursor = conn.cursor()
        sql_insert = "insert into datateam.test_thread (name, age) values (%s, %d);"
        cursor.execute(sql_insert % (name, age))
        conn.commit()
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result


if __name__ == '__main__':
    _table_insert('\'ccc\'', 30)

