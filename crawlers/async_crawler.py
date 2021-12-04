import random
import aiohttp
import asyncio
import platform
from fake_useragent import UserAgent


# for avoiding characteristic bugs in Windows
# implementations of async tasks are different
def run(urls, scraper):
    try:
        if platform.system() == 'Windows':
            return asyncio.get_event_loop().run_until_complete(launch(urls, scraper))
        else:
            return asyncio.run(launch(urls, scraper))
    except Exception as e:
        print(e)


async def launch(urls, scraper):
    for chunk_urls in chunks(urls, 100):
        for function in asyncio.as_completed([get_content(url) for url in chunk_urls]):
            # get page content
            html = await function
            # launch callback
            scraper(html)


async def get_content(url) -> str:
    async with aiohttp.ClientSession(headers=get_headers()) as session:
        async with session.get(url) as response:
            return await response.text()


def get_headers() -> dict:
    def get_rand_user_agent() -> str:
        ua_dict = UserAgent().data
        ua_list = ua_dict['browsers']['chrome']

        return ua_list[random.randrange(0, len(ua_list) - 1)]

    def get_rand_referer() -> str:
        referers = [
            'https://www.google.com',
            'https://www.bing.com',
            'https://www.facebook.com',
            'https://www.google.com',
            'https://yandex.com',
            'https://www.yahoo.com',
            'https://www.google.com',
        ]

        return referers[random.randrange(0, len(referers) - 1)]

    return {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
                  "application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Dnt": "1",
        "Referer": get_rand_referer(),
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": get_rand_user_agent(),
    }


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
