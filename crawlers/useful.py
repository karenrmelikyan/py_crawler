import csv
from urllib.parse import urlparse
from urllib import parse

"""
URLs
"""


def is_local_url(full_url, domain, protocol) -> bool:
    result = parse.urlparse(full_url)
    if result.scheme not in [protocol, '']:
        return False
    if result.netloc == domain or result.scheme == '':
        return True


def get_domain(url) -> str:
    return urlparse(url).netloc


def get_protocol(url) -> str:
    parsed_uri = urlparse(url)
    return '{uri.scheme}'.format(uri=parsed_uri)


"""
CSV files
"""


def add_row_to_csv(row, file_name):
    with open(file_name, 'a', newline='', encoding='UTF-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(row)
