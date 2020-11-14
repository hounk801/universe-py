# -*- coding: utf-8 -*-
import threading
import time


class MyThread(threading.Thread):
    def __init__(self, second):
        threading.Thread.__init__(self)
        self.second = second

    def run(self):
        print(f'Threading {threading.current_thread().name} is running')
        print(f'Threading {threading.current_thread().name} sleep {self.second}s')
        time.sleep(self.second)
        print(f'Threading {threading.current_thread().name} is ended')


print(f'Threading {threading.current_thread().name} is running')
threads = []
for i in [1, 5]:
    thread = MyThread(i)
    threads.append(thread)
    thread.start()

# 主线程等待子线程运行完毕之后才退出，可以让每个子线程对象都调用下    join    方法
for thread in threads:
    thread.join()
print(f'Threading {threading.current_thread().name} is ended')
