import csv
from urllib.parse import urlparse


def add_row_to_csv(row, file_name):
    with open(file_name, 'a', newline='', encoding='UTF-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(row)


def get_domain(url) -> str:
    parsed_uri = urlparse(url)
    return '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
