import pytest
import os
from utilities.url_utilities import load_urls_from_file
from utilities.url_utilities import load_page
from utilities.url_utilities import scrape_page


class TestURLUtils:
    def setup_method(self, method):
        self.url1 = "https://en.wikipedia.org/wiki/Python_(programming_language)"
        return

    def teardown_method(self, method):
        return "method"

    def test_read_file_with_urls_missing_file(self):
        urls = load_urls_from_file("missing_file.txt")
        assert urls == "File Not Found"

    def test_read_file_with_urls_none_in_file(self):
        urls = load_urls_from_file("urls0.txt")
        assert [] == urls

    def test_read_file_with_1url(self):
        cwd = os.getcwd()
        print(cwd)
        urls=load_urls_from_file("urls1.txt")
        assert 1 == len(urls)

    def test_read_file_with_2urls(self):
        urls=load_urls_from_file("urls.txt")
        assert 2 == len(urls)

    def test_load_page(self):
        html=load_page(self.url1)
        assert html != False

    def test_load_page_missing_url(self):
        html=load_page('')
        assert html == False

    def test_load_page_url_not_found(self):
        html=load_page("https//:www.bad_url.com")
        assert html == False

    def test_scrape_page(self):
        html=load_page(self.url1)
        clean_words=scrape_page(page_contents = html)
        assert clean_words != False
