from lib import async_crawler, async_proxy_crawler, all_urls_scraper, async_chrome_crawler


def scraper(html):
    print(html)


if __name__ == '__main__':
    urls = []
    for i in range(0, 480, 30):
        urls.append(f'https://docs.microsoft.com/en-us/learn/certifications/browse/?skip={i}')

    async_chrome_crawler.run(urls, scraper)


# if __name__ == '__main__':
#     def scraper(html):
#         return html

# async_proxy_crawler.run([
#     'https://docs.python.org/3/tutorial/errors.html',
#     'https://www.upwork.com/ab/jobs/search/?page=2&q=web%20application%20scraping&sort=recency',
#     'https://www.youtube.com/watch?v=QkHqgJIHD94',
#     'https://selenium-python-helium.readthedocs.io/en/latest/api.html',
#     'https://docs.aiohttp.org/en/stable/client_advanced.html',
#     'https://stackoverflow.com/questions/64534844/python-asyncio-aiohttp-timeout',
#     'https://docs.python.org/3/tutorial/errors.html',
#     'https://www.upwork.com/ab/jobs/search/?page=2&q=web%20application%20scraping&sort=recency',
#     'https://www.youtube.com/watch?v=QkHqgJIHD94',
#     'https://selenium-python-helium.readthedocs.io/en/latest/api.html',
#     'https://docs.aiohttp.org/en/stable/client_advanced.html',
#     'https://stackoverflow.com/questions/64534844/python-asyncio-aiohttp-timeout',
#     'https://docs.python.org/3/tutorial/errors.html',
#     'https://www.upwork.com/ab/jobs/search/?page=2&q=web%20application%20scraping&sort=recency',
#     'https://www.youtube.com/watch?v=QkHqgJIHD94',
#     'https://selenium-python-helium.readthedocs.io/en/latest/api.html',
#     'https://docs.aiohttp.org/en/stable/client_advanced.html',
#     'https://stackoverflow.com/questions/64534844/python-asyncio-aiohttp-timeout',
#     'https://docs.python.org/3/tutorial/errors.html',
# ], scraper)
