import asyncio
import time

now = lambda: time.time()


async def dosomething(num):
    print("第 {} 任務，第一步".format(num))
    await asyncio.sleep(2)
    print("第 {} 任務，第二步".format(num))
    return "第 {} 任務完成".format(num)




async def main():
    tasks = [dosomething(i) for i in range(5)]

    results = await asyncio.gather(*tasks)
    return results


if __name__ == '__main__':
    start = now()
    r=asyncio.run(main())
    print(r)
    print("TIME: ", now() - start)
