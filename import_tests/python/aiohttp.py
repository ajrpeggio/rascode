#!/usr/bin/env python3


try:
    import aiohttp
    print("Successful import of aiohttp. ")
except ImportError as e:
    print("Error importing aiohttp. ")
    print(e)
