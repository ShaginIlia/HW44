import asyncio
import time


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for ball in range(5):
        delay = 1 / power
        await asyncio.sleep(delay)
        print(f'Силач {name} поднял {ball + 1} шар')
    print(f'Силач {name} закончил соревнования')


async def start_tournament():
    strongman1 = asyncio.create_task(start_strongman('Денис', 3))
    strongman2 = asyncio.create_task(start_strongman('Вася', 2))
    strongman3 = asyncio.create_task(start_strongman('Ашот', 4))
    await strongman1
    await strongman2
    await strongman3

asyncio.run(start_tournament())

