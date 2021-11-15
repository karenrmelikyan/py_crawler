import time
import random
import aiohttp
import asyncio
import requests
import platform
from fake_useragent import UserAgent
from aiohttp_proxy import ProxyConnector


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
    data = []
    proxy_list = get_proxy_list()
    for chunk_urls in chunks(urls, 100):
        # run x(0)..x(10) concurrently and process results as they arrive
        for function in asyncio.as_completed([get_content(url, proxy_list) for url in chunk_urls]):
            html = await function
            # scrap data
            data.append(scraper(html))

    return data


async def get_content(url, proxy_list) -> str:
    proxy_counter = len(proxy_list)
    for proxy in proxy_list:
        proxy_counter -= 1
        connector = ProxyConnector.from_url('socks4://' + proxy)
        try:
            async with aiohttp.ClientTimeout(total=None, sock_connect=6, sock_read=6):
                async with aiohttp.ClientSession(connector=connector, headers=get_headers()) as session:
                    async with session.get(url, allow_redirects=False, timeout=5) as response:
                        # if was been reached end of proxy list
                        if proxy_counter <= 1:
                            raise ReachProxyListLimit(f'Exception!!! Reach of proxy list limit for url {url}')

                        return await response.text()

        except Exception as e:
            continue


def get_proxy_list() -> list:
    attempts = 0
    status_code = 0
    response = None

    while status_code != 200 and attempts < 10:
        attempts += 1
        # get socks4 proxies
        response = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000'
                                '&country=all&ssl=all&anonymity=all', headers=get_headers())
        status_code = response.status_code
        time.sleep(random.randrange(2, 4))

    if attempts >= 9:
        raise NotReceivedProxiesException('EXCEPTION!!! Was not received proxy list')

    # get proxy list from response
    socks4_proxy_list = response.text.split("\r\n")

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


def chunks(lst, n=100):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


class NotReceivedProxiesException(Exception):
    pass


class ReachProxyListLimit(Exception):
    pass
