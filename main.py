from lib import async_crawler, async_proxy_crawler, all_urls_scraper


def scraper(html):
    print('ok')


if __name__ == '__main__':
    async_proxy_crawler.run([
        'https://docs.python.org/3/tutorial/errors.html',
        'https://www.upwork.com/ab/jobs/search/?page=2&q=web%20application%20scraping&sort=recency',
        'https://www.youtube.com/watch?v=QkHqgJIHD94',
        'https://selenium-python-helium.readthedocs.io/en/latest/api.html',
        'https://docs.aiohttp.org/en/stable/client_advanced.html',
        'https://stackoverflow.com/questions/64534844/python-asyncio-aiohttp-timeout',
        'https://docs.python.org/3/tutorial/errors.html',
        'https://www.upwork.com/ab/jobs/search/?page=2&q=web%20application%20scraping&sort=recency',
        'https://www.youtube.com/watch?v=QkHqgJIHD94',
        'https://selenium-python-helium.readthedocs.io/en/latest/api.html',
        'https://docs.aiohttp.org/en/stable/client_advanced.html',
        'https://stackoverflow.com/questions/64534844/python-asyncio-aiohttp-timeout',
        'https://docs.python.org/3/tutorial/errors.html',
        'https://www.upwork.com/ab/jobs/search/?page=2&q=web%20application%20scraping&sort=recency',
        'https://www.youtube.com/watch?v=QkHqgJIHD94',
        'https://selenium-python-helium.readthedocs.io/en/latest/api.html',
        'https://docs.aiohttp.org/en/stable/client_advanced.html',
        'https://stackoverflow.com/questions/64534844/python-asyncio-aiohttp-timeout',
        'https://docs.python.org/3/tutorial/errors.html',
    ], scraper)
