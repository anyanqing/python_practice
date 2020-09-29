import threading
import queue
import time
import timeit

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, threadName, taskQueue):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.threadName = threadName
        self.taskQueue = taskQueue

    def run(self):
        print("开始线程：" + self.threadName)
        process_data(self.threadName, self.taskQueue)
        print("退出线程：" + self.threadName)


def process_data(threadName, taskQueue):
    while not exitFlag:
        queueLock.acquire()
        if not taskQueue.empty():
            data = taskQueue.get()
            queueLock.release()
            print("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        # time.sleep(1)


threadList = ["Thread-1", "Thread-2", "Thread-3"]
workList = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
            "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen"]
queueLock = threading.Lock()
workQueue = queue.Queue(15)
workPriorityQueue = queue.PriorityQueue(20)
threads = []
threadID = 1


# 创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1


# 填充队列
# queueLock.acquire()
for work in workList:
    workQueue.put(work)
# queueLock.release()

# 等待清空队列
while not workQueue.empty():
    continue

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()

print("退出主线程")
