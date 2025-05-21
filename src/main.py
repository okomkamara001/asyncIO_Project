import asyncio
import time 


async def save_after(delay, what):
  await asyncio.sleep(delay)
  print()


asyncio.run(hello_world())



