from scrapy.selector import Selector
from scrapy.spider import Spider

from SearchEngineScrapy.utils.searchengines import SearchEngineResultSelector
from SearchEngineScrapy.utils.searchenginepages import SearchEngineURLs

class SearchEngineScrapy(Spider):
    name = "SearchEngineScrapy"

    allowed_domains = ['bing.com','google.com']
    start_urls = []

    searchQuery = None
    searchEngine = None
    selector = None

    def __init__(self, searchQuery, searchEngine = "bing", pages = 3, *args, **kwargs):
        super(SearchEngineScrapy, self).__init__(*args, **kwargs)
        self.searchQuery = searchQuery.lower()
        self.searchEngine = searchEngine.lower()
        self.pages = int(pages)

        pageUrls = SearchEngineURLs(self.searchQuery, self.searchEngine, self.pages)
        self.selector = SearchEngineResultSelector[self.searchEngine]

        for url in pageUrls:
            self.start_urls.append(url)
    
    def parse(self, response):
        for url in Selector(response).xpath(self.selector).extract():
            yield { 'url': url }
        
        pass