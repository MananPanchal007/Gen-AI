# async functions and await keyword
# This code demonstrates the use of async functions and the await keyword in Python.

import asyncio

async def greet():
    print("Start greeting...")
    await asyncio.sleep(2)
    print("Hello after 2 seconds!")

async def main():
    await greet()

asyncio.run(main())
