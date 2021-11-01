import time
import random
import aiohttp
import asyncio
import requests
from fake_useragent import UserAgent
from aiohttp_socks import ProxyConnector


def run(urls, scraper):
    loop = asyncio.new_event_loop()
    loop.run_until_complete(launch(urls, scraper))
    loop.close()


async def launch(urls, scraper):
    proxy_list = get_proxy_list()
    if proxy_list:
        # run x(0)..x(10) concurrently and process results as they arrive
        for f in asyncio.as_completed([get_content(url, proxy_list) for url in urls]):
            html = await f
            # scrap data
            scraper(html)


async def get_content(url, proxy_list) -> str:
    for proxy in proxy_list:
        connector = ProxyConnector.from_url('socks4://' + proxy)
        try:
            async with aiohttp.ClientSession(connector=connector, headers=get_headers()) as session:
                async with session.get(url) as response:
                    return await response.text()
        except Exception as e:
            continue


def get_proxy_list() -> list:
    status_code = 0
    res = None

    while status_code != 200:
        # get socks4 proxies
        res = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000'
                           '&country=all&ssl=all&anonymity=all', headers=get_headers())
        status_code = res.status_code
        time.sleep(random.randrange(2, 4))

    # get proxy list from response
    socks4_proxy_list = res.text.split("\r\n")

    # remove last empty element
    socks4_proxy_list.pop(len(socks4_proxy_list) - 1)

    return socks4_proxy_list


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
