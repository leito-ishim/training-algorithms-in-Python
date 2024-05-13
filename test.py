# import asyncio
#
# async def hello():
#     await asyncio.sleep(1)
#     print('hello')
#
# async def world():
#     await asyncio.sleep(2)
#     print('world')
#
#
# async def main():
#     await asyncio.gather(hello(), world())
#
#
# if __name__ == '__main__':
#     asyncio.run(main())

# print(-120 % 200)
# a = [1,2,3,4,5,6,7,8,9]
# b = [1,2,3,4,5,6,7,8,9]
#
#
# print(id(a))
# print(id(b))


# def my_generator():
#     yield 1
#     yield 1
#     yield 2
#
#
# my_iterator = my_generator()
# print(next(my_iterator))
#
def my_generator(n):
    for i in range(n + 1):
        yield i

my_gen = my_generator(5)
for i in my_gen:
    print(i)