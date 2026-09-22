# try/except block
import asyncio


async def hot_dog_contest():
    try:
        print("Welcome to the Hot Dog Eating Contest!")
        await asyncio.sleep(1)
        print("The contest is starting now!")
        await asyncio.sleep(1)
        print("Contestants are eating hot dogs...")
        await asyncio.sleep(2)
        print("The contest has ended!")
    except Exception as e:
        print(f"An error occurred: {e}")


async def main():
    await hot_dog_contest()


if __name__ == "__main__":
    asyncio.run(main())


    