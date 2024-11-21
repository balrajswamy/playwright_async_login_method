import asyncio

async def greet(name):
    """An asynchronous function."""
    return f"Hello, {name}!"

# Example usage
async def main():
    result = await greet("Alice")
    print(result)

# Running the asynchronous function
asyncio.run(main())
