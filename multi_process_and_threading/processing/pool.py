#!/usr/bin/env python
# encoding: utf-8
"""
@author: guihehans
@file: pool.py
@time: 2020/7/20 11:12
@function:

"""

from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


import multiprocessing as mp
import time


def foo_pool(x, y):
    time.sleep(2)
    return x * x + y


result_list = []


def log_result(result):
    # This is called whenever foo_pool(i) returns a result.
    # result_list is modified only by the main process, not the pool workers.
    result_list.append(result)


def apply_async_with_callback():
    pool = mp.Pool()
    for i in range(10):
        pool.apply_async(foo_pool, args=(i, 1), callback=log_result)
    pool.close()
    pool.join()
    print(result_list)


if __name__ == '__main__':
    start = time.time()
    apply_async_with_callback()
    end = time.time()
    print("finished in {}".format(end - start))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     start=time.time()
#     p = Pool(6)
#     for i in range(6):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done. in {}'.format(time.time()-start))
