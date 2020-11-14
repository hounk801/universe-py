# -*- coding: utf-8 -*-
import multiprocessing


# 进程是 Python 中最小的资源分配单元，因此这些进程和线程不同，各个进程之间的数据是不会共享的，每启动一个进程，都会独立分配资源。

def myprocess(index):
    print(f"Process:{index}")


if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=myprocess(i))
        p.start()

    print(f'CPU:{multiprocessing.cpu_count()}')
    for p in multiprocessing.active_children():
            print(f'Child process name: {p.name} id: {p.pid}')
    print('Process Ended')