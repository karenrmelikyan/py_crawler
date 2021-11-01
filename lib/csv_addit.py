import csv


def add_row_to_csv(row, file_name) -> bool:
    try:
        with open(file_name, 'a', newline='', encoding='UTF-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(row)
        return True
    except Exception as ex:
        return False
