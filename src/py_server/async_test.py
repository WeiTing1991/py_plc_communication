#!/usr/bin/env python3

import asyncio

async def main():
    print("A")
    await print_num()
    print("B")

async def print_num():
    print("1")
    print("2")

asyncio.run(main())