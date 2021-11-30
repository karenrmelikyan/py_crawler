from crawlers import async_crawler
from multiprocessing import Process
from helium import *


def run(urls, browser_manager, chunk):
    # run all processes by chunk urls
    for chunk_urls in async_crawler.chunks(urls, chunk):
        launch_processes(chunk_urls, browser_manager)


def launch_processes(chunk_urls, browser_manager):
    p = None
    # create and start
    # chunked processes
    for url in chunk_urls:
        p = Process(target=process, args=(url, browser_manager,))
        p.start()

    # waiting of end last
    # chunked processes
    p.join()


def process(url, browser_manager):
    # invoke callback
    browser_manager(url, helium)
