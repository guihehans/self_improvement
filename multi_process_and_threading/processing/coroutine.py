import asyncio
import time
from concurrent.futures.thread import ThreadPoolExecutor

now = lambda: time.time()


async def dosomething(num):
    print("第 {} 任務，第一步".format(num))
    await asyncio.sleep(2)
    print("第 {} 任務，第二步".format(num))
    return "第 {} 任務完成".format(num)


def func(num):
    print("第 {} 任務，第一步".format(num))
    time.sleep(2)
    print("第 {} 任務，第二步".format(num))
    return "第 {} 任務完成".format(num)


async def make_func_async(num):
    # init a new thread by ThreadPoolExecutor
    executor = ThreadPoolExecutor(2)
    # get the event loop
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(executor, func, num)
    return response


async def main():
    tasks = [make_func_async(i) for i in range(5)]
    # Unpacking Argument Lists *list, to fit gather arg.
    results = await asyncio.gather(*tasks)
    return results


if __name__ == '__main__':
    start = now()
    r = asyncio.run(main())
    print(r)
    print("TIME: ", now() - start)
