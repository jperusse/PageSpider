import os
import argparse
from utilities import url_utilities

class PageReport:
    def create_page_report(self):
        return True

    def print_page_report(self):
        return True


def main(database: str, url_file_list: str):
    big_word_list = []
    print("We are going to work with " + database)
    print("We are going to scan " + url_file_list)
    urls = url_utilities.load_urls_from_file(url_file_list)
    for url in urls:
        print("reading url: " + url)
        page_content = url_utilities.load_page(url=url)
        words = url_utilities.scrape_page(page_contents=page_content)
        big_word_list.extend(words)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", "--database", help="SQLite File Name")
    parser.add_argument("-i", "--input", help="File containing urls to read")
    args = parser.parse_args()
    database_file = args.database
    input_file = args.input
    main(database=database_file, url_file_list=input_file)
