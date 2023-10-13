import asyncio
import random
import time

import asyncio

counter=1

async def count(word, nsleep):
    global counter
        
    ind=0
    while ind < nsleep+4:
        print(word, "rodando")
        await asyncio.sleep(nsleep)
        ind+=1
    
    counter+=1
    print(counter)
    

async def hello():
    print("hello")
    
async def end():
    await asyncio.sleep(2)
    print("real end", counter)

async def main():
    await asyncio.gather(count("processo 1", 1), count("processo 2",2), count("processo 3",3), hello())
    print("agora sim")

if __name__ == "__main__":
    asyncio.run(main())
    print("end", counter)
    
    