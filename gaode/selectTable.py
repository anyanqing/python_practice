import pymysql
import torndb
# torndb.Connection().get()


def select_from_table():
    while True:
        conn = pymysql.connect(host='db-d.dqprism.com', port=3306, user='daqi',
                               password='7f1a45eac5985519829c929e7bbf0557')  # 沙盒mysql
        cursor = conn.cursor()
        sql_insert = "select score from jobdb.job_application_score limit 2;"
        cursor.execute(sql_insert)
        conn.commit()
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result
