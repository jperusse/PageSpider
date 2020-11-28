from unittest.mock import MagicMock

import pytest
from pytest import raises

from utilities.url_utilities import load_page, load_urls_from_file, scrape_page


class TestURLUtils:
    firstURL = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    fmissing = "missing_file.txt"

    @pytest.fixture()
    def mock_open(self, monkeypatch):

        mock_file = MagicMock()
        mock_file.readlines = MagicMock(return_value=[self.firstURL])
        mock_open = MagicMock(return_value=mock_file)
        monkeypatch.setattr("builtins.open", mock_open)
        return mock_open

    def test_read_file_with_urls_missing_file(self):
        urls = load_urls_from_file(self.fmissing)
        assert urls == "File Not Found"

    def test_read_file_with_urls_none_in_file(self):
        urls = load_urls_from_file("urls0.txt")
        assert [] == urls

    def test_read_file_with_1url(self, mock_open, monkeypatch):

        mock_exists = MagicMock(return_value=True)
        monkeypatch.setattr("os.path.exists", mock_exists)

        urls = load_urls_from_file("urls1.txt")
        mock_open.assert_called_once_with("urls1.txt", "r")
        assert urls == [self.firstURL]

    def test_read_file_with_2urls(self):
        urls = load_urls_from_file("urls.txt")
        assert 2 == len(urls)

    def test_load_page(self):
        html = load_page(self.firstURL)
        assert html != False

    def test_load_page_missing_url(self):
        html = load_page('')
        assert html == False

    def test_load_page_url_not_found(self):
        html = load_page("https//:www.bad_url.com")
        assert html == False

    def test_scrape_page(self):
        html = load_page(self.firstURL)
        clean_words = scrape_page(page_contents=html)
        assert clean_words != False
