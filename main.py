import random
import time
from lib import multy_processing_chrome_crawler
from scrapers import linkedin

if __name__ == '__main__':
    multy_processing_chrome_crawler.run(['https://www.linkedin.com/in/karen-melikyan-450732219/'],
                                        linkedin.browser_manager, 1)












    # urls = [
    #     'https://medium.com/umbrella-network/tagged/umbrella-network-news',
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
    # ]
