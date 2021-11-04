from bs4 import BeautifulSoup
from lib import async_crawler, useful


def run(start_url, urls_param) -> None:
    async_crawler.run([start_url], scraper, domain=useful.get_domain(start_url), param=urls_param)


def scraper(html, **kwargs) -> bool:
    all_urls = get_all_urls(html)
    urls_sorting(all_urls, **kwargs)

    return True


# separating URLs for visit and save
def urls_sorting(all_urls, **kwargs):
    data = []
    for obj in kwargs.items():
        data.append(obj)
    domain_name = data[0]
    urls_param = data[1]

    local_urls = []


# first of all sort all local URLs
# for url in all_urls:
#     domain_name = useful.get_domain(url)
#     if domain_name == domain:
#         local_urls.append(url)
#     else:
#         if not domain_name:
#             local_urls.append(domain + url)
#
# print(local_urls)


def get_no_visited(urls):
    pass


def unique_resorting(urls):
    pass


def save_urls(urls):
    pass


def get_all_urls(html):
    urls = []
    soup = BeautifulSoup(html, 'html5lib')
    soup_a = soup.find_all('a')
    # urls.append(map(lambda a: a['href'], soup_a))
    for a in soup_a:
        urls.append(a['href'])

    return urls
