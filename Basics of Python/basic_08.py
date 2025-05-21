# async functions and await keyword
# This code demonstrates the use of async functions and the await keyword in Python.
# Import the asyncio module for asynchronous programming in Python


import asyncio

# Define an asynchronous function called 'greet'
async def greet():
    # Print a message indicating the start of the greeting
    print("Start greeting...")
    
    # Pause the function for 2 seconds without blocking the event loop
    await asyncio.sleep(2)
    
    # Print a message after the delay
    print("Hello after 2 seconds!")

# Define another asynchronous function called 'main'
async def main():
    # Await the completion of the 'greet' coroutine
    await greet()

# Start the event loop and run the 'main' coroutine
asyncio.run(main())

