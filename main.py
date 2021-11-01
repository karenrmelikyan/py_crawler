import time

import aiohttp
import asyncio
from lib import async_proxy_crawler


def scraper(i):
    print(str(i) + ' start')
    # await asyncio.sleep(0.25)
    time.sleep(1)
    print(str(i) + ' finish')

async_proxy_crawler.run([
    'https://docs.aiohttp.org/en/stable/',
    'https://docs.aiohttp.org/en/stable/',
    'https://docs.aiohttp.org/en/stable/',
    'https://docs.aiohttp.org/en/stable/',
    'https://docs.aiohttp.org/en/stable/',
    'https://docs.aiohttp.org/en/stable/',
    'https://docs.aiohttp.org/en/stable/',
    'https://docs.aiohttp.org/en/stable/',
    'https://docs.aiohttp.org/en/stable/',
    'https://docs.aiohttp.org/en/stable/',
    'https://docs.aiohttp.org/en/stable/',
    'https://docs.aiohttp.org/en/stable/',
    'https://docs.aiohttp.org/en/stable/',
    'https://docs.aiohttp.org/en/stable/',
    'https://docs.aiohttp.org/en/stable/',
    'https://docs.aiohttp.org/en/stable/',
    'https://docs.aiohttp.org/en/stable/',
    'https://docs.aiohttp.org/en/stable/',
    'https://docs.aiohttp.org/en/stable/',
    'https://docs.aiohttp.org/en/stable/',
    'https://docs.aiohttp.org/en/stable/',
    'https://docs.aiohttp.org/en/stable/',
    'https://docs.aiohttp.org/en/stable/',
    'https://docs.aiohttp.org/en/stable/',
], scraper)
