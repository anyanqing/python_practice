import socket
import threading
from queue import Queue, Empty
import tableInsert
import pymysql
from time import time

# python3.2版本才开始有这个模块
from concurrent.futures import ThreadPoolExecutor, wait, as_completed, ProcessPoolExecutor


# reload(sys)

# 创建工作线程类
class WorkerThread(threading.Thread):
    # 线程超时时间
    timeout = 5
    # 线程数量
    worker_count = 0

    def __init__(self, workQueue, resultQueue, **kwargs):
        threading.Thread.__init__(self)
        self.id = self.worker_count
        self.setDaemon(True)
        self.workQueue = workQueue
        self.resultQueue = resultQueue
        self.start()

    def run(self) -> None:
        while True:
            WorkerThread.worker_count += 1
            try:
                callable, args, kwargs = self.workQueue.get(timeout=WorkerThread.timeout)
                result = callable(*args, **kwargs)
                # print('mythread {id}: {result}'.format(id=self.id, result=result))
                self.resultQueue.put(result)
            except Empty:
                break
            except Exception as e:
                # print('mythread {id}: {exc}'.format(id=self.id, exc=sys.exc_info()[:2]))
                raise
        return


class ThreadManager:
    """
    线程管理类
    """
    def __init__(self, num_of_workers=10, timeout=2):
        self.workQueue = Queue(0)
        self.resultQueue = Queue(0)
        self.workers = []
        self.timeout = timeout
        self._recruit_threads(num_of_workers)

    def _recruit_threads(self, num_of_workers):
        for i in range(num_of_workers):
            worker = WorkerThread(self.workQueue, self.resultQueue)
            self.workers.append(worker)

    def wait_for_complete(self):
        while len(self.workers):
            worker = self.workers.pop()
            worker.join()
            if worker.is_alive() and not self.workQueue.empty():
                self.workers.append(worker)
        print("All jobs are completed.")

    def add_work(self, callable, *args, **kwargs):
        self.workQueue.put((callable, args, kwargs))

    def get_result(self, *args, **kwargs):
        return self.resultQueue.get(*args, **kwargs)


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


def main():
    # 使用线程池
    socket.setdefaulttimeout(10)
    print('start testing')
    thread_manager = ThreadManager(50)
    for i in range(100):
        name = '\'ccc\''
        age = 30
        thread_manager.add_work(tableInsert._table_insert, name, age)
    thread_manager.wait_for_complete()
    print('end testing')


if __name__ == '__main__':
    start_time = time()
    main()
    end_time = time()
    print(end_time-start_time)
