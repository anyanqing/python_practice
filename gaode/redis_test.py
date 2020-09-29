# -*- coding: utf-8 -*-
# import rediscluster
import redis
import pymysql


# 从MySQL获取candidate_profile_id
def get_candidate_profile_id_from_mysql():
    candidate_profile_ids = []
    conn = pymysql.connect(host='db-d.dqprism.com', port=3306, user='daqi',
                           password='7f1a45eac5985519829c929e7bbf0557')  # 沙盒
    cursor = conn.cursor()
    # sql = "select candidate_profile_id from jobdb.job_application where candidate_profile_id is not null limit 10000;"
    sql = """
        select 
            distinct a.candidate_profile_id
        from jobdb.job_application a
        left join jobdb.job_application_score b on a.id=b.application_id
        where a.candidate_profile_id is not null and b.id is null
        order by a.submit_time desc
        limit 1000
        ;
    """
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    for result in results:
        candidate_profile_ids.append(result[0])
    return candidate_profile_ids


# 向redis批量推入candidate_profile_id
def put_candidate_profile_id_to_redis(candidate_profile_ids):

    # rds = rediscluster.StrictRedisCluster(startup_nodes=settings.redis_cluster_startup_nodes)
    rds = redis.StrictRedis(host="127.0.0.1", port=6379)
    redis_key = 'ES_CRON_UPDATE_INDEX_APPLICATION_CANDIDATE_IDS'

    with rds.pipeline(transaction=False) as pl:
        for candidate_profile_id in candidate_profile_ids:
            pl.lpush(redis_key, candidate_profile_id)
        pl.execute()
        print('candidate_profile_ids has been pushed in.')


def main():
    candidate_profile_ids = get_candidate_profile_id_from_mysql()
    put_candidate_profile_id_to_redis(candidate_profile_ids)


if __name__ == '__main__':
    main()
