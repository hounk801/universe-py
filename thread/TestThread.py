# -*- coding: utf-8 -*-
import threading
import time


def my_thread(second):
    print(f"Threading1 {threading.current_thread().name} is running")
    print(f"Threading2 {threading.current_thread().name} sleep {second} s")
    time.sleep(second)
    print(f"Threading3 {threading.current_thread().name} sleep end")


print(f"Threading4 {threading.current_thread().name} is run")
for i in [1, 5]:
    thread = threading.Thread(target=my_thread, args=[i])
    thread.start()

print(f"Threading5 {threading.current_thread().name} end")
