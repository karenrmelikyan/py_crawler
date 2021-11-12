from bs4 import BeautifulSoup
from lib import async_crawler, useful, async_proxy_crawler
from urllib import parse


def run(start_url, required) -> None:
    # extract and save domain name & protocol
    domain = useful.get_domain(start_url)
    protocol = useful.get_protocol(start_url)

    # first request by first URL
    urls = async_crawler.run([start_url], get_all_urls)[0]
    # save first url
    visited = [start_url]
    # filter
    filtered = get_filtered_urls(urls, domain, protocol)
    # first bulk request and get matrix of urls
    urls_matrix = async_crawler.run(filtered, get_all_urls)
    # save before next request
    visited += list(map(lambda url: url, filtered))

    while urls_matrix:
        filtered = sum(urls_matrix, [])
        filtered = get_filtered_urls(filtered, domain, protocol)
        filtered = list(set(visited) ^ set(filtered))
        urls_matrix = async_crawler.run(filtered, get_all_urls)
        visited += list(map(lambda url: url, filtered))

        # add to file required URLs
        required_urls = list(filter(lambda x: required in x, filtered))
        if required_urls:
            with open('urls.txt', 'a') as file:
                for url in required_urls:
                    file.write(url + "\n")

def proxy_run(start_url, required) -> None:
    # extract and save domain name & protocol
    domain = useful.get_domain(start_url)
    protocol = useful.get_protocol(start_url)

    # first request by first URL
    urls = async_proxy_crawler.run([start_url], get_all_urls)[0]
    # save first url
    visited = [start_url]
    # filter
    filtered = get_filtered_urls(urls, domain, protocol)
    # first bulk request and get matrix of urls
    urls_matrix = async_proxy_crawler.run(filtered, get_all_urls)
    # save before next request
    visited += list(map(lambda url: url, filtered))

    while urls_matrix:
        filtered = sum(urls_matrix, [])
        filtered = get_filtered_urls(filtered, domain, protocol)
        filtered = list(set(visited) ^ set(filtered))
        urls_matrix = async_proxy_crawler.run(filtered, get_all_urls)
        visited += list(map(lambda url: url, filtered))

        # add to file required URLs
        required_urls = list(filter(lambda x: required in x, filtered))
        if required_urls:
            with open('urls.txt', 'a') as file:
                for url in required_urls:
                    file.write(url + "\n")



def get_filtered_urls(all_urls, domain, protocol) -> list:
    def make_url_absolute(url) -> str:
        return url if url.startswith('http') else protocol + '://' + domain + '/' + url

    def is_local_url(full_url, domain) -> bool:
        result = parse.urlparse(full_url)
        if result.scheme not in [protocol, '']:
            return False
        if result.netloc == domain or result.scheme == '':
            return True

    return list(set(map(make_url_absolute, filter(lambda url: is_local_url(url, domain), all_urls))))


def get_all_urls(html) -> list:
    urls = []
    try:
        soup = BeautifulSoup(html, 'html5lib')
        soup_a = soup.find_all('a')

        urls = list(set((map(lambda a: a.get('href'), soup_a))))

    except Exception as e:
        print('Error in get_all_urls')
        print(e)

    return urls


def print_list(elems_list):
    for elem in elems_list:
        print(elem)
