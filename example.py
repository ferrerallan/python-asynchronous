import asyncio
import random
import time

import asyncio

counter=1

async def count(word):
    global counter
    print(word)
    counter+=1
    await asyncio.sleep(1)
    print("end")
    print(counter)
    

async def hello():
    print("hello")
    
async def end():
    await asyncio.sleep(2)
    print("real end", counter)

async def main():
    await asyncio.gather(count("a"), count("b"), count("c"), hello())

if __name__ == "__main__":
    asyncio.run(main())
    print("end", counter)
    
    