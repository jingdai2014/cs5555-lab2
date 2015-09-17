import csv
import logging
from collections import defaultdict

logging.basicConfig(filename='loader.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class Person(object):
    def __init__(self):
        self.info = {}
        self.person_id = None


def load_info(filename, rows):
    """
    Loads data
    : param filename:
    : return:
    """
    header = True
    headers = {}
    check_len = None
    with open(filename,  'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            if header:
                for i, key in enumerate(row):
                    headers[i] = key
                header = False
                check_len = len(row)
            elif check_len == len(row):
                # everything is a string
                rows[row[0]].person_id = int(row[0])
                for i, value in enumerate(row):
                    rows[row[0]].info[headers[i]] = num(value)
            else:
                logging.exception("length check failed :  " + str(row))
    logging.info("number of rows: " + str(len(rows)))
    for c in rows.itervalues():
        logging.info('\t'.join([str(c.person_id), str(len(c.info))]))
        break


def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)


def load_raw():
    rows = defaultdict(Person)
    load_info('2012-Consolidated-stripped.csv', rows)
    return rows

if __name__ == '__main__':
    rows = load_raw()
    print rows['20004101'].person_id, rows['20004101'].info
    # print rows