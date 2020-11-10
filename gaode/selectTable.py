import pymysql
import torndb

db = torndb.Connection(
            host='db-d.dqprism.com',
            database='jobdb',
            user='daqi',
            password='7f1a45eac5985519829c929e7bbf0557',
            max_idle_time=180,
            charset='utf8',
            time_zone="+8:00"
        )


def select_from_table():
    # conn = pymysql.connect(host='db-d.dqprism.com', port=3306, user='daqi',
    #                        password='7f1a45eac5985519829c929e7bbf0557')  # 沙盒mysql
    # cursor = conn.cursor()
    sql = "select id,status,score from jobdb.job_application_evaluate limit 2;"
    # cursor.execute(sql)
    # conn.commit()
    # result = cursor.fetchall()
    # cursor.close()
    # conn.close()

    result = db.query(sql)
    print(result)

    evaluate_status = 0
    evaluate_score = None
    if result:
        for res in result:
            if res.get('status') != 1:
                evaluate_status = 2
            else:
                evaluate_status = 1

            if res.get("score"):
                evaluate_score = res.get("score")
    print(evaluate_status, evaluate_score)
    return evaluate_status, evaluate_score


aaa, bbb = select_from_table()

print(aaa, bbb)
