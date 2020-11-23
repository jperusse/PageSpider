import unittest
from page_spider import PageReport


class TestPageSpider(unittest.TestCase):
    def test_create_page_report(self):
        pr = PageReport()
        results = pr.create_page_report()
        self.assertTrue(results)

    def test_print_page_report(self):
        pr = PageReport()
        results = pr.print_page_report()
        self.assertTrue(results)


if __name__ == '__main__':
    unittest.main()
