from page_spider import PageReport


class TestPageSpider:
    def test_create_page_report(self):
        pr = PageReport()
        results = pr.create_page_report()
        assert results == True

    def test_print_page_report(self):
        pr = PageReport()
        results = pr.print_page_report()
        assert results == True
